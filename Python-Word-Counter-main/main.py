def word_counter(file_name):
    # Metin dosyasını oku
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

    # Kelimeleri sayma
    words = text.split()
    word_frequency = {}

    for word in words:
        word = word.lower().strip(".,!?;:()[]{}\"'")
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Sonuçları gösterme
    for word, frequency in sorted(word_frequency.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {frequency}")
    
    # Toplam kelime sayısı
    print(f"Total word count: {len(words)}")  # Toplam kelime sayısını gösterir

# Ana fonksiyon
if __name__ == "__main__":
    file_name = 'sample.txt'  # Metin dosyasının adı
    word_counter(file_name)
