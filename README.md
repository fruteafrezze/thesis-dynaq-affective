# Path-Finding Agent using Dyna-Q and Affective States

Implementasi simulator navigasi agen berbasis **Dyna-Q Reinforcement Learning** yang diintegrasikan dengan **Dimensional Emotional Model (Valence-Arousal Space)**. Repositori ini merujuk dan mereplikasi eksperimen *path-finding* dari paper Feldmaier & Diepold (IEEE RO-MAN 2014) dan dikembangkan secara modular menggunakan Python dan Docker.

---

## Fitur Utama

- **Reference Paper Included**: Berkas PDF paper acuan disertakan langsung di direktori `data/` untuk kemudahan referensi riset.
- **Maze Environment**: *Gridworld* 6x9 dengan rintangan (dinding) serta algoritma garis *Bresenham* untuk deteksi *Line-of-Sight* target.
- **Dimensional Affect Model**: Penghitungan dinamik *Valence* (persepsi positif/negatif) dan *Arousal* (aktivasi mental) berdasarkan frekuensi kejadian (*collision*, *direction change*, *goal in sight*, *moving away*).
- **Dyna-Q Agent**: Algoritma RL yang mengombinasikan *Direct Q-Learning*, *Model Learning*, dan *Planning Steps*.
- **Containerized Environment**: Siap dijalankan menggunakan Docker & Docker Compose tanpa mengotori *environment* lokal host.
- **Automated Logging & Visualization**: Menyimpan data eksperimen dalam format `.npz` dan menghasilkan plot *Learning Curve* serta *Valence-Arousal Space*.

---

## Struktur Proyek

```text
thesis-dynaq-affective/
├── data/                                               # Data eksperimen & paper referensi
│   ├── Path-finding Using Reinforcement Learning and Affective States.pdf
│   ├── results_exp1.npz                                # Output simulasi (auto-generated)
│   └── plot_results.png                                # Output visualisasi (auto-generated)
├── report/
│   └── report.py                                       # Pembacaan data dan pembentukan grafik
├── src/
│   ├── config.py                                       # Parameter simulasi dan hiperparameter RL
│   ├── environment.py                                  # Logika Gridworld Maze & Bresenham
│   ├── affect.py                                       # Modul kalkulasi Valence dan Arousal
│   ├── agent.py                                        # Agen / algoritma Dyna-Q RL
│   └── main.py                                         # Entrypoint utama eksekusi eksperimen
├── Dockerfile                                          # Image Docker berbasis Python 3.11-slim
├── docker-compose.yml                                  # Konfigurasi layanan container dan batas r
├── .gitignore                                          # Aturan pengabaian berkas Git
└── README.md                                           # Dokumentasi proyek
```

---

##  Panduan Penggunaan

### 1. Prasyarat

Pastikan sistem sudah memasang:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 2. Membangun dan Menyalakan Container

Jalankan perintah berikut dari direktori utama repositori:

```bash
docker-compose up -d --build
```

### 3. Menjalankan Simulasi

Eksekusi eksperimen Dyna-Q melalui container yang berjalan:

```bash
docker exec -it dyna_q_simulator python src/main.py
```

Hasil simulasi akan disimpan otomatis ke `data/results_exp1.npz`.

### 4. Membuat Plot dan Visualisasi

Jalankan skrip visualisasi untuk menghasilkan grafik:

```bash
docker exec -it dyna_q_simulator python report/report.py
```

Grafik visualisasi akan disimpan ke `data/plot_results.png`.

---

## Parameter Simulasi

Parameter default diisi berdasarkan Tabel I dari paper Feldmaier & Diepold (2014).

| Parameter | Definisi | Nilai |
| --- | --- | --- |
| `n_episodes` | Jumlah episode per eksperimen | `20` |
| `max_steps` | Batas maksimum langkah per episode | `2000` |
| `planning_steps` | Jumlah langkah *planning* per transisi | `50` |
| `alpha` (\(\alpha\)) | *Learning rate* | `0.01` |
| `gamma` (\(\gamma\)) | *Discount factor* | `0.95` |
| `epsilon` (\(\epsilon\)) | Probabilitas eksplorasi \(\epsilon\)-greedy | `0.1` |
| `nu` (\(\nu\)) | *Slope* pembaruan frekuensi tabrakan (\(f_{col}\)) | `0.2` |
| `theta1` (\(\theta_1\)) | *Slope* pembaruan perubahan arah (\(f_{dir}\)) | `0.2` |
| `theta2` (\(\theta_2\)) | *Slope* pembaruan pandangan target (\(f_{goal}\)) | `0.2` |
| `kappa` (\(\kappa\)) | *Slope* pembaruan arah pergerakan (\(f_{right}\)) | `0.15` |

---

## Referensi dan Dokumen Terkait

**Paper referensi utama:** `data/Path-finding Using Reinforcement Learning and Affective States.pdf`

Feldmaier, J., & Diepold, K. (2014). *Path-finding using reinforcement learning and affective states.* In *2014 23rd IEEE International Symposium on Robot and Human Interactive Communication (RO-MAN)* (pp. 543–548). IEEE.
