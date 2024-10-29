import numpy as np
import imageio
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

# Fungsi untuk memproses gambar
def process_image(input_path, output_path, sigma):
    # Membaca gambar
    image = imageio.imread(input_path)
    
    # Mengonversi gambar ke grayscale jika berwarna
    if len(image.shape) == 3:
        image = np.mean(image, axis=2).astype(np.uint8)
    
    # Menerapkan filter Gaussian
    smoothed_image = gaussian_filter(image, sigma=sigma)

    # Menyimpan gambar yang telah diproses
    imageio.imwrite(output_path, smoothed_image)

    # Menampilkan gambar asli dan gambar yang telah diproses
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("Gambar Asli")
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Gambar Setelah Filter Gaussian")
    plt.imshow(smoothed_image, cmap='gray')
    plt.axis('off')

    plt.show()

# Path untuk gambar input dan output
input_image_path = 'C:/Users/lenovo/Downloads/photo_6167803359428460692_y.jpg'  # Ganti dengan path gambar input
output_image_path = 'C:/Users/lenovo/Downloads/image_smoothed.jpg'  # Ganti dengan path gambar output

sigma_value = 2  # Variance untuk filter Gaussian

# Menjalankan fungsi
process_image(input_image_path, output_image_path, sigma_value)
