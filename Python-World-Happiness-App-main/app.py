
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import plotly.figure_factory as ff

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="🌍 Dünya Mutluluk Analiz Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🌍"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #4ECDC4;
        margin: 10px 0;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    
    /* Select box styling - yazı rengini düzelt */
    .stSelectbox > div > div > div {
        background-color: white;
        color: #262730 !important;
    }
    
    .stSelectbox label {
        color: #262730 !important;
        font-weight: bold;
    }
    
    /* Multiselect styling */
    .stMultiSelect > div > div > div {
        background-color: white;
        color: #262730 !important;
    }
    
    .stMultiSelect label {
        color: #262730 !important;
        font-weight: bold;
    }
    
    /* Radio button styling */
    .stRadio > div {
        color: #262730 !important;
    }
    
    .stRadio label {
        color: #262730 !important;
        font-weight: bold;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background-color: white;
        color: #262730 !important;
    }
    
    .stTextInput label {
        color: #262730 !important;
        font-weight: bold;
    }
    
    /* Slider styling */
    .stSlider label {
        color: #262730 !important;
        font-weight: bold;
    }
    
    /* Dataframe index hiding */
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
        display: none;
    }
    
    .dataframe tbody tr th {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🌍 Dünya Mutluluk Analiz Dashboard</h1>', unsafe_allow_html=True)
st.markdown("---")

@st.cache_data
def load_data():
    """Veri yükleme ve ön işleme"""
    df = pd.read_csv("world_happiness.csv")
    
    # Eksik değerleri kontrol et ve doldur
    df = df.fillna(df.mean(numeric_only=True))
    
    # Yeni sütunlar ekle
    df['Total_Index'] = (df['GDP per Capita'] + df['Health (Life Expectancy)'] + 
                        df['Freedom'] + df['Trust (Government Corruption)'] + df['Generosity']) / 5
    
    # Kategorik sütun ekle
    df['Happiness_Category'] = pd.cut(df['Happiness Score'], 
                                     bins=[0, 3, 5, 7, 10], 
                                     labels=['Düşük', 'Orta', 'Yüksek', 'Çok Yüksek'])
    
    return df

def get_country_stats(df, country):
    """Ülke istatistikleri"""
    country_data = df[df['Country'] == country].sort_values('Year')
    if country_data.empty:
        return None
    
    stats = {
        'avg_happiness': country_data['Happiness Score'].mean(),
        'trend': 'Artış' if country_data['Happiness Score'].iloc[-1] > country_data['Happiness Score'].iloc[0] else 'Azalış',
        'years_available': len(country_data),
        'best_year': country_data.loc[country_data['Happiness Score'].idxmax(), 'Year'],
        'worst_year': country_data.loc[country_data['Happiness Score'].idxmin(), 'Year'],
    }
    return stats

def create_correlation_heatmap(df_year):
    """Korelasyon ısı haritası oluştur"""
    numeric_cols = ['Happiness Score', 'GDP per Capita', 'Health (Life Expectancy)', 
                   'Freedom', 'Trust (Government Corruption)', 'Generosity']
    corr_matrix = df_year[numeric_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0,
        text=corr_matrix.round(2).values,
        texttemplate="%{text}",
        textfont={"size": 10},
        hoverongaps=False
    ))
    
    fig.update_layout(
        title="Mutluluk Faktörleri Arasındaki Korelasyon",
        xaxis_title="",
        yaxis_title="",
        height=500
    )
    return fig

def create_radar_chart(df_year, countries):
    """Radar grafiği oluştur"""
    categories = ['GDP per Capita', 'Health (Life Expectancy)', 'Freedom', 
                 'Trust (Government Corruption)', 'Generosity']
    
    fig = go.Figure()
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
    
    for i, country in enumerate(countries):
        country_data = df_year[df_year['Country'] == country]
        if not country_data.empty:
            values = country_data[categories].iloc[0].values.tolist()
            values += values[:1]  # İlk değeri sona ekle (kapalı şekil için)
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                fill='toself',
                name=country,
                line_color=colors[i % len(colors)]
            ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 2])
        ),
        showlegend=True,
        title="Seçili Ülkeler - Mutluluk Faktörleri Karşılaştırması"
    )
    return fig

