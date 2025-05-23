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

# Fungsi invers untuk Tsukamoto
def invers_rendah(α):
    return 30 - α * 30

def invers_sedang(α):
    return α * 30 + 20 if α <= 0.5 else 80 - α * 30

def invers_tinggi(α):
    return α * 40 + 60

# Input suhu
suhu_input = float(input("Masukkan suhu (°C): "))

# Derajat keanggotaan
dingin = suhu_dingin(suhu_input)
hangat = suhu_hangat(suhu_input)
panas = suhu_panas(suhu_input)

# Rata-rata tertimbang
output_rendah = 20
output_sedang = 50
output_tinggi = 80
total_nilai = dingin * output_rendah + hangat * output_sedang + panas * output_tinggi
total_bobot = dingin + hangat + panas
hasil_output = total_nilai / total_bobot if total_bobot != 0 else 0

# Tsukamoto
rules = []
if dingin > 0:
    rules.append((dingin, invers_rendah(dingin)))
if hangat > 0:
    rules.append((hangat, invers_sedang(hangat)))
if panas > 0:
    rules.append((panas, invers_tinggi(panas)))

numerator = sum(α * z for α, z in rules)
denominator = sum(α for α, _ in rules)
tsukamoto_output = numerator / denominator if denominator != 0 else 0

# Output
print("\n=== HASIL FUZZY ===")
print(f"Suhu input: {suhu_input}°C")
print(f"Derajat dingin: {dingin:.2f}, hangat: {hangat:.2f}, panas: {panas:.2f}")
print(f"Rata-rata tertimbang: {hasil_output:.2f}%")
print("\n=== HASIL INFERENSI TSUKAMOTO ===")
for i, (α, z) in enumerate(rules, 1):
    print(f"Rule {i}: α = {α:.2f}, z = {z:.2f}")
print(f"Output akhir (Tsukamoto): {tsukamoto_output:.2f}%")

# Plot
x_suhu = np.linspace(15, 45, 300)
x_kipas = np.linspace(0, 100, 300)
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x_suhu, [suhu_dingin(x) for x in x_suhu], label='Dingin')
plt.plot(x_suhu, [suhu_hangat(x) for x in x_suhu], label='Hangat')
plt.plot(x_suhu, [suhu_panas(x) for x in x_suhu], label='Panas')
plt.axvline(suhu_input, color='black', linestyle='--', label=f'Input: {suhu_input}°C')
plt.title("Fungsi Keanggotaan Suhu")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x_kipas, [kecepatan_rendah(x) for x in x_kipas], label='Rendah')
plt.plot(x_kipas, [kecepatan_sedang(x) for x in x_kipas], label='Sedang')
plt.plot(x_kipas, [kecepatan_tinggi(x) for x in x_kipas], label='Tinggi')
plt.axvline(tsukamoto_output, color='purple', linestyle='--', label=f'Tsukamoto: {tsukamoto_output:.2f}%')
plt.title("Output Kecepatan Kipas")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
