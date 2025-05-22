# Fungsi untuk suhu dingin (turun dari 25 ke 20)
def suhu_dingin(x):
    if x <= 20:
        return 1
    elif 20 < x < 25:
        return (25 - x) / (25 - 20)
    else:
        return 0

# Fungsi untuk suhu hangat (segitiga 23 - 26.5 - 30)
def suhu_hangat(x):
    if 23 <= x < 26.5:
        return (x - 23) / (26.5 - 23)
    elif 26.5 <= x <= 30:
        return (30 - x) / (30 - 26.5)
    else:
        return 0

# Fungsi untuk suhu panas (naik dari 28 ke 40)
def suhu_panas(x):
    if x <= 28:
        return 0
    elif 28 < x < 40:
        return (x - 28) / (40 - 28)
    else:
        return 1

# Tes input pengguna
try:
    x = float(input("Masukkan suhu ruangan (°C): "))
    dingin = suhu_dingin(x)
    hangat = suhu_hangat(x)
    panas = suhu_panas(x)

    print(f"\nDerajat Keanggotaan:")
    print(f"Dingin: {dingin:.2f}")
    print(f"Hangat: {hangat:.2f}")
    print(f"Panas : {panas:.2f}")

except ValueError:
    print("Masukkan angka suhu yang valid.")
  
