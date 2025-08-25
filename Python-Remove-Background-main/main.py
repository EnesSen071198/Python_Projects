from rembg import remove
from PIL import Image
import os

def remove_background(input_path, output_path):
    # Görüntüyü yükle
    input_image = Image.open(input_path)

    # Arkaplanı sil
    output_image = remove(input_image)

    # JPEG olarak kaydetmeden önce RGBA'dan RGB'ye dönüştür
    if output_image.mode == 'RGBA':
        output_image = output_image.convert('RGB')

    # Sonucu kaydet
    output_image.save(output_path)

def process_directory(input_dir, output_dir):
    # Çıktı klasörünü oluştur
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Tüm görüntüleri işle
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"no_bg_{filename}")
            remove_background(input_path, output_path)
            print(f"İşlendi: {filename}")

# Kullanım örneği
if __name__ == "__main__":
    input_dir = "input_images"
    output_dir = "output_images"
    process_directory(input_dir, output_dir)
