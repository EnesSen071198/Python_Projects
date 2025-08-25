import random

sorular = {
    "Python nedir?": "Bir programlama dili",
    "HTML nedir?": "Bir işaretleme dili",
    "CSS nedir?": "Bir stil sayfası dili",
}

def quiz_yap():
    soru, cevap = random.choice(list(sorular.items()))
    kullanici_cevap = input(f"{soru} ")
    if kullanici_cevap.lower() == cevap.lower():
        print("Doğru!")
    else:
        print(f"Yanlış! Doğru cevap: {cevap}")

quiz_yap()