# Veri yükleme
df = load_data()

# Sidebar - Kontrol Paneli
st.sidebar.markdown("## 🎛️ Kontrol Paneli")

# Yıl seçimi
year_options = sorted(df['Year'].unique(), reverse=True)
year = st.sidebar.selectbox("📅 Yıl Seç", year_options, index=0)
df_year = df[df['Year'] == year]

# Analiz türü seçimi
analysis_type = st.sidebar.radio(
    "📊 Analiz Türü",
    ["Genel Bakış", "Ülke Karşılaştırma", "Trend Analizi", "Korelasyon Analizi", "Detaylı İstatistikler"]
)

# Gösterim seçenekleri
if analysis_type == "Genel Bakış":
    show_option = st.sidebar.radio(
        "🏆 Gösterim Seçeneği",
        ["En Mutlu 10 Ülke", "En Mutsuz 10 Ülke", "Tüm Ülkeler", "Bölgesel Analiz"]
    )

# Ülke arama
search_country = st.sidebar.text_input("🔍 Ülke Ara", placeholder="Ülke adı girin...")

# Gelişmiş filtreler
st.sidebar.markdown("### 🎚️ Gelişmiş Filtreler")
happiness_range = st.sidebar.slider(
    "Mutluluk Skoru Aralığı",
    float(df_year['Happiness Score'].min()),
    float(df_year['Happiness Score'].max()),
    (float(df_year['Happiness Score'].min()), float(df_year['Happiness Score'].max())),
    step=0.1
)

gdp_range = st.sidebar.slider(
    "GDP Aralığı",
    float(df_year['GDP per Capita'].min()),
    float(df_year['GDP per Capita'].max()),
    (float(df_year['GDP per Capita'].min()), float(df_year['GDP per Capita'].max())),
    step=0.01
)

# Filtreleme
df_filtered = df_year[
    (df_year['Happiness Score'] >= happiness_range[0]) & 
    (df_year['Happiness Score'] <= happiness_range[1]) &
    (df_year['GDP per Capita'] >= gdp_range[0]) & 
    (df_year['GDP per Capita'] <= gdp_range[1])
]

if search_country:
    df_filtered = df_filtered[df_filtered['Country'].str.contains(search_country, case=False, na=False)]

