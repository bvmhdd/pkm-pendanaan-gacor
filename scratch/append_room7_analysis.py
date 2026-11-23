# -*- coding: utf-8 -*-
import os

analysis_room7 = '''

---

# Bedah Komprehensif Room 7 (PKP 2026: 14–18 September)

> Berkas sumber: `pkp pkm room 7, 14 september.md` s.d. `pkp pkm room 7, 18 september.md` (Total 5 hari rekaman PKP, ~1,9 juta karakter).
> Panggung utama PKM-KC berada di **Sesi 15 September 2026** yang menampilkan 11 prototipe teknologi tingkat nasional.

## 1. Pemetaan Skema Harian Room 7
- **14 September 2026:** PKM-PM (Pengabdian Masyarakat) — Pemberdayaan masyarakat pesisir, bank sampah, dan edukasi stunting.
- **15 September 2026:** **PKM-KC (Karsa Cipta)** & PKM-K — Panggung utama rekayasa teknologi perangkat cerdas, sensor biomedis/pertanian, Edge AI, dan TinyML.
- **16 September 2026:** PKM-VGK (Video Gagasan Konstruktif) — Rancangan futuristik tata ruang, ketahanan pangan, dan kebijakan berbasis visual 3D.
- **17 September 2026:** PKM-RE (Riset Eksakta) — Sintesis material nano, fotodegradasi katalitik, dan ekstraksi biokomposit.
- **18 September 2026:** PKM-RE (Riset Eksakta) — Formulasi nanoemulsi, uji fitokimia antibakteri, dan uji laboratorium basah.

---

## 2. Bedah 11 Prototipe PKM-KC (15 September 2026)

### A. Peduli TB (Politeknik Elektronika Negeri Surabaya - PENS)
- **Judul:** Rancang Bangun Perangkat Cerdas Portabel Berbasis TinyML Terintegrasi Multi-parameter Sensing untuk Sistem Deteksi Dini Tuberkulosis.
- **Arsitektur:** Mikrokontroler cerdas mengintegrasikan 4 sensor fisik (akustik batuk/pernapasan, sensor laju respirasi, saturasi oksigen SpO2/PPG, dan suhu tubuh). Menjalankan model inferensi TinyML langsung di perangkat (*on-device*) dengan akurasi 96,4% dan latensi rendah tanpa bergantung ke internet.
- **Realisasi Anggaran:** Plafon Belmawa Rp 7,7 juta, realisasi Rp 7,556 juta, sisa saldo akhir Rp 143.685 (pengelolaan sangat akurat).
- **Cecaran Kritis Reviewer:**
  1. *Kontaminasi Silang Antar-Pasien:* Reviewer menanyakan: *"Alat yang dibuat baru 1 unit, diuji coba ke 10 subjek (4 pasien TBC, 2 ISPA, 4 orang sehat). Bagaimana prototipe Anda menjamin tidak terjadi penularan bakteri TBC antar-pasien saat corong/sensor dipindahkan?"*
  2. *Validasi Medis & Harga Komersil:* Reviewer mencecar estimasi harga jual vs biaya produksi prototipe jika masuk tahap hilirisasi.
- **Pelajaran Tim:** Untuk perangkat yang berinteraksi fisik dengan subjek, wajib mencantumkan protokol sterilisasi/disposabel dan estimasi biaya per unit (BOM - *Bill of Materials*).

### B. Antaraga (Politeknik Elektronika Negeri Surabaya - PENS)
- **Judul:** *Smartband* Deteksi Dini Risiko Stroke Berbasis Multi-wavelength Photoplethysmography (PPG) dan Parameter Fisiologis.
- **Arsitektur:** Gelang pintar dengan multi-wavelength PPG (LED hijau, merah, inframerah) untuk mengekstraksi kekakuan pembuluh darah (*arterial stiffness*), heart rate variability (HRV), dan integrasi skor klinis stroke ABCD2 via aplikasi seluler. Menggunakan model regresi SVR/XGBoost.
- **Luaran & Diseminasi:** Akun media sosial menjangkau 37.000 akun (54.000 tayangan, 11.000 interaksi), prototipe fisik 100%, HKI Hak Cipta program komputer 100%.
- **Cecaran Kritis Reviewer:**
  1. *Variabilitas Komorbid Pasien:* *"Bagaimana sensitivitas sensor optik PPG Anda terhadap pasien yang memiliki komorbid hipertensi murni vs pasien diabetes melitus? Apakah algoritma mampu memisahkan noise arteriosklerosis karena usia vs risiko stroke akut?"*
  2. *Standar Kalibrasi Medis:* Validasi pembanding dengan tensimeter klinis dan EKG standar rumah sakit.

### C. Emeris (Universitas Negeri Surabaya - UNESA)
- **Judul:** Sandal Pintar Deteksi Jatuh (*Fall Detection*) dan Pemantauan Tremor Lansia Berbasis TinyML.
- **Arsitektur:** Sandal pintar dilengkapi sensor gerak inersia (IMU Gyroscope & Accelerometer 6-axis) yang ditanam pada *outsole*. Menjalankan model TinyML untuk mengklasifikasikan 4 kondisi gerak: Diam, Berjalan Normal, Tremor, dan Jatuh. Akurasi model 98,2%, loss 0,21.
- **Cecaran Kritis Reviewer:**
  1. *Ketebalan Fisik & Ergonomi:* Reviewer mengkritik: *"Ketebalan sandal mencapai 2–3 cm karena menampung boks komponen. Untuk lansia dengan gaya berjalan menyeret (shuffling gait), sandal setebal ini justru berisiko tinggi membuat mereka tersandung!"*
  2. *Ketahanan Beban Mekanik:* Reviewer menguji: *"Apakah boks elektrikal di telapak kaki tidak remuk bila diinjak pengguna berbobot 80 kg di tepi anak tangga?"*
  3. *False Positive Saat Sandal Miring:* Bagaimana membedakan sandal yang tergeletak miring di lantai vs lansia yang benar-benar jatuh?

### D. Nirwana AI (Universitas Pendidikan Indonesia - UPI)
- **Judul:** *Patch* Pemantau Hipoksia Ginjal Neonatus Berbasis Near-Infrared Spectroscopy (NIRS) Non-Invasif Terintegrasi TinyML.
- **Arsitektur:** Sensor optik inframerah dekat (NIRS) yang ditempelkan di punggung bayi baru lahir (neonatus) untuk mendeteksi penurunan perfusi oksigen ginjal secara dini (pencegahan *Acute Kidney Injury* / AKI).
- **Metodologi Pengujian:** Menggunakan *tissue phantom* multilayer buatan untuk mensimulasikan jaringan kulit, lemak, dan parenkim ginjal neonatus guna menghindari uji invasif tanpa *ethical clearance*. Akurasi model 93%.
- **Cecaran Kritis Reviewer:**
  1. *Keamanan Biokompatibilitas Perekat:* *"Kulit bayi neonatus sangat tipis dan rapuh. Apakah perekat patch Anda tidak menimbulkan iritasi epidermal atau laserasi saat dilepas berkali-kali?"*
  2. *Validitas Fantom vs Darah Nyata:* Reviewer menguji sejauh mana larutan phantom mampu merefleksikan dinamika pulsasi hemoglobin beroksigen nyata pada organ hidup.

### E. Disguise ID (Universitas Muslim Indonesia - UMI)
- **Judul:** Prototipe Sistem Deteksi Wajah DPO terhadap Variasi Penyamaran Berbasis CCTV Pintar dengan Model Variational Autoencoder (VAE).
- **Arsitektur:** Kamera CCTV dengan komputasi edge yang menjalankan *RetinaFace* untuk deteksi wajah, VAE untuk merekonstruksi bagian wajah yang tertutup (topeng, topi, kacamata, jenggot palsu), dan *ArcFace* untuk matching database DPO kepolisian.
- **Pengujian:** Uji lapangan langsung di area parkir terbuka Fakultas Ilmu Komputer UMI.
- **Cecaran Kritis Reviewer:**
  1. *Sudut Pandang Kamera & Evasion:* *"CCTV dipasang pada tiang tinggi. Bila target DPO menundukkan kepala atau memalingkan muka saat melihat ada kamera, bagaimana sistem tetap dapat mengenali kontur wajah?"*
  2. *Dokumentasi Fisik Prototipe:* Reviewer menegur karena foto boks fisik prototipe dan penempatan sensor tidak ditampilkan jelas di badan utama laporan kemajuan, melainkan tersembunyi di lampiran akhir.

### F. Gamelock AI (Universitas Teknologi Yogyakarta - UTY)
- **Judul:** Sistem Pemblokiran Konten dan Aplikasi Judi Online Berbasis On-Device AI.
- **Arsitektur:** Aplikasi Android dengan modul inferensi *on-device* yang menginspeksi trafik paket data lokal dan pola antarmuka visual untuk memblokir akses ke situs/aplikasi judol tanpa mengirim log pengguna ke server eksternal (menjaga privasi). Akurasi deteksi 96,59% pada 50 situs uji.
- **Cecaran Kritis Reviewer:**
  1. *Privasi vs Hak Akses (Permissions):* Reviewer menanyakan apakah izin akses VPN/Aksesibilitas lokal melanggar regulasi privasi data pribadi (UU PDP).
  2. *Bypass Evasion:* Bagaimana sistem mencegah pengguna cerdik yang menggunakan Private DNS terenkripsi (DoH/DoT) atau VPN pihak ketiga?

### G. Otomedis (Politeknik Negeri Madiun)
- **Judul:** Sistem Otoskopi Berbasis Deep Learning (YOLOv6) dan IoT untuk Identifikasi 4 Penyakit Telinga Tengah.
- **Arsitektur:** Kamera endoskopi telinga portabel dihubungkan ke modul pengolah citra yang mengidentifikasi Otitis Media Akut, Kronis, Supuratif Kronis, dan Myringosclerosis. Divalidasi langsung di RSUD Dr. Sudono Madiun.
- **Cecaran Kritis Reviewer:** Prosedur sterilisasi spekulum optik antar-pasien telinga dan latensi inferensi saat dokter mengarahkan lensa ke membran timpani yang bergetar.

### H. Spinaliz (Universitas Gadjah Mada - UGM)
- **Judul:** Sistem Deteksi dan Skrining Postur Tulang Belakang (Kifosis & Lordosis) Berbasis Computer Vision Tanpa Radiasi.
- **Arsitektur:** Kamera penangkap postur tubuh yang mengekstraksi titik sudut anatomis (*skeletal landmarks*) via computer vision, mengonversi kelengkungan kurva tulang belakang ke derajat keparahan (ringan, sedang, berat), dan menampilkannya di LCD lokal untuk faskes tingkat pertama.
- **Cecaran Kritis Reviewer:** Bagaimana akurasi penarikan titik landmark ketika pasien mengenakan pakaian tebal atau longgar?

### I. Edupos (Universitas Bina Nusantara - Binus)
- **Judul:** Sistem Monitoring Cerdas Interaksi dan Postur Belajar Siswa di Ruang Kelas Berbasis YOLO-Pose.
- **Arsitektur:** Analisis video interaksi guru dan keterlibatan siswa di kelas dengan estimasi pose 2D. Akurasi 96% pada 75 sesi pengujian.
- **Cecaran Kritis Reviewer:** Etika privasi pemantauan kontinu di kelas dan masalah *occlusion* (siswa terhalang meja atau teman di depannya).

### J. Aerator Pintar (UPN Veteran Jawa Timur)
- **Judul:** Aerator Cerdas Tambak Bandeng Terintegrasi Auto-Feeder Berbasis IoT.
- **Arsitektur:** Aerasi otomatis berbasis pembacaan sensor DO (*Dissolved Oxygen*) dan suhu air, dilengkapi pelontar pakan otomatis.
- **Cecaran Kritis Reviewer:** Mekanika lontaran pakan (radius sebaran pakan di tambak luas vs pakan hanya jatuh menetes di satu titik), serta kelengkapan grafik data pengujian 1 bulan di tambak nyata yang lupa dimasukkan tim ke slide PPT.

### K. Ekotra (Universitas Gunadarma)
- **Judul:** Ekosistem Pertanian Presisi dengan Smart Pest Sprayer Otomatis Berbasis Sensor.
- **Arsitektur:** Penyemprot hama otomatis berbasis deteksi optik/sensor lingkungan pada lahan pertanian.
- **Cecaran Kritis Reviewer:** Kelalaian administratif: video kemajuan produk dan tautan media sosial belum diunggah ke portal Simbelmawa pada batas waktu PKP.

---

## 3. Matriks Komparatif & 5 Aturan Emas Reviewer untuk PKM-KC 2027

| Aspek Ujian | Kesalahan Fatal Tim yang Dicecar | Pola Jawaban Tim yang Lolos (PENS, UGM, UPI) |
|---|---|---|
| **Kuantitas Prototipe** | Hanya membuat 1 unit fisik padahal mengklaim sistem komunikasi/skrining massal. | Membuat jumlah node yang cukup untuk membuktikan arsitektur (atau modular testbed terverifikasi). |
| **Ergonomi & Mekanik** | Boks rangkaian terlalu tebal (2–3 cm pada sandal), kabel semrawut, mudah pecah bila diinjak/jatuh. | Menggunakan enclosure standar IP54/IP65 dengan uji jatuh (*drop-test*) dan simulasi beban nyata. |
| **Edge AI / TinyML** | Mengklaim AI canggih tapi semua inferensi dioper ke server cloud (tidak jalan jika internet mati). | Inferensi model dikuantisasi (INT8/TFLite Micro) dan berjalan 100% lokal di chip MCU ESP32-S3 / RP2040. |
| **Pengujian Nyata** | Hanya simulasi software atau uji di meja lab tanpa interaksi dengan lingkungan target. | Uji empiris di lapangan (parkiran kampus, phantom jaringan biologis, kolam nyata) dengan metrik presisi. |
| **Administrasi Belmawa** | Link video progress dan media sosial lupa dicantumkan di laporan atau belum diunggah di Simbelmawa. | Kepatuhan luaran 100% (video HD di YouTube, akun Instagram aktif >10 postingan, logbook belanja rapi). |

---

## 4. Sintesis Konkret: Rekayasa Arsitektur RescueMesh Anti-Gugur Juri

Melihat anatomi cecaran reviewer di Room 7 terhadap sistem komunikasi dan perangkat keras, ide **RescueMesh** memiliki keunggulan luar biasa bila dirancang dengan benteng teknis berikut:

```
[KORBAN BENCANA] (Tanpa Pulsa / Tanpa Internet / Tanpa Aplikasi Khusus)
       │  (Buka smartphone biasa, connect ke Wi-Fi terbuka: "SOS-RESCUEMESH")
       ▼
┌────────────────────────────────────────────────────────────────────────┐
│ NODE RESCUEMESH (ESP32-S3 + Semtech SX1262 LoRa 920 MHz)               │
│                                                                        │
│ 1. DNS Spoofing Captive Portal (HTTP Port 80) -> Auto-Pop Up Browser   │
│ 2. Form SOS Web Sangat Ringan: Nama, Cedera, Jumlah Jiwa, Status Trap  │
│ 3. Wi-Fi Promiscuous Sniffer (Deteksi Probe Request HP Korban Pasif)   │
│ 4. Kompresi Payload Biner: Form & Lokasi -> Paket Data 13 Byte Ringkas │
│ 5. Transceiver LoRa Mesh (Flooding Protocol Anti-Collision + CSMA/CA) │
└────────────────────────────────────────────────────────────────────────┘
       │  (Transmisi Radio RF 920 MHz Sub-GHz, Jangkauan 1-3 km Antar-Node)
       ▼
[NODE RELAY PEPOHONAN / RUNTUHAN] (Baterai 18650 + Solar Cell 5V)
       │  (Hop forwarding tanpa server internet)
       ▼
[BASE STATION TIM SAR / POSKO BENCANA]
       │  (USB Serial / Web Dashboard Offline)
       ▼
[PETA GIS LOKASI KORBAN & DAFTAR PRIORITAS CEDERA WAKTU NYATA]
```

### Jawaban Otomatis Terhadap Potensi Cecaran Juri PIMNAS:
1. **Berapa node yang dibuat?** Kita wajib memproduksi **4 Unit Node Fisik** (1 Base Station SAR, 2 Relay Mesh Lapangan, 1 Sniffer/Captive Node). Biaya komponen: 4 x Rp 195.000 = Rp 780.000 (sangat hemat dan aman di bawah pagu Belmawa Rp 6–8 juta).
2. **Bagaimana korban menggunakan jika tidak punya aplikasi?** Nol aplikasi (*Zero-App*). Korban cukup mengaktifkan Wi-Fi, memilih SSID `SOS-RESCUEMESH`, dan halaman darurat otomatis muncul via mekanisme captive portal standar Android/iOS.
3. **Bagaimana jika korban pingsan/tertimbun puing dan tidak bisa mengetik?** Node RescueMesh menjalankan mode *promiscuous Wi-Fi sniffing* yang secara pasif menangkap sinyal *probe request* yang terus dipancarkan smartphone korban di sakunya, membaca MAC Address & RSSI kekuatan sinyal untuk estimasi jarak dan keberadaan korban hidup.
4. **Keandalan Mekanik Enclosure:** Enclosure menggunakan boks tahan cuaca ABS IP65 dengan *gasket seal* silikon, perlindungan antena SMA berpelindung karet, dan pengait karabiner untuk dilempar atau digantung di pohon oleh regu penyelamat.
'''

target_path = r'd:\Belajar\Semester 5\Project\PKM\PKP PKM 2026\INDEX-ANALISIS-PKP2.md'

with open(target_path, 'a', encoding='utf-8') as f:
    f.write(analysis_room7)

print("Successfully written Room 7 analysis to INDEX-ANALISIS-PKP2.md")
