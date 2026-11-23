# DOSIR LENGKAP DUA OPSI USULAN PROPOSAL PKM-KC 2027
## Dokumen Panduan Diskusi Tim Mahasiswa & Dosen Pendamping (Endah Setyowati S.T., M.T.)

> **Penyusun:**  
> - Muhammad Muhibbin (Ketua Tim — NIM / Teknik Elektro)  
> - Sahra Raditiya Fadillah (Anggota 1 — Pemrosesan Sinyal & TinyML)  
> - Syahbudin Hamzah Hasan (Anggota 2 — Telekomunikasi & Telemetri)  
> **Dosen Pendamping:** Endah Setyowati S.T., M.T.  
> **Pagu Anggaran Optimal:** Rp 7.850.000 (Usulan Belmawa) + Rp 1.500.000 (Dana Pendamping PT) = **Total Rp 9.350.000**

---

## DAFTAR ISI DOSIR
1. **Pengantar & Filosofi Pemilihan Topik** (Mengapa HealthTech & Pola Emas PIMNAS)
2. **BEDAH MENDALAM OPSI 1: LITHOSCAN** (Deteksi Dini Risiko Litogenik Batu Ginjal)
   - 2.1 Identitas & Judul Resmi
   - 2.2 Urgensi Masalah & Kesenjangan Klinis
   - 2.3 Arsitektur Enjiniring & Cara Kerja Alat
   - 2.4 Rencana Anggaran Biaya (RAB) Belmawa Rp 7,85 Juta
   - 2.5 Protokol Uji Laboratorium Bebas Izin Etik Rumah Sakit
   - 2.6 Celah Kelemahan & Strategi Tangkalannya
3. **BEDAH MENDALAM OPSI 2: ASMA-GUARD** (Deteksi Dini Mengi Asma Nokturnal Anak)
   - 3.1 Identitas & Judul Resmi
   - 3.2 Urgensi Masalah & Kesenjangan Klinis
   - 3.3 Arsitektur Enjiniring & Cara Kerja Alat
   - 3.4 Rencana Anggaran Biaya (RAB) Belmawa Rp 7,85 Juta
   - 3.5 Protokol Uji Laboratorium Bebas Izin Etik Rumah Sakit
   - 3.6 Celah Kelemahan & Strategi Tangkalannya
4. **Matriks Perbandingan Head-to-Head (15 Parameter)**
5. **Naskah Pitching 3 Menit Menghadap Dosen Pendamping**

---

# BAGIAN 1: PENGANTAR & FILOSOFI PEMILIHAN TOPIK

Berdasarkan diskusi awal dan arahan tertulis Ibu Endah Setyowati S.T., M.T. melalui tautan percakapan ChatGPT mengenai *HealthTech*, terdapat tiga prinsip utama yang ditekankan:
1. **Sederhana, murah, dan komponen mudah didapat di pasaran domestik.**
2. **Menyelesaikan masalah kesehatan nyata di masyarakat.**
3. **Fungsional, memiliki kebaruan (*novelty*), dan realistis dikerjakan mahasiswa Sistem Telekomunikasi/Elektro.**

Setelah menganalisis arsip juara **Medali Emas PIMNAS ke-37 s.d. PIMNAS ke-39** (seperti *Cardioguard UGM*, *Orside UGM*, dan *ITS TB Suara Batuk*) serta transkrip penilaian kemajuan (PKP) nasional 2026, kedua opsi di dalam dosir ini dirancang untuk memenuhi seluruh kriteria tersebut dengan **anggaran optimal Belmawa Rp 7.850.000** (bebas dari risiko penolakan akibat melebihi plafon atau item belanja satuan $> \text{Rp } 1.000.000$).

---

# BAGIAN 2: BEDAH MENDALAM OPSI 1 (LITHOSCAN)

### 2.1 Identitas & Judul Resmi
- **Nama Inovasi:** LITHOSCAN (Lithogenic Risk Urinalysis Scanner)
- **Judul Proposal:**  
  > **LITHOSCAN: Perangkat Point-of-Care Multi-Wavelength Spectrophotometry dan Nephelometric Turbidimetry Terintegrasi Thermal-Stabilized Chamber dan TinyML untuk Deteksi Dini Risiko Litogenik Batu Ginjal (Nefrolitiasis)**

