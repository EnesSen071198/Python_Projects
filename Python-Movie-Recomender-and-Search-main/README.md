# Movie Recommender

A simple Streamlit app. Provides content-based (genres) and user-based recommendations (SVD via Surprise if available, otherwise item-based fallback).

## Hızlı Başlangıç

1) Virtual environment (recommended):

```cmd
py -m venv .venv
.venv\Scripts\activate
```

2) Dependencies:

```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3) Optional (Surprise):
- On Windows, C++ Build Tools are required, or use Python 3.10.
- Then run `pip install scikit-surprise`.

4) OMDb poster API key:
- Get a free key and set it as an environment variable:
```cmd
set OMDB_API_KEY=YOUR_KEY
```

5) Run:

```cmd
streamlit run movie_recommender.py
```

## Data
- If `movies.csv` and `ratings.csv` exist, the app will use them.
- Otherwise, a small sample dataset is loaded automatically.
