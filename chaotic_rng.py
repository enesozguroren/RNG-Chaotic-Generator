import matplotlib.pyplot as plt

def logistic_map_generator(seed, r, iterations):
    """
    Lojistik harita algoritması kullanarak sayı üretir.
    x_n+1 = r * x_n * (1 - x_n)
    """
    numbers = []
    x = seed
    
    for _ in range(iterations):
        x = r * x * (1 - x)
        numbers.append(x)
        
    return numbers

# Parametreler
seed_value = 0.23  # Başlangıç değeri (Tohum)
r_value = 4.0      # Kaos katsayısı
n_iterations = 100 # Üretilecek sayı adedi

# Sayıları üret
results = logistic_map_generator(seed_value, r_value, n_iterations)

# Sonuçları ekrana yazdır (İlk 10 sayı)
print(f"İlk 10 Kaotik Sayı (Seed: {seed_value}):")
for i, val in enumerate(results[:10], 1):
    print(f"{i}. Sayı: {val:.6f}")

# --- GÖRSELLEŞTİRME ---
plt.figure(figsize=(12, 5))

# 1. Grafik: Zaman Serisi (Sayıların bir sonraki adımda nasıl savrulduğu)
plt.subplot(1, 2, 1)
plt.plot(results, color='blue', marker='o', linestyle='-', markersize=4, alpha=0.7)
plt.title(f"Kaotik Zaman Serisi (r={r_value})")
plt.xlabel("İterasyon Adımı")
plt.ylabel("Değer (x)")
plt.grid(True)

# 2. Grafik: Dağılım Histogramı (Sayıların 0-1 arasındaki yayılımı)
plt.subplot(1, 2, 2)
plt.hist(results, bins=20, color='green', edgecolor='black', alpha=0.7)
plt.title("Sayıların Dağılım Histogramı")
plt.xlabel("Sayı Aralığı")
plt.ylabel("Frekans")

plt.tight_layout()
plt.show()