### 2.2 Urgensi Masalah & Kesenjangan Klinis
- **[FAKTA] Epidemiologi & Angka Kekambuhan:**  
  Penyakit batu ginjal (nefrolitiasis) diderita oleh jutaan masyarakat Indonesia. Pasien yang telah menjalani operasi atau tembak gelombang kejut (ESWL) memiliki risiko kambuh (*recurrence rate*) sebesar **50% dalam rentang waktu 5 tahun**.
- **[FAKTA] Kesenjangan Diagnostik Rumah Sakit:**  
  Alat medis rumah sakit seperti USG Abdomen dan CT Scan baru dapat mendeteksi batu ginjal setelah batu mengeras dan berukuran diameter $> 3\text{--}4 \text{ mm}$ yang kerap kali telah menyumbat saluran kencing (memicu nyeri kolik akut dan pendarahan). Saat ini, **tidak ada alat pemantau mandiri portabel murah** di Puskesmas atau rumah pasien untuk mendeteksi kapan urin kembali memasuki fase pembentukan kristal aktif.
- **[INFERENSI] Jendela Emas Deteksi Dini:**  
  Sebelum batu ginjal membesar, urin selalu melalui fase **supersaturasi kristaluria** (kalsium oksalat $CaC_2O_4$ atau asam urat mikroskopis) dan **mikrohematuria subklinis** (kebocoran eritrosit mikro akibat gesekan kristal pada tubulus ginjal). LITHOSCAN menangkap tanda-tanda biokimiawi ini sebelum batu terbentuk.

### 2.3 Arsitektur Enjiniring & Cara Kerja Alat
LITHOSCAN adalah perangkat genggam (*handheld analyzer*) yang terdiri dari:

```
[SAMPEL URIN SEGAR] (5 ml dimasukkan ke kuvet optik disposabel)
       │
       ▼
┌────────────────────────────────────────────────────────────────────────┐
│ RUANG BACA OPTIK TERMAL (Thermal-Stabilized Chamber 37.0°C ± 0.2°C)    │
│ • Pemanas Film PTC + Termistor NTC + Kontroler PID di ESP32-S3        │
│   (Mengunci suhu urin pada 37°C persis di dalam tubuh manusia,         │
│    mencegah kristalisasi palsu akibat pendinginan di suhu ruang 25°C)  │
├───────────────────────────────────┬────────────────────────────────────┤
│ JALUR TRANSMISI 180°              │ JALUR HAMBURAN 90° (ISO 7027)      │
│ • Sensor Spektrometer 11-Kanal    │ • Emisi Terfokus IR 850 nm         │
│   AMS AS7341 (415 nm s.d. 910 nm) │ • Detektor Fotodioda Hamamatsu     │
│ • Membaca profil serapan kimiawi, │ • Khusus mengukur kepadatan fisik  │
│   hemoglobin darah (555 nm), dan  │   kristal mikro tersuspensi        │
│   proteinuria urin                │   (satuan Nephelometric / NTU)     │
├───────────────────────────────────┴────────────────────────────────────┤
│ ELEKTRODA pH MIKRO ANALISIS                                            │
│ • Mengukur tingkat keasaman urin (pH < 5.5 = Asam Urat, pH > 6.5 = CaOx│
└────────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌────────────────────────────────────────────────────────────────────────┐
│ PEMROSESAN SINYAL & TINYML (ESP32-S3 Dual-Core 240 MHz)                │
│ • Kuantisasi INT8 Model TFLite Micro on-device (Tanpa Butuh Internet)  │
│ • Menghitung Indeks Litogenik Tiselius & Estimasi Konsentrasi (mM)     │
│ • Menampilkan Hasil di Layar OLED 0.96" + Telemetri BLE ke Smartphone  │
└────────────────────────────────────────────────────────────────────────┘
```

**Konsep Bebas Kontaminasi Silang:**  
Sampel urin diletakkan dalam **kuvet plastik polistiren sekali pakai (*disposable cuvette*)** seharga Rp 850/buah. Urin tidak pernah menyentuh sensor optik atau boks alat, sehingga alat 100% steril antar-pengujian (menjawab telak kritik juri PIMNAS terhadap tim alat kesehatan terdahulu).

