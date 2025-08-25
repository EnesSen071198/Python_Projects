import requests

API_KEY = '6a95fe6850729eed0555c267ee974578'
BASE_URL = 'https://api.themoviedb.org/3/'

def film_ara(query):
    url = f"{BASE_URL}search/movie?api_key={API_KEY}&query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results', [])
        if results:
            for film in results:
                print(f"Başlık: {film['title']}\nAçıklama: {film['overview']}\n")
        else:
            print("Film bulunamadı.")
    else:
        print("API isteğinde hata oluştu.")
        print(f"Hata kodu: {response.status_code}")
        print(f"Mesaj: {response.json()}")

query = input("Aramak istediğiniz filmi girin: ")
film_ara(query)
