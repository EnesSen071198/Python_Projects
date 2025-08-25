import random
import math

# Hayvan sınıfı
class Hayvan:
    def __init__(self, tur, cinsiyet, x, y, hareket_birimi):
        self.tur = tur
        self.cinsiyet = cinsiyet
        self.x = x
        self.y = y
        self.hareket_birimi = hareket_birimi

    def hareket_et(self):
        self.x += random.randint(-self.hareket_birimi, self.hareket_birimi)
        self.y += random.randint(-self.hareket_birimi, self.hareket_birimi)
        self.x = max(0, min(500, self.x))  # Alanın sınırları
        self.y = max(0, min(500, self.y))

# Avcı sınıfı
class Avci:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hareket_et(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        self.x = max(0, min(500, self.x))
        self.y = max(0, min(500, self.y))

# Mesafe hesaplama fonksiyonu
def mesafe(hayvan1, hayvan2):
    return math.sqrt((hayvan1.x - hayvan2.x) ** 2 + (hayvan1.y - hayvan2.y) ** 2)

# Hayvanların oluşturulması
def hayvanlari_olustur():
    hayvanlar = []
    # Koyun
    hayvanlar.extend([Hayvan("koyun", random.choice(["erkek", "dişi"]), random.randint(0, 500), random.randint(0, 500), 2) for _ in range(30)])
    # Inek
    hayvanlar.extend([Hayvan("inek", random.choice(["erkek", "dişi"]), random.randint(0, 500), random.randint(0, 500), 2) for _ in range(10)])
    # Tavuk
    hayvanlar.extend([Hayvan("tavuk", "dişi", random.randint(0, 500), random.randint(0, 500), 1) for _ in range(10)])
    # Horoz
    hayvanlar.extend([Hayvan("horoz", "erkek", random.randint(0, 500), random.randint(0, 500), 1) for _ in range(10)])
    # Kurt
    hayvanlar.extend([Hayvan("kurt", random.choice(["erkek", "dişi"]), random.randint(0, 500), random.randint(0, 500), 3) for _ in range(10)])
    # Aslan
    hayvanlar.extend([Hayvan("aslan", random.choice(["erkek", "dişi"]), random.randint(0, 500), random.randint(0, 500), 4) for _ in range(8)])

    return hayvanlar

# Ana simülasyon döngüsü
def simulasyon():
    hayvanlar = hayvanlari_olustur()
    avci = Avci(random.randint(0, 500), random.randint(0, 500))

    for hareket in range(1000):
        # Hayvanlar hareket eder
        for hayvan in hayvanlar:
            hayvan.hareket_et()

        # Avcı hareket eder
        avci.hareket_et()

        # Kurtlar avlanır
        for kurt in [h for h in hayvanlar if h.tur == "kurt"]:
            hedefler = [h for h in hayvanlar if h.tur in ["koyun", "tavuk", "horoz"] and mesafe(kurt, h) <= 4]
            for hedef in hedefler:
                hayvanlar.remove(hedef)

        # Aslanlar avlanır
        for aslan in [h for h in hayvanlar if h.tur == "aslan"]:
            hedefler = [h for h in hayvanlar if h.tur in ["koyun", "inek"] and mesafe(aslan, h) <= 5]
            for hedef in hedefler:
                hayvanlar.remove(hedef)

        # Avcı avlanır
        hedefler = [h for h in hayvanlar if mesafe(avci, h) <= 8]
        for hedef in hedefler:
            hayvanlar.remove(hedef)

        # Üreme
        yeni_hayvanlar = []
        for hayvan1 in hayvanlar:
            for hayvan2 in hayvanlar:
                if hayvan1 != hayvan2 and hayvan1.tur == hayvan2.tur and hayvan1.cinsiyet != hayvan2.cinsiyet and mesafe(hayvan1, hayvan2) <= 3:
                    yeni_hayvanlar.append(Hayvan(hayvan1.tur, random.choice(["erkek", "dişi"]), random.randint(0, 500), random.randint(0, 500), hayvan1.hareket_birimi))
        hayvanlar.extend(yeni_hayvanlar)

    # Sonuçlar
    tur_sayilari = {}
    for hayvan in hayvanlar:
        tur_sayilari[hayvan.tur] = tur_sayilari.get(hayvan.tur, 0) + 1

    print("Simülasyon Sonuçları:")
    for tur, sayi in tur_sayilari.items():
        print(f"{tur}: {sayi}")

if __name__ == "__main__":
    simulasyon()