### 2.4 Rencana Anggaran Biaya (RAB) Belmawa LITHOSCAN (Rp 7.850.000)

| Pos Pengeluaran | Alokasi Belmawa (Rp) | Persentase | Batas Pedoman Belmawa | Status Kepatuhan |
|---|---|---|---|---|
| **1. Bahan Habis Pakai** | Rp 4.550.000 | 57,96% | Maksimal 60% | **PATUH ✅** |
| **2. Sewa dan Jasa** | Rp 1.070.000 | 13,63% | Maksimal 15% | **PATUH ✅** |
| **3. Transportasi Lokal** | Rp 1.530.000 | 19,49% | Maksimal 30% | **PATUH ✅** |
| **4. Lain-lain** | Rp 700.000 | 8,92% | Maksimal 15% | **PATUH ✅** |
| **TOTAL DANA BELMAWA** | **Rp 7.850.000** | **100,00%** | **Rp 6–8 Juta** | **PATUH ✅** |
| *Dana Pendamping PT* | *Rp 1.500.000* | *Kuvet Kuarsa Master & Casing Aluminium CNC* | Maks. Rp 2 Juta | **PATUH ✅** |

*Rincian Komponen Kunci:*  
- 2x ESP32-S3 + 2x Sensor 11-Channel AS7341 + 2x Sensor pH Probe Analog = Rp 1.380.000 (Untuk membuat **2 Unit Prototipe Identik** guna membuktikan reliabilitas antar-alat).
- 400 pcs Kuvet Disposabel Polistiren = Rp 500.000.
- Bahan Kimia Uji Analitik p.a. ($CaCl_2$, $Na_2C_2O_4$, Asam Urat, Buffer NIST) = Rp 850.000.
- Sewa Spektrofotometer UV-Vis Double Beam Lab Riset Kampus (16 Jam @ Rp 50.000) = Rp 800.000.
- Pendaftaran HKI Hak Cipta Firmware di Ditjen KI Kemenkumham = Rp 400.000.

### 2.5 Protokol Uji Laboratorium (Bebas Hambatan Izin Etik Pasien)
- **[FAKTA] Nol Risiko Etik Pasien:** Tim tidak perlu mengurus izin etik (*ethical clearance*) rumah sakit yang memakan waktu berbulan-bulan.
- **Metode Uji di Kampus:** 
  1. Tim melarutkan kalsium klorida ($CaCl_2$) dan natrium oksalat ($Na_2C_2O_4$) di lab kimia kampus dengan konsentrasi bertingkat ($0,2 \text{ mM} - 4,0 \text{ mM}$) untuk membentuk kristal kalsium oksalat sintetis secara terkontrol.
  2. Hasil pembacaan LITHOSCAN dibandingkan langsung dengan **Spektrofotometer UV-Vis Double Beam milik laboratorium kampus**. Target: Nilai korelasi $R^2 \ge 0,95$.
  3. Menguji 50 sampel yang sama pada **Unit 1** dan **Unit 2** untuk membuktikan bahwa pembacaan alat konsisten (*Coefficient of Variation / CV < 3%*).

### 2.6 Celah Kelemahan LITHOSCAN & Solusi Tangkalannya
1. **Celah: Variasi Warna Alami Urin.**  
   *Urin pekat bisa menyerap cahaya dan disangka kristal.*  
   *Solusi:* Menggunakan deteksi nefelometri $90^\circ$ di panjang gelombang inframerah 850 nm yang **kebal warna**, karena molekul warna cairan tidak menyerap cahaya inframerah.
2. **Celah: Kristal Mengendap ke Dasar Kuvet Akibat Gravitasi.**  
   *Solusi:* Firmware mengunci waktu pembacaan otomatis tepat pada detik ke-10 setelah kuvet dimasukkan ke ruang baca.
3. **Celah: Reviewer Menuduh Kristaluria Tidak Selalu Jadi Batu Ginjal.**  
   *Solusi:* Menegaskan posisi LITHOSCAN sebagai pemantau **risiko kekambuhan litogenik pasca-operasi**, dengan skor komposit Tiselius yang memadukan pH, konsentrasi kristal, dan mikrohematuria.

