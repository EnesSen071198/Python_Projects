
# Python Face Detection System

This project performs real-time human face detection using OpenCV. Additionally, it includes features like glasses detection, age and gender prediction (if model files are available), and audio alerts when the number of faces changes.

## Features
- Real-time face detection
- Display the current number of faces on screen
- Audio alert when the number of faces changes
- Glasses detection
- Age and gender prediction (if OpenCV model files are available)

## Requirements
- Python 3.11+
- OpenCV
- numpy
- pyttsx3

--

Bu proje, OpenCV kullanarak gerçek zamanlı insan yüzü tespiti yapar. Ek olarak, gözlük tespiti, yaş ve cinsiyet tahmini (model dosyaları varsa) ve yüz sayısı değiştiğinde sesli uyarı özellikleri içerir.

## Özellikler
- Gerçek zamanlı yüz tespiti
- Ekranda anlık yüz sayısı
- Yüz sayısı değiştiğinde sesli uyarı
- Gözlük tespiti
- Yaş ve cinsiyet tahmini (OpenCV model dosyaları varsa)

## Gereksinimler
- Python 3.11+
- OpenCV
- numpy
- pyttsx3

## Kurulum
1. Gerekli paketleri yükleyin:
   ```bash
   pip install opencv-python numpy pyttsx3
   ```
2. (İsteğe bağlı) Yaş ve cinsiyet tahmini için OpenCV model dosyalarını `face_detect.py` dosyasındaki ilgili yerlere ekleyin.

## Kullanım
1. Proje klasöründe terminal açın.
2. Aşağıdaki komutu çalıştırın:
   ```cmd
   C:/Users/Enes/Desktop/Python-Face-Detected/.venv/Scripts/python.exe face_detect.py
   ```
3. Kameradan gelen görüntüde yüzler, gözlük, yaş ve cinsiyet bilgisi ekranda gösterilir.
4. Çıkmak için 'q' tuşuna basın.

## Notlar
- Yaş ve cinsiyet tahmini için model dosyaları yoksa, ekranda sadece "Human" yazısı gösterilir.
- Maske tespiti için ek model dosyası eklenebilir.

## Geliştirme
Ek özellikler veya hata bildirimi için bana ulaşabilirsiniz.
