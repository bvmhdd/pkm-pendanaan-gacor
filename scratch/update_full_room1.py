import os

folder = r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026"
index_file = os.path.join(folder, "INDEX-ANALISIS-PKP2.md")

room1_summary = """

---

# Bedah Komprehensif Seluruh Room 1 (Room 1-1 s.d. Room 1-5)

> Analisis mendalam terhadap 5 berkas Room 1 (~1,8 juta karakter) yang merekam seluruh sesi penilaian kemajuan di Room 1 PKP 2026.

## 1. Pemetaan Skema di Room 1
- **Room 1-1 (PKM-PM & PKM-PI):** Rekayasa sosial dan teknologi terapan untuk mitra (Smart Antropometri Stunting Posyandu, Papan Komunikasi AAC Siswa SLB, Penentu Akurasi Arah Kiblat Istiwa).
- **Room 1-2 (PKM-KC - Karsa Cipta Murni):** Panggung utama prototipe teknologi cerdas (Smart Clove Separator, Fetalguard Maternal Wearable, Stetoskop Paru ESP32-S3 TinyML UGM, Alat Kualitas Daya Listrik Polines, Klasifikasi Sayuran Hijau). Penilai: **Bpk. Guntur Eka Saputra & Bpk. Muhammad Izzuddin Mahali**.
- **Room 1-3 (PKM-RSH):** Riset Sosial Humaniora (Buzzer Alert Medsos, Vitalitas Bahasa Daerah, Game Edukasi Budaya Mandar, Etnomistika).
- **Room 1-4 (PKM-RSH & Media Edukasi):** Riset sosial dan perancangan media pembelajaran grafis (Beyond Sugar Graphics).
- **Room 1-5 (PKM-RE - Riset Eksakta Laboratorium):** Sintesis kimia dan material maju biomedis (Scaffold Komposit Tulang, Nanohidroksiapatit, Nano Kitosan, Biokarbonat).

## 2. Analisis Kasus Karsa Cipta & Teknologi (Room 1-1 & 1-2)

### A. UGM — Stetoskop Digital Paru & Breathing Mask (Room 1-2)
- **Konsep:** Skrining dini penyakit respirasi balita non-invasif berbasis ESP32-S3, sensor stetoskop akustik, breathing mask laju respirasi, dan OLED.
- **Poin Kuat:** Hardware kompak, edge AI mandiri tanpa cloud (cocok untuk faskes terpencil), pemilihan mikrokontroler tepat (ESP32-S3 punya instruksi vektor untuk TinyML).
- **Inspirasi untuk Tim:** Metodologi akustik analog + TinyML ESP32-S3 ini bisa kita adaptasi ke ranah non-medis (**Bio-Acoustic Wood Stethoscope Hama Sawit**) agar terhindar dari perizinan etik RS yang berbelit.

### B. Polines — Alat Perbaikan Kualitas Daya & THD Harmonisa (Room 1-2)
- **Konsep:** Pengukuran distorsi harmonisa (THD) pada gelombang listrik via algoritma FFT di ESP32, dilengkapi switching kapasitor bank bertingkat dan notifikasi IoT.
- **Poin Kuat:** Murni ranah Teknik Elektro (Power Systems, Signal Processing).
- **Kritik Keras Juri:** Pemilihan relay mekanik untuk switching kapasitor dinilai berbahaya (rawan arcing/percikan api) dan sensor PZEM dinilai kurang memadai untuk frekuensi tinggi.
- **Inspirasi untuk Tim:** Kita bisa melangkah lebih jauh ke ranah **Deteksi Partial Discharge Trafo PLN** menggunakan antena microstrip RF PCB dan sensor TEV non-kontak (lebih aman, canggih, dan berstandar industri).

### C. Tim Antropometri Digital Posyandu (Room 1-1)
- **Konsep:** Alat ukur tinggi dan berat badan balita otomatis dalam satu proses terintegrasi website Posyandu untuk mitigasi stunting.
- **Kritik Juri:** Stabilitas mekanik tiang saat balita meronta, serta daya tahan dan kemandirian kader Posyandu saat mengoperasikan alat tanpa tim mahasiswa.

### D. PCR — Fetalguard / Vetaguard Maternal Wearable (Room 1-2)
- **Konsep:** Sabuk wearable pemantau detak jantung janin dan ibu hamil berbasis hybrid deep learning CNN-LSTM terintegrasi IoT.
- **Poin Kuat:** Kesiapan integrasi prototipe ke website dan aplikasi mobile, narasi masalah kesehatan yang terukur.
"""

with open(index_file, "a", encoding="utf-8") as f:
    f.write(room1_summary)

print("INDEX-ANALISIS-PKP2.md updated with full Room 1 breakdown.")
