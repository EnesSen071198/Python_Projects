# -*- coding: utf-8 -*-

import random

def fikir_jeneratoru():
    # Fikirleri içeren liste
    fikirler = [
        "Yeni bir dil öğren.",
        "Kitap yazmaya başla.",
        "Bahçede bir sebze bahçesi oluştur.",
        "Fotoğrafçılığa başla.",
        "Bir podcast başlat.",
        "Farklı bir yemek tarifi dene.",
        "Bir sanat projesi oluştur.",
        "Bir müzik aleti çalmayı öğren.",
        "Yürüyüş yap ve doğayı keşfet.",
        "Yoga veya meditasyon yapmaya başla.",
        "Kodlamayı öğren ve küçük bir proje geliştir.",
        "Yeni bir spor dalı dene.",
        "Hedeflerin için bir vizyon panosu oluştur.",
        "Bir gönüllü projeye katıl.",
        "Bahçende çiçek yetiştir.",
        "Evin için DIY (Do It Yourself) projeleri yap.",
        "Yabancı bir mutfaktan yemekler dene.",
        "Bir günlük veya blog tut.",
        "Bütçeleme ve finansal planlama yap.",
        "Kendi web siteni veya portföyünü oluştur.",
        "Doğa gezisine çık.",
        "Bir arkadaşına veya aile üyesine el yapımı hediye yap.",
        "Bilinmeyen bir konuda araştırma yap ve öğren.",
        "Sanal turlar ve müze gezileri yap.",
        "Kendi kitabını yaz ve yayımla.",
        "Arkeolojik veya tarihsel yerleri ziyaret et.",
        "Çevrimiçi kurslara katıl ve yeni beceriler öğren.",
        "Mikro hobi bahçecilik yap."
    ]

    # Rastgele bir fikir seç
    rastgele_fikir = random.choice(fikirler)
    print(f"Bugün denemen gereken şey: {rastgele_fikir}")

# Örnek kullanım, kullanıcı girdisi beklemeden çalışacak
for _ in range(5):  # 5 adet fikir üretmek için
    fikir_jeneratoru()