# Ana İçerik
if analysis_type == "Genel Bakış":
    # Özet İstatistikler
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_happiness = df_filtered['Happiness Score'].mean()
        st.metric(
            label="📊 Ortalama Mutluluk", 
            value=f"{avg_happiness:.2f}",
            delta=f"{avg_happiness - df['Happiness Score'].mean():.2f}"
        )
    
    with col2:
        st.metric(
            label="🌍 Toplam Ülke", 
            value=len(df_filtered),
            delta=f"{len(df_filtered) - len(df_year)}"
        )
    
    with col3:
        max_happiness = df_filtered['Happiness Score'].max()
        happiest_country = df_filtered.loc[df_filtered['Happiness Score'].idxmax(), 'Country']
        st.metric(
            label="🏆 En Yüksek Skor", 
            value=f"{max_happiness:.2f}",
            delta=f"({happiest_country})"
        )
    
    with col4:
        min_happiness = df_filtered['Happiness Score'].min()
        saddest_country = df_filtered.loc[df_filtered['Happiness Score'].idxmin(), 'Country']
        st.metric(
            label="😔 En Düşük Skor", 
            value=f"{min_happiness:.2f}",
            delta=f"({saddest_country})"
        )
    
    st.markdown("---")
    
    # Veri gösterimi
    if show_option == "En Mutlu 10 Ülke":
        display_data = df_filtered.sort_values(by="Happiness Score", ascending=False).head(10)
        st.subheader("🏆 En Mutlu 10 Ülke")
    elif show_option == "En Mutsuz 10 Ülke":
        display_data = df_filtered.sort_values(by="Happiness Score", ascending=True).head(10)
        st.subheader("😔 En Mutsuz 10 Ülke")
    elif show_option == "Bölgesel Analiz":
        # Basit bölgesel gruplandırma (ülke isimlerine göre)
        display_data = df_filtered.sort_values(by="Happiness Score", ascending=False)
        st.subheader("🌎 Bölgesel Analiz")
        
        # Kontinentlere göre basit gruplandırma
        europe_keywords = ['Finland', 'Denmark', 'Switzerland', 'Iceland', 'Norway', 'Netherlands', 'Sweden', 'Austria', 'Luxembourg', 'Germany', 'United Kingdom', 'France', 'Belgium', 'Ireland', 'Italy', 'Spain', 'Portugal', 'Greece', 'Poland']
        asia_keywords = ['Japan', 'South Korea', 'China', 'India', 'Indonesia', 'Vietnam']
        americas_keywords = ['Canada', 'United States', 'Brazil', 'Argentina', 'Mexico']
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            europe_data = display_data[display_data['Country'].isin(europe_keywords)]
            st.markdown("### 🇪🇺 Avrupa")
            if not europe_data.empty:
                st.metric("Ortalama Mutluluk", f"{europe_data['Happiness Score'].mean():.2f}")
                st.write(f"Ülke Sayısı: {len(europe_data)}")
        
        with col2:
            asia_data = display_data[display_data['Country'].isin(asia_keywords)]
            st.markdown("### 🌏 Asya")
            if not asia_data.empty:
                st.metric("Ortalama Mutluluk", f"{asia_data['Happiness Score'].mean():.2f}")
                st.write(f"Ülke Sayısı: {len(asia_data)}")
        
        with col3:
            americas_data = display_data[display_data['Country'].isin(americas_keywords)]
            st.markdown("### 🌎 Amerika")
            if not americas_data.empty:
                st.metric("Ortalama Mutluluk", f"{americas_data['Happiness Score'].mean():.2f}")
                st.write(f"Ülke Sayısı: {len(americas_data)}")
    else:
        display_data = df_filtered.sort_values(by="Happiness Score", ascending=False)
        st.subheader(f"🌍 Tüm Ülkeler ({len(display_data)} ülke)")
    
    # Tablo gösterimi
    if show_option != "Bölgesel Analiz" and not display_data.empty:
        # Index'i sıfırla ve sıralama numarası ekle
        display_data_clean = display_data.reset_index(drop=True)
        display_data_clean.insert(0, 'Sıra', range(1, len(display_data_clean) + 1))
        
        if len(display_data_clean) > 10:
            st.dataframe(
                display_data_clean[['Sıra', 'Country', 'Happiness Score', 'GDP per Capita', 'Health (Life Expectancy)', 'Freedom', 'Total_Index']].round(3),
                height=400,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Sıra": st.column_config.NumberColumn(
                        "Sıra",
                        help="Mutluluk skoruna göre sıralama",
                        width="small"
                    ),
                    "Country": st.column_config.TextColumn(
                        "Ülke",
                        width="medium"
                    ),
                    "Happiness Score": st.column_config.NumberColumn(
                        "Mutluluk Skoru",
                        format="%.2f",
                        width="medium"
                    ),
                    "GDP per Capita": st.column_config.NumberColumn(
                        "GSYİH/Kişi",
                        format="%.2f",
                        width="medium"
                    ),
                    "Health (Life Expectancy)": st.column_config.NumberColumn(
                        "Sağlık",
                        format="%.2f",
                        width="medium"
                    ),
                    "Freedom": st.column_config.NumberColumn(
                        "Özgürlük",
                        format="%.2f",
                        width="medium"
                    ),
                    "Total_Index": st.column_config.NumberColumn(
                        "Toplam İndeks",
                        format="%.3f",
                        width="medium"
                    )
                }
            )
        else:
            st.dataframe(
                display_data_clean[['Sıra', 'Country', 'Happiness Score', 'GDP per Capita', 'Health (Life Expectancy)', 'Freedom']].round(3),
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Sıra": st.column_config.NumberColumn(
                        "Sıra",
                        help="Mutluluk skoruna göre sıralama",
                        width="small"
                    ),
                    "Country": st.column_config.TextColumn(
                        "Ülke",
                        width="medium"
                    ),
                    "Happiness Score": st.column_config.NumberColumn(
                        "Mutluluk Skoru",
                        format="%.2f",
                        width="medium"
                    ),
                    "GDP per Capita": st.column_config.NumberColumn(
                        "GSYİH/Kişi",
                        format="%.2f",
                        width="medium"
                    ),
                    "Health (Life Expectancy)": st.column_config.NumberColumn(
                        "Sağlık",
                        format="%.2f",
                        width="medium"
                    ),
                    "Freedom": st.column_config.NumberColumn(
                        "Özgürlük",
                        format="%.2f",
                        width="medium"
                    )
                }
            )
        
        # Grafik gösterimi
        if len(display_data) <= 20:  # Çok fazla ülke varsa grafiği sınırla
            chart_data = display_data
        else:
            chart_data = display_data.head(20)
            st.info("📊 Grafik görünümü için ilk 20 ülke gösteriliyor.")
        
        fig = px.bar(
            chart_data, 
            x="Country", 
            y="Happiness Score", 
            color="Happiness Score",
            color_continuous_scale="Viridis",
            title=f"{show_option} - Mutluluk Skorları",
            labels={'Happiness Score': 'Mutluluk Skoru'}
        )
