import time

def pomodoro(sure):
    print(f"{sure} dakika çalışmaya başla!")
    time.sleep(sure * 60)
    print("Süre doldu! Kısa bir mola ver.")

calisma_suresi = int(input("Kaç dakika çalışmak istiyorsunuz? "))
pomodoro(calisma_suresi)
