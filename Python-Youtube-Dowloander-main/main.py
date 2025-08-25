import yt_dlp

# Video URL'si
url = input("Enter video URL: ")

# İndirilecek dosyanın kaydedileceği yol ve dosya adı
output_path = "C:/Users/eness/PycharmProjects/%(title)s.%(ext)s"  # Kaydetmek istediğiniz yer

# İndirme işlemi
ydl_opts = {
    'outtmpl': output_path  # Çıktı yolu burada belirtiliyor
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Video indiriliyor
    print("Video başarıyla indirildi ve kaydedildi!")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
