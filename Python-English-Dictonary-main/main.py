import requests

def sozluk_ara(kelime):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{kelime}"
    response = requests.get(url)

    if response.status_code == 200:
        veri = response.json()
        anlamlar = veri[0]['meanings']

        print(f"\n'{kelime}' kelimesinin anlamları:")
        for anlam in anlamlar:
            for tanim in anlam['definitions']:
                print(f"- {tanim['definition']}")
    else:
        print(f"'{kelime}' kelimesi için bir sonuç bulunamadı.")


# Kullanıcıdan kelime girişi almak için döngü
while True:
    kelime = input("Aramak istediğiniz kelimeyi girin ('q' ile çıkış yapabilirsiniz): ")
    if kelime.lower() == 'q':
        print("Sözlük Uygulaması kapanıyor...")
        break
    sozluk_ara(kelime)