elif analysis_type == "Ülke Karşılaştırma":
    st.subheader("🔍 Ülke Karşılaştırma Analizi")
    
    # Ülke seçimi
    countries_list = sorted(df['Country'].unique())
    selected_countries = st.multiselect(
        "Karşılaştırmak istediğiniz ülkeleri seçin (maksimum 5):",
        countries_list,
        default=countries_list[:3] if len(countries_list) >= 3 else countries_list,
        max_selections=5
    )
    
    if len(selected_countries) >= 2:
        comparison_data = df_filtered[df_filtered['Country'].isin(selected_countries)]
        
        # Karşılaştırma tablosu
        comparison_summary = comparison_data.groupby('Country').agg({
            'Happiness Score': 'mean',
            'GDP per Capita': 'mean',
            'Health (Life Expectancy)': 'mean',
            'Freedom': 'mean',
            'Trust (Government Corruption)': 'mean',
            'Generosity': 'mean'
        }).round(3).reset_index()
        
        # Mutluluk skoruna göre sırala ve sıra numarası ekle
        comparison_summary = comparison_summary.sort_values('Happiness Score', ascending=False).reset_index(drop=True)
        comparison_summary.insert(0, 'Sıra', range(1, len(comparison_summary) + 1))
        
        st.dataframe(
            comparison_summary, 
            use_container_width=True, 
            hide_index=True,
            column_config={
                "Sıra": st.column_config.NumberColumn(
                    "Sıra",
                    help="Mutluluk skoruna göre sıralama",
                    width="small"
                ),
                "Country": st.column_config.TextColumn(
                    "Ülke",
                    width="medium"
                ),
                "Happiness Score": st.column_config.NumberColumn(
                    "Mutluluk Skoru",
                    format="%.3f",
                    width="medium"
                ),
                "GDP per Capita": st.column_config.NumberColumn(
                    "GSYİH/Kişi",
                    format="%.3f",
                    width="medium"
                ),
                "Health (Life Expectancy)": st.column_config.NumberColumn(
                    "Sağlık",
                    format="%.3f",
                    width="medium"
                ),
                "Freedom": st.column_config.NumberColumn(
                    "Özgürlük",
                    format="%.3f",
                    width="medium"
                ),
                "Trust (Government Corruption)": st.column_config.NumberColumn(
                    "Güven",
                    format="%.3f",
                    width="medium"
                ),
                "Generosity": st.column_config.NumberColumn(
                    "Cömertlik",
                    format="%.3f",
                    width="medium"
                )
            }
        )
        
        # Radar grafiği
        if len(selected_countries) <= 5:
            radar_fig = create_radar_chart(df_filtered, selected_countries)
            st.plotly_chart(radar_fig, use_container_width=True)
        
        # Paralel koordinat grafiği
        cols_for_parallel = ['Happiness Score', 'GDP per Capita', 'Health (Life Expectancy)', 'Freedom']
        fig_parallel = px.parallel_coordinates(
            comparison_data,
            color='Happiness Score',
            dimensions=cols_for_parallel,
            color_continuous_scale='Viridis',
            title="Ülkeler Arası Paralel Koordinat Analizi"
        )
        st.plotly_chart(fig_parallel, use_container_width=True)
    
    else:
        st.warning("Karşılaştırma için en az 2 ülke seçin.")

