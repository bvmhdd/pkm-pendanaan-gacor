# PANDUAN PROMPT NAPKIN AI — PROPOSAL PKM-KC LITHOSCAN 2026

Dokumen ini memuat teks prompt terstruktur khusus untuk di-generate di **Napkin AI** (https://www.napkin.ai).
Format teks di bawah ini dirancang dengan hierarki ringkas dan padat agar Napkin AI menghasilkan visual berorientasi **Horizontal / Compact Grid** (lebar menyamping, tidak memakan banyak tinggi halaman), sehingga pas dan tidak membuat proposal melebihi batas 10 halaman.

---

## Cara Menggunakan di Napkin AI:
1. Buka [https://www.napkin.ai](https://www.napkin.ai) dan buat dokumen baru (*New Napkin*).
2. Salin (*copy*) teks prompt di bawah ini untuk masing-masing gambar.
3. Tempel (*paste*) teks ke editor Napkin AI.
4. Sorot teks tersebut, lalu klik ikon **Sparkle / Generate Visual** di sisi kiri.
5. Pada pilihan variasi diagram:
   - Pilih layout bertipe **Horizontal Flow**, **Chevron / Process**, atau **Multi-Column Card Matrix**.
   - Hindari layout vertikal panjang agar hemat ruang halaman Word.
6. Klik **Download / Export** -> Pilih **PNG (Transparent)** atau **SVG**, lalu masukkan ke Microsoft Word dengan lebar diatur sekitar **13–14 cm** (Center).

---

## PROMPT 1: Gambar 1.1 Diagram Blok Konseptual Instrumen LITHOSCAN

Salin teks di bawah ini ke Napkin AI:

```text
Arsitektur Sistem Instrumen Medis LITHOSCAN (Deteksi Dini Risiko Nefrolitiasis):

1. Ruang Sampel & Optik (Cuvette Chamber)
- Sumber Cahaya: NIR LED 860 nm (Standar ISO 7027-1) dan LED Soret 415 nm
- Sampel: Kuvet Kaca Optik 10x10 mm Berisi Urin Pasien
- Sensor Deteksi: Photodiode Nefelometri Hamburan 90° dan Sensor Spektrometer 11-Kanal ams AS7341
- Sensor Suhu: NTC Thermistor 10k Presisi 0.5% Menempel pada Kuvet

2. Pengondisi Sinyal Analog & Termal (AFE & Thermal PID)
- Penguat Arus Rendah: Transimpedance Amplifier (TIA OPA388) Zero-Drift
- Reduksi Noise: Active Low Pass Filter & ADC 16-bit
- Kontrol Termal Fisiologis: Pemanas PTC Keramik dengan Pengendali Loop Tertutup PID Stabil 37.0°C ± 0.2°C

3. Unit Pemroses Tepi (Edge Computing ESP32-S3)
- Mikrokontroler: ESP32-S3 Dual-Core 240 MHz (512 KB SRAM, 8 MB PSRAM)
- Mesin AI Lokal: Pipeline TinyML INT8 on-Device (Zero-Cloud Dependency)
- Fungsi: Fusi Data Spektral, Ekstraksi Laju Turbiditas, dan Inferensi Indeks Risiko < 45 ms

4. Antarmuka Pasien & Telemetri Medis
- Tampilan Alat: Layar OLED 0.96 inch Menampilkan Level Risiko Instan
- Komunikasi Nirkabel: BLE 5.0 (Bluetooth Low Energy) & Wi-Fi
- Platform Pasien: Aplikasi Android Telemonitoring & Rekomendasi Terapi Hidrasi Presisi
```

---

## PROMPT 2: Gambar 2.1 Kurva Kinetika Agregasi Turbiditas CaOx dan Respon Spektroskopi AS7341

Salin teks di bawah ini ke Napkin AI:

```text
Dinamika Kinetika Kristalisasi Kalsium Oksalat (CaOx) pada Urin 37.0°C dan Respons Multispektral AS7341:

Fase 1: Fase Induksi (Menit 0–10)
- Kondisi Urin: Larutan metastabil, ion kalsium dan oksalat larut bebas
- Sinyal Hamburan 90°: Turbiditas sangat rendah (< 5 NTU), transmisi NIR 860 nm tinggi (> 95%)
- Respons AS7341: Kanal spektral F1–F8 stabil, kanal 415 nm mengukur konsentrasi pigmen urobilin dasar
- Status Medis: Belum terjadi presipitasi kristal, kondisi aman

Fase 2: Nukleasi & Agregasi Cepat (Menit 10–25)
- Kondisi Urin: Titik jenuh terlampaui, kristal COM/COD mulai tumbuh dan beragregasi (2–12 µm)
- Sinyal Hamburan 90°: Lonjakan turbiditas tajam dengan laju tinggi (dNTU/dt > 4.5 NTU/menit)
- Respons AS7341: Reduksi absorbansi serentak pada spektrum visual F1–F4 (410–515 nm) akibat hamburan Mie
- Status Medis: Risiko pembentukan batu ginjal aktif, butuh intervensi hidrasi cepat

Fase 3: Fase Kejenuhan / Makroagregat (Menit 25–40)
- Kondisi Urin: Kristal membentuk makroagregat besar (> 20 µm) dan mulai mengendap
- Sinyal Hamburan 90°: Turbiditas mencapai batas kejenuhan konstan (plateau ~95 NTU)
- Respons AS7341: Rasio spektral A415/A860 terkunci untuk mengestimasi indeks saturasi urin
- Status Medis: Risiko litogenik kritis, potensi obstruksi saluran kemih
```

---

## PROMPT 3: Gambar 3.1 Diagram Alir Tahapan Pelaksanaan Enjiniring LITHOSCAN

Salin teks di bawah ini ke Napkin AI:

```text
Tahapan Rekayasa Sistem Enjiniring Prototipe LITHOSCAN (Jadwal 4 Bulan PKM-KC):

Tahap 1: Desain & Fabrikasi Perangkat Keras (Bulan 1)
- Pemodelan 3D Cuvette Chamber & Enclosure Optik Menggunakan PETG Hitam
- Perakitan Sirkuit Analog Front-End (TIA OPA388) & Driver LED Dual-Wavelength
- Pemasangan Pemanas PTC dan Kalibrasi Pengendali PID Suhu 37.0°C ± 0.2°C
- Uji Lolos Milestone 1: Drift Suhu < 0.5°C dan Signal-to-Noise Ratio (SNR) Optik > 40 dB

Tahap 2: Pengembangan Algoritma TinyML & Firmware (Bulan 2)
- Akuisisi Data Spektral 11-Kanal AS7341 & Turbiditas 90° dari Larutan Uji
- Ekstraksi Fitur: Kemiringan Laju Agregasi (dNTU/dt), Rasio Soret Band, dan AUC
- Pelatihan Model Random Forest & Kuantisasi Penuh INT8 via TensorFlow Lite Micro
- Uji Lolos Milestone 2: Akurasi Model > 90%, Latensi < 100 ms, dan Alokasi RAM < 64 KB

Tahap 3: Validasi Laboratorium Urin Sintetis ASTM (Bulan 3)
- Formulasi Urin Sintetis Berbagai Tingkat Kejenuhan Kalsium dan Oksalat
- Pengujian Rentang Dinamis Turbiditas (0.1–100 NTU) dan Koreksi Warna/Hematuria
- Uji Komparasi Akurasi dengan Spektrofotometer UV-Vis Benchtop Laboratorium
- Uji Lolos Milestone 3: Koefisien Determinasi R² > 0.95 dan Presisi CV < 5%

Tahap 4: Integrasi Sistem, Telemetri & Evaluasi Komparatif (Bulan 4)
- Integrasi Koneksi Nirkabel BLE 5.0 ke Aplikasi Mobile Android Pasien
- Uji Ketahanan Alat, Efisiensi Daya Baterai Li-ion, dan Evaluasi Side-by-Side vs Strip Celup Urin
- Finalisasi Prototipe Fungsional Siap Uji (TRL 4–5) & Penyusunan Laporan Kemajuan
- Uji Lolos Milestone 4: Sistem Beroperasi Mandiri Siap Dipresentasikan di PKP2
```

---

## PROMPT 4: Gambar 3.2 Arsitektur Pipeline TinyML INT8 on-Device ESP32-S3

Salin teks di bawah ini ke Napkin AI:

```text
Pipeline Inferensi TinyML INT8 on-Device ESP32-S3 (Komputasi Tepi Mandiri Tanpa Cloud):

1. Masukan Sensor Multimodal (Sampling 10 Hz)
- Sensor Spektroskopi 11-Kanal AS7341 (Kanal F1–F8, NIR 910 nm, Clear)
- Detektor Hamburan 90° Nefelometri (Cahaya NIR 860 nm)
- Sensor Suhu Termistor NTC (Verifikasi Suhu Tubuh 37.0°C)

2. Pra-pemrosesan & Ekstraksi Fitur On-Device
- Koreksi Baseline & Pengurangan Arus Gelap (Dark-Current Subtraction)
- Fitur 1: Laju Kinetika Agregasi Kristal per Satuan Waktu (dNTU/dt)
- Fitur 2: Indeks Rasio Penyerapan Hemoglobin Soret Band (A415 / A680)
- Fitur 3: Total Area Bawah Kurva Turbiditas (AUC)

3. Mesin Inferensi Terkuantisasi INT8 (SRAM ESP32-S3)
- Model: Quantized Random Forest & Compact Multilayer Perceptron (MLP)
- Format: Fixed-Point INT8 Menggunakan TensorFlow Lite Micro
- Efisiensi: Waktu Komputasi < 45 ms, Penggunaan RAM < 48 KB, Akselerasi SIMD ESP-NN

4. Klasifikasi Indeks Risiko Litogenik (3 Kategori)
- Tingkat 1 - Risiko Rendah (Hijau): Urin normal terhidrasi, kristaluria nihil
- Tingkat 2 - Risiko Sedang (Kuning): Supersaturasi awal terdeteksi, butuh hidrasi 500 mL
- Tingkat 3 - Risiko Tinggi (Merah): Agregasi masif CaOx aktif, risiko obstruksi tinggi

5. Luaran Sistem & Aksi Medis
- Layar OLED 0.96 inch Alat Menampilkan Tingkat Risiko Seketika
- Transmisi Data BLE 5.0 ke Aplikasi Smartphone untuk Riwayat Harian
- Peringatan Dini Hidrasi Presisi bagi Pasien Pencegah Kekambuhan
```