---

# BAGIAN 3: BEDAH MENDALAM OPSI 2 (ASMA-GUARD)

### 3.1 Identitas & Judul Resmi
- **Nama Inovasi:** ASMA-GUARD (Acoustic Tracheal Pediatric Asthma Monitor)
- **Judul Proposal:**  
  > **ASMA-GUARD: Perangkat Wearable Pemantau Akustik Trakea Berbasis Sensor Piezoelektrik PVDF dan TinyML Terintegrasi Bedside Gateway untuk Deteksi Dini Eksaserbasi Asma Nokturnal pada Anak**

### 3.2 Urgensi Masalah & Kesenjangan Klinis
- **[FAKTA] Kematian Asma Malam Hari:**  
  Sekitar **70% kematian asma pada anak** terjadi pada malam hari saat tidur lelap (pukul 02.00–05.00 pagi). Hal ini disebabkan oleh penurunan alami hormon kortisol dan suhu udara malam yang memicu penyempitan saluran napas (*bronchospasm*).
- **[INFERENSI] Keterlambatan Respon Orang Tua:**  
  Anak yang tidur di kamar terpisah tidak mampu berteriak meminta tolong saat sesak napas. Suara mengi (*wheezing*) awal sangat halus dan tertelan oleh hembusan napas, sehingga orang tua baru menyadari saat anak sudah mengalami hipoksia berat atau bibir membiru.
- **[FAKTA] Keselarasan Dosen:**  
  Sangat cocok dengan usulan *Pulmo-Scan* dan *Breath-Alert* yang diberikan Bu Endah dalam tautan percakapan beliau.

### 3.3 Arsitektur Enjiniring & Cara Kerja Alat
ASMA-GUARD terdiri dari dua bagian ekosistem perangkat keras:

```
[LEHER ANAK (TAKIK SUPRASTERNAL)]
       │  (Getaran fisik saluran trakea saat mengi)
       ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 1. WEARABLE TRACHEAL SENSOR NODE (Patch Silikon Medis di Leher)       │
│ • Sensor Film Piezoelektrik Kontak PVDF (TE Connectivity LDT0-028K)    │
│   (Kebal 100% terhadap suara bising udara kamar: kipas angin, AC, TV)  │
│ • Pre-Amp Instrumentasi OPA2350 Ultra Low-Noise                        │
│ • Active Bandpass Filter Butterworth Orde-4 (Cutoff: 100 s.d. 1.800 Hz)│
│ • Automatic Gain Control (AGC) Meredam Noise Gesekan Selimut           │
│ • Mikrokontroler ESP32-S3 (On-Device TinyML: Ekstraksi MFCC + 1D-CNN)   │
└────────────────────────────────────────────────────────────────────────┘
       │  (Transmisi Nirkabel BLE 5.0 & ESP-NOW Jarak 10–15 Meter)
       ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. BEDSIDE GATEWAY DISPLAY (Diletakkan di Meja Kamar Orang Tua)        │
│ • Unit Mandiri Tanpa Bergantung pada Baterai Ponsel Pintar             │
│ • Layar LCD TFT 2.4" Menampilkan Laju Napas & Status Pernapasan Anak   │
│ • Speaker Alarm Keras 85 dB: Berbunyi Instan Saat Wheezing Terdeteksi   │
│   Kontinu > 3 Kali dalam 3 Menit                                       │
└────────────────────────────────────────────────────────────────────────┘
```

### 3.4 Rencana Anggaran Biaya (RAB) Belmawa ASMA-GUARD (Rp 7.850.000)

| Pos Pengeluaran | Alokasi Belmawa (Rp) | Persentase | Batas Pedoman Belmawa | Status Kepatuhan |
|---|---|---|---|---|
| **1. Bahan Habis Pakai** | Rp 4.540.000 | 57,83% | Maksimal 60% | **PATUH ✅** |
| **2. Sewa dan Jasa** | Rp 1.080.000 | 13,76% | Maksimal 15% | **PATUH ✅** |
| **3. Transportasi Lokal** | Rp 1.530.000 | 19,49% | Maksimal 30% | **PATUH ✅** |
| **4. Lain-lain** | Rp 700.000 | 8,92% | Maksimal 15% | **PATUH ✅** |
| **TOTAL DANA BELMAWA** | **Rp 7.850.000** | **100,00%** | **Rp 6–8 Juta** | **PATUH ✅** |
| *Dana Pendamping PT* | *Rp 1.500.000* | *Sound Level Meter Presisi & Boks Akrilik Gateway*| Maks. Rp 2 Juta | **PATUH ✅** |