elif analysis_type == "Trend Analizi":
    st.subheader("📈 Trend Analizi")
    
    # Ülke seçimi
    trend_countries = st.multiselect(
        "Trend analizi için ülke seçin:",
        sorted(df['Country'].unique()),
        default=['Finland', 'Denmark', 'Switzerland'] if 'Finland' in df['Country'].values else df['Country'].unique()[:3]
    )
    
    if trend_countries:
        trend_data = df[df['Country'].isin(trend_countries)]
        
        # Zaman serisi grafiği
        fig_trend = px.line(
            trend_data,
            x='Year',
            y='Happiness Score',
            color='Country',
            title='Yıllar İçinde Mutluluk Skoru Değişimi',
            markers=True
        )
        fig_trend.update_layout(height=500)
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Trend istatistikleri
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Trend İstatistikleri")
            for country in trend_countries:
                country_stats = get_country_stats(df, country)
                if country_stats:
                    st.markdown(f"**{country}:**")
                    st.write(f"- Ortalama: {country_stats['avg_happiness']:.2f}")
                    st.write(f"- Trend: {country_stats['trend']}")
                    st.write(f"- En iyi yıl: {country_stats['best_year']}")
                    st.write("---")
        
        with col2:
            # Değişim grafiği
            change_data = []
            for country in trend_countries:
                country_data = trend_data[trend_data['Country'] == country].sort_values('Year')
                if len(country_data) >= 2:
                    first_score = country_data['Happiness Score'].iloc[0]
                    last_score = country_data['Happiness Score'].iloc[-1]
                    change = last_score - first_score
                    change_data.append({'Country': country, 'Change': change})
            
            if change_data:
                change_df = pd.DataFrame(change_data)
                fig_change = px.bar(
                    change_df,
                    x='Country',
                    y='Change',
                    color='Change',
                    color_continuous_scale='RdYlGn',
                    title='Toplam Mutluluk Değişimi'
                )
                st.plotly_chart(fig_change, use_container_width=True)

