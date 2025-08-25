# 🌍 World Happiness Analysis Dashboard

This project is a professional web application that allows you to analyze World Happiness Report data through an interactive dashboard.

## 🚀 Features

### 📊 Analysis Types
- **Overview**: Happiest/unhappiest countries, regional analysis
- **Country Comparison**: Radar charts and parallel coordinates analysis
- **Trend Analysis**: Time series charts and trend statistics
- **Correlation Analysis**: Heatmaps and scatter plot analysis
- **Detailed Statistics**: Histograms, box plots, and category analysis

### 🎛️ Interactive Features
- ✅ Year-based filtering
- ✅ Country search and selection
- ✅ Advanced filters (happiness score, GDP range)
- ✅ Multi-country comparison
- ✅ Interactive map views
- ✅ Dynamic chart type selection

### 📈 Visualizations
- 🗺️ Interactive world map
- 📊 Bar charts and histograms
- 📈 Time series trends
- 🎯 Radar charts
- 🔗 Correlation heatmaps
- 📉 Box plots and scatter plots

--

# 🌍 Dünya Mutluluk Analiz Dashboard

Bu proje, Dünya Mutluluk Raporu verilerini interaktif bir dashboard ile analiz etmenizi sağlayan profesyonel bir web uygulamasıdır.

## 🚀 Özellikler

### 📊 Analiz Türleri
- **Genel Bakış**: En mutlu/mutsuz ülkeler, bölgesel analiz
- **Ülke Karşılaştırma**: Radar grafikleri ve paralel koordinat analizi
- **Trend Analizi**: Zaman serisi grafikleri ve trend istatistikleri
- **Korelasyon Analizi**: Isı haritaları ve scatter plot analizi
- **Detaylı İstatistikler**: Histogram, box plot ve kategori analizleri

### 🎛️ İnteraktif Özellikler
- ✅ Yıl bazında filtreleme
- ✅ Ülke arama ve seçimi
- ✅ Gelişmiş filtreler (mutluluk skoru, GDP aralığı)
- ✅ Çoklu ülke karşılaştırma
- ✅ İnteraktif harita görünümleri
- ✅ Dinamik grafik türü seçimi

### 📈 Görselleştirmeler
- 🗺️ İnteraktif dünya haritası
- 📊 Bar grafikleri ve histogramlar
- 📈 Zaman serisi trendleri
- 🎯 Radar grafikleri
- 🔗 Korelasyon ısı haritaları
- 📉 Box plot ve dağılım grafikleri

## 🛠️ Kurulum

### Gereksinimler
```bash
pip install -r requirements.txt
```

### Çalıştırma
```bash
streamlit run app.py
```

## 📁 Proje Yapısı
```
world_happiness_app/
│
├── app.py                 # Ana uygulama dosyası
├── world_happiness.csv    # Veri dosyası
├── requirements.txt       # Python paket gereksinimleri
└── README.md             # Bu dosya
```

## 📊 Veri Hakkında

Veri seti aşağıdaki sütunları içerir:
- **Country**: Ülke adı
- **Year**: Yıl (2015-2024)
- **Happiness Score**: Mutluluk skoru (0-10 arası)
- **GDP per Capita**: Kişi başına GSYİH
- **Health (Life Expectancy)**: Sağlık/Yaşam beklentisi
- **Freedom**: Özgürlük indeksi
- **Trust (Government Corruption)**: Güven/Yolsuzluk indeksi
- **Generosity**: Cömertlik indeksi

## 🎯 Kullanım

1. **Yıl Seçimi**: Sol panelden analiz etmek istediğiniz yılı seçin
2. **Analiz Türü**: Yapmak istediğiniz analiz türünü seçin
3. **Filtreler**: Gelişmiş filtreleri kullanarak veriyi özelleştirin
4. **Ülke Seçimi**: Karşılaştırma ve trend analizi için ülkeleri seçin
5. **İnteraksiyon**: Grafikleri yakınlaştırın, hover yapın ve keşfedin

## 🔧 Teknik Detaylar

- **Framework**: Streamlit
- **Veri İşleme**: Pandas
- **Görselleştirme**: Plotly Express & Plotly Graph Objects
- **Styling**: Custom CSS
- **Caching**: Streamlit cache_data dekoratörü

## 📈 Performans Optimizasyonu

- Veri cache'leme ile hızlı yükleme
- Dinamik filtreleme
- Responsive tasarım
- Optimize edilmiş grafik rendering

## 🚀 Gelişmiş Özellikler

- **Radar Grafikleri**: Çoklu faktör karşılaştırması
- **Paralel Koordinat**: Çok boyutlu veri analizi
- **İnteraktif Harita**: Coğrafi veri görselleştirme
- **Trend Analizi**: Zaman serisi analizi
- **Korelasyon Matrisi**: İstatistiksel ilişkiler
- **Kategorisel Analiz**: Mutluluk seviyesi gruplandırması

## 💡 İpuçları

- Karşılaştırma için en fazla 5 ülke seçin
- Trend analizi için birden fazla yılın verisi bulunan ülkeleri tercih edin
- Filtreleri kullanarak belirli aralıklardaki ülkeleri analiz edin
- Harita üzerinde hover yaparak detaylı bilgileri görün

## 🐛 Sorun Giderme

**Veri yüklenmiyor**: `world_happiness.csv` dosyasının aynı klasörde olduğundan emin olun
**Grafik görünmüyor**: İnternet bağlantınızı kontrol edin (Plotly CDN gerektirir)
**Yavaş çalışıyor**: Filtreleri kullanarak veri boyutunu küçültün

---
**Geliştirici**: Dashboard v2.0 | **Teknoloji**: Streamlit + Plotly | **Veri**: World Happiness Report
