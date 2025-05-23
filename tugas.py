import matplotlib.pyplot as plt
import numpy as np

# Fungsi keanggotaan suhu
def suhu_dingin(x):
    if x <= 20:
        return 1
    elif 20 < x < 25:
        return (25 - x) / 5
    else:
        return 0

def suhu_hangat(x):
    if 23 <= x < 26.5:
        return (x - 23) / 3.5
    elif 26.5 <= x <= 30:
        return (30 - x) / 3.5
    else:
        return 0

def suhu_panas(x):
    if x <= 28:
        return 0
    elif 28 < x < 40:
        return (x - 28) / 12
    else:
        return 1

# Fungsi keanggotaan kecepatan kipas
def kecepatan_rendah(x):
    if x <= 0:
        return 1
    elif 0 < x < 30:
        return (30 - x) / 30
    else:
        return 0

def kecepatan_sedang(x):
    if 20 < x < 50:
        return (x - 20) / 30
    elif 50 <= x < 80:
        return (80 - x) / 30
    else:
        return 0

def kecepatan_tinggi(x):
    if x <= 60:
        return 0
    elif 60 < x < 100:
        return (x - 60) / 40
    else:
        return 1

# Input
try:
    suhu_input = float(input("Masukkan suhu saat ini (°C): "))
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
    exit()

# Hitung derajat keanggotaan suhu
dingin = suhu_dingin(suhu_input)
hangat = suhu_hangat(suhu_input)
panas = suhu_panas(suhu_input)

# Defuzzifikasi dengan metode rata-rata tertimbang
output_rendah = 20
output_sedang = 50
output_tinggi = 80

total_nilai = (dingin * output_rendah) + (hangat * output_sedang) + (panas * output_tinggi)
total_bobot = dingin + hangat + panas

if total_bobot == 0:
    hasil_output = 0
else:
    hasil_output = total_nilai / total_bobot

# Tampilkan hasil
print("\n=== HASIL FUZZY ===")
print(f"Input Suhu: {suhu_input}°C")
print(f"  Derajat Dingin: {dingin:.2f}")
print(f"  Derajat Hangat: {hangat:.2f}")
print(f"  Derajat Panas : {panas:.2f}")
print(f"\nRekomendasi Kecepatan Kipas: {hasil_output:.2f}%")

# Plot
x_vals_suhu = np.linspace(15, 45, 300)
dingin_vals = [suhu_dingin(x) for x in x_vals_suhu]
hangat_vals = [suhu_hangat(x) for x in x_vals_suhu]
panas_vals = [suhu_panas(x) for x in x_vals_suhu]

x_vals_kecepatan = np.linspace(0, 100, 300)
rendah_vals = [kecepatan_rendah(x) for x in x_vals_kecepatan]
sedang_vals = [kecepatan_sedang(x) for x in x_vals_kecepatan]
tinggi_vals = [kecepatan_tinggi(x) for x in x_vals_kecepatan]

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plot suhu
axs[0].plot(x_vals_suhu, dingin_vals, label='Dingin', color='blue')
axs[0].plot(x_vals_suhu, hangat_vals, label='Hangat', color='orange')
axs[0].plot(x_vals_suhu, panas_vals, label='Panas', color='red')
axs[0].axvline(suhu_input, color='black', linestyle='--', label=f'Input: {suhu_input}°C')
axs[0].set_title("Fungsi Keanggotaan Suhu")
axs[0].set_xlabel("Suhu (°C)")
axs[0].set_ylabel("Derajat Keanggotaan")
axs[0].legend()
axs[0].grid(True)

# Plot kecepatan
axs[1].plot(x_vals_kecepatan, rendah_vals, label='Rendah', color='green')
axs[1].plot(x_vals_kecepatan, sedang_vals, label='Sedang', color='orange')
axs[1].plot(x_vals_kecepatan, tinggi_vals, label='Tinggi', color='red')
axs[1].axvline(hasil_output, color='black', linestyle='--', label=f'Output: {hasil_output:.2f}%')
axs[1].set_title("Output Fuzzy : Kecepatan Kipas")
axs[1].set_xlabel("Kecepatan Kipas (%)")
axs[1].set_ylabel("Derajat Keanggotaan")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