elif analysis_type == "Korelasyon Analizi":
    st.subheader("🔗 Korelasyon Analizi")
    
    # Korelasyon ısı haritası
    corr_fig = create_correlation_heatmap(df_filtered)
    st.plotly_chart(corr_fig, use_container_width=True)
    
    # Scatter plot matrisi
    numeric_cols = ['Happiness Score', 'GDP per Capita', 'Health (Life Expectancy)', 'Freedom']
    
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("X Ekseni", numeric_cols, index=1)
    with col2:
        y_axis = st.selectbox("Y Ekseni", numeric_cols, index=0)
    
    fig_scatter = px.scatter(
        df_filtered,
        x=x_axis,
        y=y_axis,
        color='Happiness Score',
        size='Total_Index',
        hover_name='Country',
        color_continuous_scale='Viridis',
        title=f'{x_axis} vs {y_axis}'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Korelasyon yorumu
    correlation = df_filtered[x_axis].corr(df_filtered[y_axis])
    if abs(correlation) > 0.7:
        strength = "Güçlü"
    elif abs(correlation) > 0.5:
        strength = "Orta"
    else:
        strength = "Zayıf"
    
    direction = "Pozitif" if correlation > 0 else "Negatif"
    st.info(f"**Korelasyon Analizi:** {x_axis} ve {y_axis} arasında {strength.lower()} {direction.lower()} korelasyon ({correlation:.3f})")

elif analysis_type == "Detaylı İstatistikler":
    st.subheader("📈 Detaylı İstatistikler")
    
    # Genel istatistikler
    st.markdown("### 📊 Genel İstatistikler")
    stats_df = df_filtered.describe().round(3).reset_index()
    st.dataframe(stats_df, use_container_width=True, hide_index=True)
    
    # Dağılım grafikleri
    col1, col2 = st.columns(2)
    
    with col1:
        # Histogram
        fig_hist = px.histogram(
            df_filtered,
            x='Happiness Score',
            nbins=20,
            title='Mutluluk Skoru Dağılımı',
            labels={'count': 'Ülke Sayısı'}
        )
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Box plot
        fig_box = px.box(
            df_filtered,
            y='Happiness Score',
            title='Mutluluk Skoru Box Plot'
        )
        st.plotly_chart(fig_box, use_container_width=True)
    
    # Kategori analizi
    if 'Happiness_Category' in df_filtered.columns:
        category_counts = df_filtered['Happiness_Category'].value_counts()
        fig_pie = px.pie(
            values=category_counts.values,
            names=category_counts.index,
            title='Mutluluk Kategorisi Dağılımı'
        )
        st.plotly_chart(fig_pie, use_container_width=True)

# Dünya Haritası (her analiz türünde göster)
if len(df_filtered) > 1:  # En az 2 ülke varsa haritayı göster
    st.markdown("---")
    st.subheader("🗺️ Dünya Mutluluk Haritası")
    
    # Harita türü seçimi
    map_col1, map_col2 = st.columns([3, 1])
    
    with map_col2:
        map_metric = st.selectbox(
            "Harita Metriği:",
            ['Happiness Score', 'GDP per Capita', 'Health (Life Expectancy)', 'Freedom', 'Total_Index']
        )
    
    # İnteraktif dünya haritası
    fig_map = px.choropleth(
        df_filtered,
        locations="Country",
        locationmode="country names",
        color=map_metric,
        hover_name="Country",
        hover_data={
            'Happiness Score': ':.2f',
            'GDP per Capita': ':.2f',
            'Health (Life Expectancy)': ':.2f',
            'Freedom': ':.2f'
        },
        color_continuous_scale="Viridis",
        title=f"{year} - {map_metric} Dünya Haritası"
    )
    
    fig_map.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth'
        ),
        height=600
    )
    
    st.plotly_chart(fig_map, use_container_width=True)

# Sidebar - Ek Bilgiler
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ Veri Hakkında")
st.sidebar.info(f"""
**Veri Seti Özeti:**
- 📅 Yıl Aralığı: {df['Year'].min()} - {df['Year'].max()}
- 🌍 Toplam Ülke: {df['Country'].nunique()}
- 📊 Veri Noktası: {len(df):,}
- 🏆 En Yüksek Skor: {df['Happiness Score'].max():.2f}
- 😔 En Düşük Skor: {df['Happiness Score'].min():.2f}
""")

# Uygulamayı kim yaptı bilgisi
st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Geliştirici")
st.sidebar.markdown("""
**Dünya Mutluluk Dashboard v2.0**  
🚀 Streamlit & Plotly ile geliştirildi  
� infoenessen@gmail.com  
🐱 https://github.com/EnesSen071198
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <h4>🌍 Dünya Mutluluk Analiz </h4>
    <p>Mutluluk verilerini keşfedin, trendleri analiz edin ve ülkeleri karşılaştırın.</p>
    <p><em>Veri kaynağı: World Happiness Report | Geliştirme: Streamlit & Plotly</em></p>
</div>
""", unsafe_allow_html=True)
