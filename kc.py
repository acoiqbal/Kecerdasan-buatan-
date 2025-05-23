# Re-import necessary packages due to kernel reset
import matplotlib.pyplot as plt
import numpy as np

# Redefine suhu membership functions
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

# Redefine kecepatan membership functions
def kecepatan_rendah(x):
    if x <= 0:
        return 1
    elif 0 < x < 15:
        return (15 - x) / 15
    elif 15 <= x <= 30:
        return (30 - x) / 15
    else:
        return 0

def kecepatan_sedang(x):
    if 20 <= x < 45:
        return (x - 20) / (45 - 20)
    elif 45 <= x <= 70:
        return (70 - x) / (70 - 45)
    else:
        return 0

def kecepatan_tinggi(x):
    if x <= 60:
        return 0
    elif 60 < x < 100:
        return (x - 60) / (100 - 60)
    else:
        return 1

# Prepare x values
x_vals_suhu = np.linspace(15, 45, 300)
dingin_vals = [suhu_dingin(x) for x in x_vals_suhu]
hangat_vals = [suhu_hangat(x) for x in x_vals_suhu]
panas_vals = [suhu_panas(x) for x in x_vals_suhu]

x_vals_kecepatan = np.linspace(0, 100, 300)
rendah_vals = [kecepatan_rendah(x) for x in x_vals_kecepatan]
sedang_vals = [kecepatan_sedang(x) for x in x_vals_kecepatan]
tinggi_vals = [kecepatan_tinggi(x) for x in x_vals_kecepatan]

# Plot
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=False)

# Suhu plot
axs[0].plot(x_vals_suhu, dingin_vals, label='Dingin', color='blue')
axs[0].plot(x_vals_suhu, hangat_vals, label='Hangat', color='orange')
axs[0].plot(x_vals_suhu, panas_vals, label='Panas', color='red')
axs[0].set_title("Fungsi Keanggotaan Suhu")
axs[0].set_xlabel("Suhu (°C)")
axs[0].set_ylabel("Derajat Keanggotaan")
axs[0].legend()
axs[0].grid(True)

# Kecepatan plot
axs[1].plot(x_vals_kecepatan, rendah_vals, label='Rendah', color='green')
axs[1].plot(x_vals_kecepatan, sedang_vals, label='Sedang', color='orange')
axs[1].plot(x_vals_kecepatan, tinggi_vals, label='Tinggi', color='red')
axs[1].set_title("Fungsi Keanggotaan Kecepatan Kipas")
axs[1].set_xlabel("Kecepatan Kipas (%)")
axs[1].set_ylabel("Derajat Keanggotaan")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