*Rincian Komponen Kunci:*  
- 3x ESP32-S3 + 4x Sensor Piezo Film PVDF + Op-Amp OPA2350 = Rp 1.195.000 (Untuk merakit **2 Unit Wearable Anak + 1 Unit Bedside Gateway**).
- 1 Unit Layar LCD TFT 2.4" SPI ILI9341 = Rp 125.000.
- Bahan Simulator Trakea Akustik Lab (Tabung Silikon, Kompresor Mini, Nozzle) = Rp 855.000.
- Patch Perekat Medis Hipoalergenik Breathable (100 pcs) = Rp 220.000.
- Sewa Ruang Kedap Suara (*Soundproof Chamber*) Lab Akustik Kampus = Rp 780.000.
- Pendaftaran HKI Hak Cipta Firmware TinyML = Rp 400.000.

### 3.5 Protokol Uji Laboratorium (Bebas Hambatan Izin Etik Pasien)
- **[FAKTA] Nol Risiko Etik Pasien Anak:**  
  Tim tidak melakukan eksperimen medis invasif pada anak-anak penderita asma nyata di awal kegiatan.
- **Metode Uji di Kampus:**
  1. Tim merakit **Simulator Trakea Akustik** di laboratorium elektro menggunakan tabung silikon bertekanan udara variabel.
  2. Suara pernapasan medis resmi dari **ICBHI 2017 Respiratory Sound Database** (database respirasi klinis terbuka berstandar internasional) dipancarkan melalui transduser ke simulator trakea.
  3. Sensor PVDF diuji kemampuannya mendeteksi mengi di tengah simulasi derau kipas angin kamar tidur berintensitas $40\text{--}70\text{ dB}$. Target: Akurasi klasifikasi TinyML $\ge 95\%$ dan latensi alarm $< 2\text{ detik}$.

### 3.6 Celah Kelemahan ASMA-GUARD & Solusi Tangkalannya
1. **Celah: Artefak Gerakan Anak Saat Tidur (Menelan/Menoleh).**  
   *Film PVDF peka terhadap tekukan leher.*  
   *Solusi:* Filter analog aktif High-Pass Orde-4 memotong tuntas semua getaran mekanik leher di bawah 100 Hz, ditambah logika firmware yang mensyaratkan frekuensi mengi stabil selama $> 3\text{ detik}$ agar tidak memicu alarm palsu.
2. **Celah: Anak Risih Menggunakan Patch di Leher.**  
   *Solusi:* Modul dibuat seringan mungkin ($< 15\text{ gram}$) dengan silikon medis lembut melengkung (*ergonomic neck contour*), dilengkapi alarm pengingat jika patch tidak sengaja terlepas (*lead-off alert*).
3. **Celah: Reviewer Menyerang "Database ICBHI Berasal dari Suara Dada, Bukan Trakea".**  
   *Solusi:* Menerapkan *transfer learning* di mana model dasar ICBHI di-fine-tune menggunakan data rekaman getaran simulator trakea fisik piezoelektrik di laboratorium kampus.

---

# BAGIAN 4: MATRIKS PERBANDINGAN HEAD-TO-HEAD

