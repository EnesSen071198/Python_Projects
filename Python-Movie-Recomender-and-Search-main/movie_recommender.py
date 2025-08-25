"""
Film öneri uygulaması (Streamlit)

- İçerik tabanlı öneri: Tür (genres) TF/IDF + kosinüs benzerliği
- Kullanıcı tabanlı öneri: 
  - Eğer yüklüyse Surprise SVD kullanır
  - Aksi halde saf pandas + scikit-learn ile item-based (film-film) benzerlik fallback

Notlar:
- scikit-surprise Windows/Python 3.11 ortamında derleyici gerektirebilir. Bu durumda fallback otomatik devreye girer.
- OMDb poster anahtarı için ortam değişkeni (OMDB_API_KEY) veya Streamlit secrets kullanılabilir.
"""

import os
import requests
import numpy as np
import pandas as pd
import streamlit as st
from typing import List

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Surprise'i opsiyonel yap
HAVE_SURPRISE = False
try:
    from surprise import Dataset, Reader, SVD  # type: ignore
    HAVE_SURPRISE = True
except Exception:
    HAVE_SURPRISE = False


# -------- Yardımcı: Veri Yükleme --------
@st.cache_data(show_spinner=False)
def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """movies.csv ve ratings.csv dosyalarını yükler.
    Yoksa hata vermek yerine örnek küçük veri setiyle devam eder.
    """
    movies_path = "movies.csv"
    ratings_path = "ratings.csv"

    if os.path.exists(movies_path) and os.path.exists(ratings_path):
        movies_df = pd.read_csv(movies_path)
        ratings_df = pd.read_csv(ratings_path)
    else:
        # Örnek küçük veri (projeyle birlikte geliyor)
        movies_df = pd.DataFrame(
            [
                {"movieId": 1, "title": "Toy Story (1995)", "genres": "Adventure|Animation|Children|Comedy|Fantasy"},
                {"movieId": 2, "title": "Jumanji (1995)", "genres": "Adventure|Children|Fantasy"},
                {"movieId": 3, "title": "Grumpier Old Men (1995)", "genres": "Comedy|Romance"},
                {"movieId": 4, "title": "Waiting to Exhale (1995)", "genres": "Comedy|Drama|Romance"},
                {"movieId": 5, "title": "Father of the Bride Part II (1995)", "genres": "Comedy"},
                {"movieId": 6, "title": "Heat (1995)", "genres": "Action|Crime|Thriller"},
                {"movieId": 7, "title": "Sabrina (1995)", "genres": "Comedy|Romance"},
                {"movieId": 8, "title": "Tom and Huck (1995)", "genres": "Adventure|Children"},
                {"movieId": 9, "title": "Sudden Death (1995)", "genres": "Action"},
                {"movieId": 10, "title": "GoldenEye (1995)", "genres": "Action|Adventure|Thriller"},
            ]
        )
        ratings_df = pd.DataFrame(
            [
                {"userId": 1, "movieId": 1, "rating": 4.0},
                {"userId": 1, "movieId": 2, "rating": 3.5},
                {"userId": 1, "movieId": 3, "rating": 2.0},
                {"userId": 1, "movieId": 6, "rating": 4.5},
                {"userId": 2, "movieId": 1, "rating": 5.0},
                {"userId": 2, "movieId": 4, "rating": 3.0},
                {"userId": 2, "movieId": 7, "rating": 4.0},
                {"userId": 2, "movieId": 10, "rating": 4.5},
                {"userId": 3, "movieId": 2, "rating": 4.0},
                {"userId": 3, "movieId": 3, "rating": 3.5},
                {"userId": 3, "movieId": 5, "rating": 3.0},
                {"userId": 3, "movieId": 6, "rating": 4.0},
                {"userId": 4, "movieId": 1, "rating": 2.5},
                {"userId": 4, "movieId": 5, "rating": 4.0},
                {"userId": 4, "movieId": 9, "rating": 3.0},
                {"userId": 5, "movieId": 2, "rating": 4.5},
                {"userId": 5, "movieId": 6, "rating": 5.0},
                {"userId": 5, "movieId": 10, "rating": 4.0},
            ]
        )

    # Tip güvenliği
    movies_df = movies_df.copy()
    ratings_df = ratings_df.copy()
    if "movieId" in movies_df:
        movies_df["movieId"] = movies_df["movieId"].astype(int)
    if {"userId", "movieId"}.issubset(ratings_df.columns):
        ratings_df["userId"] = ratings_df["userId"].astype(int)
        ratings_df["movieId"] = ratings_df["movieId"].astype(int)
    return movies_df, ratings_df


movies, ratings = load_data()


