# src/utils.py
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_va(ax, V, A, title):
    # Membuat warna gradasi dari episode lama (terang) ke episode baru (gelap)[cite: 1]
    shades = np.linspace(0.0, 0.8, len(V))
    ax.scatter(V, A, c=shades, cmap="gray", s=25)
    
    # Memberi nomor episode di titik plot[cite: 1]
    for i, (v, a) in enumerate(zip(V, A), 1):
        ax.annotate(str(i), (v, a), fontsize=7, xytext=(3, 3), textcoords="offset points")
    
    ax.axhline(0, color="r", ls=":", lw=0.8)
    ax.axvline(0, color="r", ls=":", lw=0.8)
    ax.set_xlabel("Valence")
    ax.set_ylabel("Arousal")
    ax.set_title(title)

def main():
    print("Memuat data hasil eksperimen...")
    # Load file .npz yang tadi dihasilkan[cite: 1, 3]
    if not os.path.exists("data/results_exp1.npz"):
        print("Data tidak ditemukan! Jalankan dynaq-run terlebih dahulu.")
        return

    data1 = np.load("data/results_exp1.npz")
    S1, V1, A1 = data1['steps'], data1['V'], data1['A']

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    # Plot 1: Valence-Arousal Space (Pergerakan Afektif)[cite: 1, 2]
    plot_va(ax[0], V1, A1, "Exp. 1: Pergerakan Affective States")

    # Plot 2: Learning Curve (Langkah per episode)[cite: 1, 2]
    eps = np.arange(1, len(S1) + 1)
    ax[1].plot(eps, S1, label="Eksperimen 1", marker='o', markersize=4)
    ax[1].set_xlabel("Episodes")
    ax[1].set_ylabel("Steps per episode")
    ax[1].set_title("Kurva Pembelajaran (Learning Curve)")
    ax[1].legend()

    plt.tight_layout()
    
    # Simpan hasil plot ke folder data
    save_path = "data/plot_results.png"
    plt.savefig(save_path, dpi=150)
    print(f"Berhasil! Grafik telah disimpan sebagai gambar di: {save_path}")

if __name__ == "__main__":
    main()