| No | Parameter Perbandingan | OPSI 1: LITHOSCAN (Batu Ginjal) | OPSI 2: ASMA-GUARD (Asma Anak) |
|---|---|---|---|
| 1 | **Objek Sampel** | Cairan urin segar dalam kuvet plastik | Getaran mekanik trakea leher anak |
| 2 | **Sensor Utama** | Spektrometer 11-Kanal AS7341 + Fotodioda | Sensor Kontak Piezo Film PVDF |
| 3 | **Fisika Pengukuran** | Transmisi optik 180° + Hamburan 90° | Akustik kontak + Filter analog aktif bandpass |
| 4 | **Keunikan Suhu** | *Thermal Chamber 37°C PID Controller* | Kompensasi suhu tubuh pasif |
| 5 | **Form Factor** | Alat ukur genggam (*handheld cuvette analyzer*) | Wearable patch leher + Bedside Gateway |
| 6 | **Bebas Kontaminasi Silang** | Sangat Mutlak (Kuvet sekali pakai Rp 850) | Sangat Mutlak (Patch perekat sekali pakai) |
| 7 | **Tingkat Kejenuhan di PIMNAS** | **Sangat Rendah (Anti-Mainstream)** | Sedang (Banyak tema paru, tapi PVDF baru) |
| 8 | **Kemiripan Juara PIMNAS** | Mirip **Orside UGM** & **Nirwana AI UPI** | Mirip **ITS TB Batuk** & **Cardioguard UGM** |
| 9 | **Kesesuaian Arahan Dosen** | Sangat Baik (HealthTech komponen terjangkau)| **100% Identik** (Sesuai ide *Pulmo-Scan*) |
| 10 | **Kemudahan Validasi Lab** | **Sangat Mudah** (Uji kimia garam kalsium) | Sedang (Perlu simulator trakea silikon) |
| 11 | **Kestabilan Sinyal Sensor** | **Sangat Stabil** (Sampel cairan statis) | Perlu filter ketat untuk meredam gerak leher |
| 12 | **Resiko Penolakan Pengguna** | Nol (Pasien tidak dipasangi alat) | Rendah–Sedang (Anak risih memakai patch) |
| 13 | **Pagu Anggaran Belmawa** | Rp 7.850.000 (RAB 4 Pos Patuh 100%) | Rp 7.850.000 (RAB 4 Pos Patuh 100%) |
| 14 | **Jumlah Unit Prototipe** | **2 Unit Fisik** (Field Unit + Lab Station) | **3 Unit Fisik** (2 Patch Anak + 1 Gateway) |
| 15 | **Beban Kerja AI Tim** | Analisis Spektral Multivariat & Tiselius | Ekstraksi Audio MFCC & 1D-CNN Classifier |

---

# BAGIAN 5: NASKAH PITCHING 3 MENIT MENYAMPAIKAN KE IBU ENDAH

*(Dapat dibacakan oleh Muhammad Muhibbin saat berkonsultasi langsung dengan Ibu Endah Setyowati S.T., M.T.)*

> *"Selamat pagi/siang Ibu Endah. Terima kasih banyak atas masukan dan referensi topik HealthTech yang Ibu bagikan kemarin.*
> 
> *Setelah kami pelajari bersama tim, kami merancang dua opsi konkret yang keduanya murni memadukan keahlian Teknik Elektro, Pemrosesan Sinyal/AI, dan Telekomunikasi, dengan anggaran optimal Belmawa sebesar Rp 7,85 juta tanpa melanggar batasan pedoman.*
> 
> *Opsi pertama adalah **LITHOSCAN**, yaitu alat genggam spektrofotometri multi-spektral 11-kanal dan nefelometri untuk deteksi dini risiko kekambuhan batu ginjal melalui urin. Keunggulan utamanya adalah adanya Thermal Chamber 37 derajat Celcius terkontrol PID untuk mencegah kristalisasi dingin palsu, serta kuvet sekali pakai yang bebas kontaminasi silang. Ide ini sangat anti-mainstream dan belum pernah ada di PIMNAS.*
> 
> *Opsi kedua adalah **ASMA-GUARD**, yang 100 persen sejalan dengan rekomendasi Ibu mengenai Pulmo-Scan. Kami merancang patch leher anak berbasis sensor kontak piezoelektrik film PVDF yang kebal dari suara bising kipas atau AC kamar tidur. Begitu terdeteksi suara mengi saat anak tidur lelap, sistem langsung mengirim alarm instan ke Bedside Gateway mandiri di meja kamar orang tua.*
> 
> *Kedua opsi ini sama-sama dapat kami uji tuntas di laboratorium kampus tanpa hambatan izin etik rumah sakit, dan rincian RAB-nya sudah kami hitung sangat rinci. Menurut pandangan Ibu, dari kedua inovasi ini, manakah yang sebaiknya kami kunci sebagai judul proposal resmi PKM-KC tim kami?"*
