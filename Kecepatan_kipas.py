# Fungsi untuk kecepatan rendah (0 - 30), segitiga puncak di 15
def kecepatan_rendah(x):
    if x <= 0:
        return 1
    elif 0 < x < 15:
        return (15 - x) / 15
    elif 15 <= x <= 30:
        return (30 - x) / 15
    else:
        return 0

# Fungsi untuk kecepatan sedang (20 - 70), segitiga puncak di 45
def kecepatan_sedang(x):
    if 20 <= x < 45:
        return (x - 20) / (45 - 20)
    elif 45 <= x <= 70:
        return (70 - x) / (70 - 45)
    else:
        return 0

# Fungsi untuk kecepatan tinggi (60 - 100), linear naik
def kecepatan_tinggi(x):
    if x <= 60:
        return 0
    elif 60 < x < 100:
        return (x - 60) / (100 - 60)
    else:
        return 1

# Tes input pengguna
try:
    v = float(input("Masukkan kecepatan kipas (%): "))
    rendah = kecepatan_rendah(v)
    sedang = kecepatan_sedang(v)
    tinggi = kecepatan_tinggi(v)

    print(f"\nDerajat Keanggotaan Kecepatan:")
    print(f"Rendah : {rendah:.2f}")
    print(f"Sedang : {sedang:.2f}")
    print(f"Tinggi : {tinggi:.2f}")

except ValueError:
    print("Masukkan angka kecepatan yang valid.")
