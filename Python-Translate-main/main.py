from translate import Translator

def ceviri_yap(metin, hedef_dil):
    translator = Translator(to_lang=hedef_dil)
    sonuc = translator.translate(metin)
    return sonuc

# Kullanıcıdan girdi alarak çeviri yapma
while True:
    metin = input("Çevirmek istediğiniz metni girin ('q' ile çıkış yapabilirsiniz): ")
    if metin.lower() == 'q':
        print("Çeviri Uygulaması kapanıyor...")
        break
    hedef_dil = input("Hedef dili girin (örneğin 'en' İngilizce için, 'tr' Türkçe için): ")
    ceviri_sonucu = ceviri_yap(metin, hedef_dil)
    print(f"Çeviri: {ceviri_sonucu}")