# -------- 2. İçerik Tabanlı Öneri --------
def content_based_recommendations(title: str, top_n: int = 10) -> List[str]:
    if title not in set(movies["title"].tolist()):
        return []
    cv = CountVectorizer(stop_words="english")
    genres = movies["genres"].fillna("")
    count_matrix = cv.fit_transform(genres)
    cos = cosine_similarity(count_matrix)

    indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()
    idx = int(indices[title])
    sim_scores = list(enumerate(cos[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1 : top_n + 1]
    movie_indices = [i for i, _ in sim_scores]
    return movies.loc[movie_indices, "title"].tolist()


# -------- 3. Kullanıcı Tabanlı Öneri --------
@st.cache_resource(show_spinner=False)
def train_surprise(ratings_df: pd.DataFrame):
    if not HAVE_SURPRISE:
        return None
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(ratings_df[["userId", "movieId", "rating"]], reader)
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)
    return algo


def item_based_cf_recommendations(user_id: int, top_n: int = 10) -> List[int]:
    # Kullanıcı-ürün matrisi
    ui = ratings.pivot_table(index="userId", columns="movieId", values="rating")
    if user_id not in ui.index:
        return []
    ui_filled = ui.fillna(0.0)
    R = ui_filled.values  # (n_users, n_items)
    item_sim = cosine_similarity(R.T)  # (n_items, n_items)

    # Kullanıcı vektörü
    user_row = ui_filled.loc[user_id].values  # (n_items,)
    rated_mask = user_row > 0
    if not rated_mask.any():
        return []
    sim_masked = item_sim[:, rated_mask]  # (n_items, n_rated)
    numerator = sim_masked @ user_row[rated_mask]
    denominator = np.abs(sim_masked).sum(axis=1) + 1e-8
    pred = numerator / denominator
    # Zaten puan verdiklerini dışla
    pred[rated_mask] = -np.inf

    # En iyi N filmId
    top_idx = np.argpartition(-pred, range(min(top_n, len(pred))))[:top_n]
    # Skora göre sırala
    top_idx = top_idx[np.argsort(-pred[top_idx])]
    movie_ids = ui_filled.columns.values[top_idx].tolist()
    return [int(m) for m in movie_ids]


def collaborative_filtering_recommendations(user_id: int, top_n: int = 10) -> List[str]:
    # Önce Surprise dene (varsa)
    if HAVE_SURPRISE:
        algo = train_surprise(ratings)
        if algo is not None:
            all_movie_ids = movies["movieId"].unique().tolist()
            rated_movie_ids = ratings.loc[ratings["userId"] == user_id, "movieId"].tolist()
            unrated = [m for m in all_movie_ids if m not in rated_movie_ids]
            if not unrated:
                return []
            preds = [algo.predict(user_id, m) for m in unrated]
            preds.sort(key=lambda x: x.est, reverse=True)
            top_movies = [p.iid for p in preds[:top_n]]
            return movies.loc[movies["movieId"].isin(top_movies), "title"].tolist()

    # Fallback: item-based CF
    top_movie_ids = item_based_cf_recommendations(user_id, top_n=top_n)
    if not top_movie_ids:
        # Son çare: popülerlik bazlı öneri
        pop = (
            ratings.groupby("movieId").agg(cnt=("rating", "count"), mean=("rating", "mean")).reset_index()
        )
        pop = pop.sort_values(["cnt", "mean"], ascending=[False, False])
        top_movie_ids = pop["movieId"].head(top_n).astype(int).tolist()
    return movies.loc[movies["movieId"].isin(top_movie_ids), "title"].tolist()


# -------- 4. Film Posterleri --------
def _effective_omdb_key() -> str | None:
    # Öncelik sırası: sidebar input -> secrets -> env
    key = st.session_state.get("omdb_api_key") if "omdb_api_key" in st.session_state else None
    try:
        key = st.secrets.get("OMDB_API_KEY") or key  # type: ignore[attr-defined]
    except Exception:
        pass
    if not key:
        key = os.environ.get("OMDB_API_KEY")
    return key


def _parse_title_year(title: str) -> tuple[str, int | None]:
    # 'Movie Name (1995)' -> ("Movie Name", 1995)
    if title.endswith(")") and "(" in title:
        try:
            base = title[: title.rfind("(")].strip()
            year = int(title[title.rfind("(") + 1 : title.rfind(")")])
            return base, year
        except Exception:
            return title, None
    return title, None


@st.cache_data(show_spinner=False)
def _fetch_poster_from_omdb(name: str, year: int | None, api_key: str) -> str:
    try:
        # 1) Doğrudan başlık + (opsiyonel) yıl ile dene
        url = f"http://www.omdbapi.com/?t={requests.utils.quote(name)}&apikey={api_key}"
        if year:
            url += f"&y={year}"
        resp = requests.get(url, timeout=8)
        data = resp.json()
        poster = data.get("Poster")
        if poster and poster != "N/A":
            return poster

        # 2) Arama ile en yakın eşleşmeyi bul (s=)
        s_url = f"http://www.omdbapi.com/?s={requests.utils.quote(name)}&apikey={api_key}"
        s_resp = requests.get(s_url, timeout=8)
        s_data = s_resp.json()
        results = s_data.get("Search") or []
        if results:
            # Yıla en yakın olanı seç
            best = results[0]
            if year:
                for r in results:
                    try:
                        if int(r.get("Year", "0")[:4]) == year:
                            best = r
                            break
                    except Exception:
                        pass
            imdb_id = best.get("imdbID")
            if imdb_id:
                by_id = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
                d2 = requests.get(by_id, timeout=8).json()
                poster2 = d2.get("Poster")
                if poster2 and poster2 != "N/A":
                    return poster2
    except Exception:
        pass
    return "https://via.placeholder.com/120x180?text=No+Poster"


def get_movie_poster(title: str) -> str:
    api_key = _effective_omdb_key()
    name, year = _parse_title_year(title)
    if not api_key:
        return "https://via.placeholder.com/120x180?text=No+Poster"
    return _fetch_poster_from_omdb(name, year, api_key)


# -------- 5. Streamlit Arayüz --------
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("🎬 Movie Recommender")

with st.sidebar:
    st.markdown("## Ayarlar")
    st.markdown(
        f"Veri boyutu: {len(movies)} film • {len(ratings)} puan"
    )
    if HAVE_SURPRISE:
        st.success("Surprise SVD kullanılabilir.")
    else:
        st.info("Surprise bulunamadı. Item-based CF kullanılacak.")
    st.divider()
    st.markdown("### OMDb API Anahtarı")
    st.text_input(
        "Poster için OMDb API Key",
        value=st.session_state.get("omdb_api_key", ""),
        key="omdb_api_key",
        help="https://www.omdbapi.com/ üzerinden ücretsiz key alabilirsiniz.",
    )

option = st.selectbox("Bir öneri yöntemi seç:", ["İçerik Tabanlı", "Kullanıcı Tabanlı"], index=0)

if option == "İçerik Tabanlı":
    # Kolay arama için bir arama kutusu
    query = st.text_input("Film ara:", "")
    title_list = movies["title"].unique().tolist()
    if query:
        filtered = [t for t in title_list if query.lower() in t.lower()]
    else:
        filtered = title_list
    selected_movie = st.selectbox("Film seçiniz:", filtered)
    top_n = st.slider("Kaç öneri gösterilsin?", 3, 20, 10)
    if st.button("Önerileri Getir", type="primary"):
        recs = content_based_recommendations(selected_movie, top_n=top_n)
        if not recs:
            st.warning("Öneri bulunamadı.")
        else:
            # Seçilen film için kapak görseli ve etiketler
            st.subheader("Seçilen Film")
            left, right = st.columns([1, 3])
            with left:
                st.image(get_movie_poster(selected_movie), width=200)
            with right:
                st.markdown(f"### {selected_movie}")
                genres = movies.loc[movies["title"] == selected_movie, "genres"].iloc[0]
                chips = " ".join([f"`{g}`" for g in str(genres).split("|") if g])
                st.markdown(chips)
            st.divider()

            st.subheader("Önerilen Filmler")
            cols = st.columns(min(5, len(recs)))
            for i, film in enumerate(recs):
                with cols[i % len(cols)]:
                    st.image(get_movie_poster(film), width=150)
                    st.caption(film)
            # İndirilebilir liste
            st.download_button(
                "Önerileri CSV olarak indir",
                data=pd.DataFrame({"title": recs}).to_csv(index=False).encode("utf-8"),
                file_name="oneriler_iceri_k.csv",
                mime="text/csv",
            )

else:  # Kullanıcı Tabanlı
    existing_users = sorted(ratings["userId"].unique().tolist())
    if existing_users:
        default_user = existing_users[0]
    else:
        default_user = 1
    selected_user = st.selectbox("Kullanıcı ID seçiniz:", existing_users or [1], index=0)
    top_n = st.slider("Kaç öneri gösterilsin?", 3, 20, 10, key="cf_n")
    if st.button("Önerileri Getir", type="primary", key="cf_btn"):
        recs = collaborative_filtering_recommendations(int(selected_user), top_n=top_n)
        if not recs:
            st.warning("Öneri bulunamadı (kullanıcının oylaması yok olabilir).")
        else:
            st.subheader("Önerilen Filmler")
            cols = st.columns(min(5, len(recs)))
            for i, film in enumerate(recs):
                with cols[i % len(cols)]:
                    st.image(get_movie_poster(film), width=150)
                    st.caption(film)
            st.download_button(
                "Önerileri CSV olarak indir",
                data=pd.DataFrame({"title": recs}).to_csv(index=False).encode("utf-8"),
                file_name="oneriler_kullanici_k.csv",
                mime="text/csv",
            )

