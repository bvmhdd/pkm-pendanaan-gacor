# PEDISCAN-BIS (Diabetic Foot Bio-Impedance Spectroscopy)
## Rencana Implementasi Terperinci (Implementation Plan) — PKM-Karsa Cipta 2027
**Judul Usulan:**  
*PEDISCAN-BIS: Rancang Bangun Spektrometer Bio-Impedansi Tetrapolar Portabel Berbasis Model Cole-Cole dan TinyML untuk Skrining Dini Iskemia Mikrovaskular dan Edema Subkutan Kaki Diabetik*

**Target Skema:** PKM-Karsa Cipta (PKM-KC) 2027 — Kemendiktisaintek / Belmawa  
**Pagu Anggaran:** Rp 7.850.000 (Maksimal Belmawa) + Rp 1.500.000 (Co-Funding Perguruan Tinggi) = **Rp 9.350.000**  
**Durasi Pelaksanaan:** 4 Bulan (16 Minggu Efektif)  
**Status Evaluasi:** `ANTI-MAINSTREAM & ZERO-SATURATION` (Belum ada prototipe kompetitor di PKM terdahulu)

---

## 1. Urgensi Medis & Masalah Kritis Nasional (Background & Urgency)

### 1.1 Epidemiologi & Fakta Klinis
* **Beban Penyakit Nasional:** Berdasarkan data Federasi Diabetes Internasional (IDF) dan Kemenkes RI, Indonesia menempati **peringkat ke-5 dunia** dengan **19,5 juta penderita diabetes melitus**.
* **Komplikasi Ulkus Kaki Diabetik (Diabetic Foot Ulcer / DFU):**
  * Sekitar 1 dari 6 penderita diabetes (15–25%) akan mengalami ulkus borok kaki kronis selama hidupnya.
  * **85% kasus amputasi kaki** pada penderita diabetes diawali oleh luka ulkus yang tidak tertangani.
  * Tingkat mortalitas 5 tahun setelah amputasi mencapai 50–70% (lebih mematikan dibandingkan beberapa jenis kanker).
* **Celah Diagnostik di Faskes Tingkat Pertama (Puskesmas / Posbindu):**
  * Standar skrining saat ini di Puskesmas hanya menggunakan **uji sentuh monofilamen Semmes-Weinstein (benang nilon 10 gram)**. Uji ini bersifat kasar dan **hanya mendeteksi neuropati perifer sensorik setelah serabut saraf mati**, bukan gangguan sirkulasi mikrovaskular dini.
  * Pemeriksaan vaskular standar emas (*Ankle-Brachial Index / ABI* dengan Doppler USG atau angiografi) membutuhkan operator terlatih dan alat mahal yang hanya ada di Rumah Sakit Tipe A/B.
  * **Jurang Kritis:** Saat ini **tidak ada instrumen genggam terjangkau** yang mampu mendeteksi penurunan perfusi darah mikrovaskular (iskemia) dan penumpukan cairan jaringan mikro (edema intraseluler/ekstraseluler) **2–4 minggu SEBELUM kulit pecah menjadi luka terbuka**.

---

## 2. Landasan Sains & Biofisika: Teori Model Cole-Cole

```
                                          R_e (Fluida Ekstraseluler)
                                  +----------------/\/\/\/\----------------+
                                  |                                        |
                 Arus Injeksi     |          C_m (Membran Sel)             |    Arus Keluar
              --------------------+---->---||---+---/\/\/\/\---+---------->+-----------------
                 (I_ex AC)        |             |              |           |     (I_out)
                                  +-------------+    R_i       +-----------+
                                                (Fluida Intraseluler)
```

### 2.1 Dispersi Dielektrik Jaringan Biologis
Jaringan biologis kulit dan subkutan kaki manusia terdiri dari sel-sel yang tersuspensi dalam cairan elektrolit:
1. **Fluida Ekstraseluler (ECF):** Bersifat murni resistif ($R_e$).
2. **Membran Sel Ganda Lipid (Cell Membrane):** Bersifat isolator tipis yang bertindak sebagai kapasitor biologis ($C_m$) dengan elemen fase konstan (*Constant Phase Element / CPE*).
3. **Fluida Intraseluler (ICF):** Terletak di dalam sel, bersifat resistif ($R_i$).

### 2.2 Fenomena Spektroskopi Multi-Frekuensi (MF-BIS)
* **Pada Frekuensi Rendah ($f < 10\text{ kHz}$):**
  Impedansi kapasitansi membran sel ($X_c = \frac{1}{2\pi f C_m}$) bernilai sangat tinggi. Arus listrik bolak-balik **terblokir** dan tidak dapat menembus ke dalam sel. Arus murni mengalir melalui jalur resistansi ekstraseluler ($R_0 \approx R_e$).
* **Pada Frekuensi Tinggi ($f > 100\text{--}200\text{ kHz}$):**
  Impedansi kapasitif membran sel mengecil mendekati hubung singkat ($X_c \to 0$). Arus mampu menembus membran lipid dan mengalir melintasi fluida intraseluler dan ekstraseluler secara paralel ($R_\infty = \frac{R_e R_i}{R_e + R_i}$).

### 2.3 Persamaan Matematis Cole-Cole
Respon impedansi kompleks $Z(\omega)$ terhadap frekuensi sudut $\omega = 2\pi f$ dimodelkan secara analitik:
$$Z(\omega) = R_\infty + \frac{R_0 - R_\infty}{1 + (j\omega \tau)^\alpha}$$

Di mana:
* $R_0$: Resistansi pada frekuensi nol/rendah (indikator volume cairan ekstraseluler).
* $R_\infty$: Resistansi pada frekuensi tak hingga (indikator volume cairan total tubuh).
* $\tau$: Konstanta waktu relaksasi jaringan ($\tau = \frac{1}{2\pi f_c}$, dengan $f_c$ adalah frekuensi relaksasi karakteristik).
* $\alpha$: Parameter heterogenitas struktural jaringan ($0 \le \alpha \le 1$, bernilai $\sim 0.7\text{--}0.8$ pada jaringan sehat).
* **Phase Angle ($\text{PhA}$ pada 50 kHz):**
  $$\text{PhA} = \arctan\left(\frac{X_c}{R}\right) \times \frac{180^\circ}{\pi}$$
  Sudut fase mencerminkan integritas dan polaritas membran sel. Penurunan $\text{PhA} < 5^\circ$ pada area plantar kaki merupakan prediktor klinis kuat terjadinya kerusakan jaringan iskemik dan kematian sel subkutan.

---

## 3. Arsitektur Enjiniring & Perangkat Keras (Hardware Architecture)

```
       +---------------------------------------------------------------------------------+
       |                              PASIEN KAKI DIABETIK                               |
       |                (Area Plantar: Metatarsal 1, Metatarsal 5, dan Tumit)            |
       +---------------------------------------------------------------------------------+
                 ^                    ^                                ^             ^
                 | (I+)               | (V+)                           | (V-)        | (I-)
                 |                    |                                |             |
       +---------+--------------------+--------------------------------+-------------+---+
       |       PROBE TETRAPOLAR 4-TITIK KELVIN (Pegas Pogo-Pin Berlapis Emas 24K)        |
       +---------------------------------------------------------------------------------+
                 ^                    |                                |             |
                 |                    +----------------+---------------+             |
                 |                                     |                             |
       +---------+-----------+                         v                             |
       |  ENHANCED HOWLAND   |               +--------------------+                  |
       |  CURRENT PUMP (VCCS)|               | DIFFERENTIAL BIO-  |                  |
       |  - Arus Konstan AC  |               | INSTRUMENTATION AMP|                  |
       |  - I_ex < 100 uA    |               | - AD8226 (CMRR>100)|                  |
       |  - Patuh IEC 60601-1|               | - High Input Z     |                  |
       +---------------------+               +--------------------+                  |
                 ^                                     |                             |
                 | Sinusoid Excitation                 v                             |
       +---------+-------------------------------------+-----------------------------+---+
       |                 ANALOG DEVICES AD5933 (12-bit, 1 MSPS Impedance AFE)             |
       |  - Direct Digital Synthesizer (DDS): Frequency Sweep 5 kHz s.d. 100 kHz         |
       |  - On-Chip Discrete Fourier Transform (DFT) Engine: Ekstraksi Real & Imag       |
       +---------------------------------------------------------------------------------+
                                               |
                                               | I2C Bus Terisolasi (ADuM1250)
                                               v
       +---------------------------------------------------------------------------------+
       |                  ESP32-S3 DUAL-CORE MICROCONTROLLER (240 MHz)                   |
       |  - FreeRTOS Core 0: Driver AD5933, Sweep Sequencer & Proteksi Pasien            |
       |  - FreeRTOS Core 1: Algoritma Non-Linear Cole-Cole Fit & TinyML Classifier      |
       |  - NVS Memory: Kalibrasi Sirkuit Phantom RC Standar                             |
       +---------------------------------------------------------------------------------+
                 |                                                     |
                 v                                                     v
       +--------------------+                                +--------------------+
       |  OLED DISPLAY 1.3" |                                | TELEMETRI NIRKABEL |
       |  - Grafik Cole-Cole|                                | - BLE 5.0 (App HP) |
       |  - Skor Risiko DFU |                                | - LoRa 920-923 MHz |
       +--------------------+                                +--------------------+
```

### 3.1 Sub-sistem Analog Front-End (AFE) Tetrapolar Kelvin
* **Mengapa Wajib Tetrapolar (4-Elektroda)?**
  Metode bipolar (2 elektroda) gagal total pada bioimpedansi kulit karena resistansi kontak stratum korneum keringat dan elektroda ($Z_{contact} \approx 10\text{--}100\ \text{k}\Omega$) jauh lebih besar daripada impedansi jaringan subkutan yang ingin diukur ($Z_{tissue} \approx 50\text{--}500\ \Omega$).
  * **2 Elektroda Luar ($I_+, I_-$):** Menginjeksikan arus AC mikro presisi.
  * **2 Elektroda Dalam ($V_+, V_-$):** Mengukur penurunan tegangan melintasi jaringan dengan penguat diferensial berimpedansi input Tera-Ohm ($>10^{12}\ \Omega$), sehingga arus yang masuk ke sensor tegangan praktis nol dan efek resistansi kontak tereliminasi 100%.
* **Patient Safety Compliant (IEC 60601-1):**
  Menggunakan sirkuit *Enhanced Howland Current Pump* berbasis op-amp ganda berderau ultra-rendah (OPA2140 / AD8606) yang membatasi arus injeksi konstan pada **$< 100\ \mu\text{A}$ RMS**, aman dari bahaya sengatan listrik mikro dan tidak dirasakan oleh pasien (*imperceptible*).
* **Isolasi Galvanik:** Bus komunikasi I2C dipisahkan menggunakan isolator digital iCoupler **ADuM1250** dan konverter DC-DC terisolasi medis (B0505S-1WR3) untuk mencegah ground loop dan kebocoran arus listrik ke tubuh pasien.

### 3.2 Mesin Spektroskopi AD5933
* IC terintegrasi beresolusi 12-bit dengan on-chip Direct Digital Synthesizer (DDS) yang membangkitkan frekuensi sweep dari 5 kHz hingga 100 kHz (dapat diekstensi hingga 200 kHz).
* Dilengkapi mesin Discrete Fourier Transform (DFT) internal yang langsung mengeluarkan nilai komponen riil ($R$) dan imajiner ($X_c$) pada setiap titik frekuensi melalui antarmuka $I^2C$.

### 3.3 Pemrosesan Sinyal & TinyML On-Device (ESP32-S3)
1. **Algoritma Cole-Cole Circle Fitting:**
   Data impedansi $(R, X_c)$ di setiap frekuensi dipetakan ke dalam bidang kompleks (*Nyquist plot*). ESP32-S3 menjalankan algoritma regresi lingkaran kuadrat terkecil non-linier (*Non-Linear Least Squares Circle Fit*) untuk mengekstraksi 4 parameter kunci: $R_0$, $R_\infty$, $f_c$, dan $\alpha$.
2. **Kategori Output Risiko Iskemia Kaki Diabetik:**
   * **Zona Hijau (Normal Tissue):** $\text{PhA} \ge 6.5^\circ$, $R_0/R_\infty \approx 1.3\text{--}1.5$, integritas membran sel utuh.
   * **Zona Kuning (Subclinical Edema / Mild Ischemia):** $\text{PhA } 5.0^\circ\text{--}6.4^\circ$, penurunan $R_0$ akibat retensi cairan ekstraseluler subkutan.
   * **Zona Merah (Severe Ischemic Pre-Ulcerative Risk):** $\text{PhA} < 5.0^\circ$, rasio $R_0/R_\infty \to 1.0$, menandakan depolarisasi membran sel masif dan nekrosis jaringan mikrovaskular yang membutuhkan intervensi medis segera.

---

## 4. Pembagian Peran Anggota Tim (Merujuk USER.md & Portofolio)

| Nama Anggota | Program Studi / Keahlian | Peran Fungsional di PEDISCAN-BIS | Tanggung Jawab Teknis Spesifik |
|---|---|---|---|
| **Muhammad Muhibbin** | S1 Teknik Elektro (Hardware & Analog) | **Ketua Tim / Hardware Lead** | • Desain skematik & layout PCB 4-layer AFE bioimpedansi.<br>• Implementasi *Enhanced Howland Current Pump* ($<100\ \mu\text{A}$ RMS) & kepatuhan standar isolasi IEC 60601-1.<br>• Pemrograman driver I2C AD5933 dan kalibrasi sirkuit phantom RC.<br>• Sistem manajemen daya baterai LiFePO4 3.2V dengan proteksi BMS. |
| **Sahra Raditiya Fadillah** | S1 Teknik Telekomunikasi (RF & Jaringan) | **Anggota 1 / RF & Enclosure Lead** | • Integrasi modul telemetri nirkabel BLE 5.0 & LoRa (920–923 MHz Kominfo).<br>• Desain mekanik probe 4-pin pogo berlapis emas 24K dengan pegas suspensi seragam.<br>• Fabrikasi housing genggam ergonomis berbasis 3D printing resin biocompatible.<br>• Protokol transmisi tele-podiatri data impedansi ke dashboard faskes/Puskesmas. |
| **Syahbudin Hamzah Hasan** | S1 Informatika / CS (Software & AI) | **Anggota 2 / Edge AI & Firmware Lead** | • Pemrograman algoritma non-linear Cole-Cole circle fitting pada ESP32-S3.<br>• Pengembangan model inferensi TinyML INT8 untuk klasifikasi tingkat keparahan iskemia.<br>• Desain User Interface pada layar OLED 1.3" dan aplikasi pendamping Android (Flutter).<br>• Pengujian akurasi fitting ($R^2 > 0.95$) terhadap sirkuit ekivalen kalibrasi. |
| **Endah Setyowati, S.T., M.T.** | Dosen Pembimbing (Teknik Elektro/Telekomunikasi) | **Advisor / Scientific Validator** | • Supervisi metodologi pengukuran bioimpedansi dan integritas sinyal frekuensi tinggi.<br>• Memfasilitasi akses laboratorium kalibrasi instrumentasi (LCR Meter presisi tinggi).<br>• Validasi kepatuhan naskah terhadap pedoman Belmawa dan etika pengujian biomedis. |

---

## 5. Rencana Anggaran Biaya (RAB) Belmawa 2026/2027

Perhitungan anggaran disusun dengan mematuhi **batas pagu dana Belmawa Rp 7.850.000** ditambah **dana pendamping perguruan tinggi Rp 1.500.000** (Total Rp 9.350.000), sesuai persentase akun belanja resmi:

### Rekapitulasi Rencana Anggaran Biaya
| No | Jenis Pengeluaran | Alokasi Dana Belmawa (Rp) | Alokasi Dana PT (Rp) | Total Anggaran (Rp) | Persentase Belmawa |
|---|---|---|---|---|---|
| 1 | Bahan Khusus (maks 60%) | Rp 4.685.000 | Rp 500.000 | Rp 5.185.000 | 59,68% (Valid) |
| 2 | Sewa dan Jasa (maks 15%) | Rp 1.150.000 | Rp 400.000 | Rp 1.550.000 | 14,65% (Valid) |
| 3 | Transportasi Lokal (maks 30%) | Rp 1.050.000 | Rp 300.000 | Rp 1.350.000 | 13,38% (Valid) |
| 4 | Lain-lain (maks 15%) | Rp 965.000 | Rp 300.000 | Rp 1.265.000 | 12,29% (Valid) |
| **TOTAL** | | **Rp 7.850.000** | **Rp 1.500.000** | **Rp 9.350.000** | **100,00%** |

---

### Rincian Detail Belanja Bahan Khusus (Akun 1)
| Komponen / Bahan | Spesifikasi Teknis | Volume | Harga Satuan (Rp) | Total (Rp) | Sumber Dana |
|---|---|---|---|---|---|
| IC Impedance Converter AD5933 | 12-bit, 1 MSPS, I2C, SSOP-16 | 2 pcs | Rp 275.000 | Rp 550.000 | Belmawa |
| Mikrokontroler ESP32-S3 DevKit | Dual-core 240 MHz, 8MB Flash, 2MB PSRAM | 2 unit | Rp 145.000 | Rp 290.000 | Belmawa |
| Precision Dual Op-Amp AFE (AD8606/OPA2140) | Ultra-low noise, low offset, Rail-to-rail | 4 pcs | Rp 95.000 | Rp 380.000 | Belmawa |
| Pogo-Pin Probe Emas 24K Tetrapolar | Spring-loaded, gold plated, tip R1.5 mm | 8 pcs | Rp 45.000 | Rp 360.000 | Belmawa |
| Digital Isolator ADuM1250 | Bidirectional I2C galvanic isolation | 2 pcs | Rp 110.000 | Rp 220.000 | Belmawa |
| Medical DC-DC Converter B0505S-1WR3 | 5V to 5V 1W, 3000 VDC Isolation | 2 pcs | Rp 85.000 | Rp 170.000 | Belmawa |
| Modul Transceiver LoRa Ra-02 (SX1278/SX1262) | 915/920 MHz frequency band Kominfo | 2 unit | Rp 115.000 | Rp 230.000 | Belmawa |
| Layar OLED 1.3 Inch SPI/I2C | Resolusi 128x64 White, Driver SH1106 | 2 unit | Rp 65.000 | Rp 130.000 | Belmawa |
| Baterai LiFePO4 3.2V 3200 mAh & BMS | Cell 26650, siklus >2000x + BMS 1S 5A | 2 set | Rp 165.000 | Rp 330.000 | Belmawa |
| Komponen Pasif Presisi SMD (Resistor 0.1%, Cap NP0) | Resistor metal film 0.1% untuk kalibrasi phantom | 1 lot | Rp 275.000 | Rp 275.000 | Belmawa |
| Filamen 3D Printing Resin Biocompatible | Medical-grade UV resin non-toxic (1 kg) | 1 botol | Rp 450.000 | Rp 450.000 | Belmawa |
| Elektrolit Gel & Elektroda Ag/AgCl Standar | Pack 50 pcs Ag/AgCl disposable sensor ECG/BIS | 2 pack | Rp 150.000 | Rp 300.000 | Belmawa |
| Kabel Koaksial Mikro & Konektor SMA/U.FL | Shielded RG178 low capacitance cable | 4 set | Rp 125.000 | Rp 500.000 | Belmawa |
| Box Akrilik & Fastener Stainless Steel | Enclosure lab station & fixture probe | 1 lot | Rp 500.000 | Rp 500.000 | PT (Co-Funding) |
| **Subtotal Akun 1** | | | | **Rp 5.185.000** | |

---

### Rincian Detail Belanja Sewa dan Jasa (Akun 2)
| Item Sewa / Jasa | Justifikasi / Output | Volume | Harga Satuan (Rp) | Total (Rp) | Sumber Dana |
|---|---|---|---|---|---|
| Jasa Fabrikasi PCB 4-Layer Impedance Control | Fabrikasi PCB JLCPCB/PCBWay ENIG gold-plated | 2 order | Rp 425.000 | Rp 850.000 | Belmawa |
| Sewa LCR Meter Presisi Tinggi (Lab Kampus) | Kalibrasi nilai impedansi standar phantom RC | 3 sesi | Rp 100.000 | Rp 300.000 | Belmawa |
| Jasa Laser Cutting & Pemotongan Akrilik | Dudukan cetakan probe kaki dan fixtures uji | 1 paket | Rp 400.000 | Rp 400.000 | PT (Co-Funding) |
| **Subtotal Akun 2** | | | | **Rp 1.550.000** | |

---

### Rincian Detail Transportasi Lokal (Akun 3)
| Kegiatan Perjalanan | Tujuan / Destinasi | Volume | Biaya (Rp) | Total (Rp) | Sumber Dana |
|---|---|---|---|---|---|
| Pengadaan Komponen Elektronika Khusus | Pasar Elektronika Lokal & Agen Logistik | 3 trip | Rp 150.000 | Rp 450.000 | Belmawa |
| Observasi Lapangan & Wawancara Nakes | Klinik Perawatan Luka Kaki Diabetik / Puskesmas | 4 trip | Rp 150.000 | Rp 600.000 | Belmawa |
| Pengujian Sinyal Transmisi LoRa Lapangan | Pengujian link-budget area padat urban | 2 trip | Rp 150.000 | Rp 300.000 | PT (Co-Funding) |
| **Subtotal Akun 3** | | | | **Rp 1.350.000** | |

---

### Rincian Detail Lain-lain (Akun 4)
| Item Pengeluaran | Justifikasi | Volume | Biaya (Rp) | Total (Rp) | Sumber Dana |
|---|---|---|---|---|---|
| Pendaftaran Akun Google Play Console / Hosting | Deployment dashboard tele-podiatri faskes | 1 paket | Rp 425.000 | Rp 425.000 | Belmawa |
| Logistik Penjilidan, Materai & Dokumen Legalitas | Berkas MoU kemitraan, lembar pengesahan | 1 paket | Rp 240.000 | Rp 240.000 | Belmawa |
| Biaya Publikasi Prosiding / Luaran Ilmiah | Registrasi seminar nasional luaran PKM | 1 artikel | Rp 300.000 | Rp 300.000 | Belmawa |
| Paket Kuota Data IoT & Komunikasi Tim | Sinkronisasi dataset cloud 4 bulan | 3 paket | Rp 100.000 | Rp 300.000 | PT (Co-Funding) |
| **Subtotal Akun 4** | | | | **Rp 1.265.000** | |

---

## 6. Jadwal Kerja 4 Bulan (Gantt Chart 16 Minggu)

```
Aktivitas / Minggu              | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10| M11| M12| M13| M14| M15| M16|
--------------------------------+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
FASE 0: STUDI & PHANTOM DESAIN  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Studi literatur Cole-Cole DFU |████|████|    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Desain sirkuit phantom RC uji |    |████|████|    |    |    |    |    |    |    |    |    |    |    |    |    |
FASE 1: PERANCANGAN SISTEM      |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Skematik AFE Howland & AD5933 |    |    |████|████|    |    |    |    |    |    |    |    |    |    |    |    |
- Desain PCB 4-layer & 3D Probe |    |    |    |████|████|    |    |    |    |    |    |    |    |    |    |    |
- Firmware sweep driver AD5933  |    |    |    |    |████|████|    |    |    |    |    |    |    |    |    |    |
FASE 2: FABRIKASI & INTEGRASI   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Perakitan komponen PCB & AFE  |    |    |    |    |    |████|████|    |    |    |    |    |    |    |    |    |
- Kalibrasi phantom vs LCR Meter|    |    |    |    |    |    |████|████|    |    |    |    |    |    |    |    |
- Integrasi Cole-Cole Fit ESP32 |    |    |    |    |    |    |    |████|████|    |    |    |    |    |    |    |
- Fabrikasi probe pogo & housing|    |    |    |    |    |    |    |    |    |████|████|    |    |    |    |    |
FASE 3: PENGUJIAN & VALIDASI    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Uji stabilitas sweep 5-100 kHz|    |    |    |    |    |    |    |    |    |    |████|████|    |    |    |    |
- Uji relaksasi jaringan in-vivo|    |    |    |    |    |    |    |    |    |    |    |████|████|    |    |    |
- Pengujian telemetri BLE/LoRa  |    |    |    |    |    |    |    |    |    |    |    |    |████|████|    |    |
FASE 4: LAPORAN & LUARAN        |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Penyusunan Laporan Kemajuan   |    |    |    |    |    |    |    |████|    |    |    |    |    |    |    |    |
- Penulisan Draf Paten / HKI    |    |    |    |    |    |    |    |    |    |    |    |    |████|████|    |    |
- Laporan Akhir & Artikel Ilmiah|    |    |    |    |    |    |    |    |    |    |    |    |    |    |████|████|
```

---

## 7. Nilai Kebaruan & Mengapa Ide Ini "Pasti Lolos Pendanaan" (Juri Perspective)

1. **Anti-Saturasi 100%:** Di panggung PKP/PIMNAS selama 5 tahun terakhir, belum pernah ada tim PKM-KC mahasiswa S1 yang mengangkat **Spektroskopi Bio-Impedansi Tetrapolar dengan Model Matematika Cole-Cole untuk Kaki Diabetik**. Topik ini biasanya hanya muncul di level tesis Magister atau jurnal IEEE Transactions on Biomedical Engineering.
2. **Kekuatan Teori Enjiniring (Electrical Engineering Depth):**
   * Reviewer Teknik Elektro akan kagum karena tim tidak sekadar menghubungkan sensor modul pasaran, melainkan merancang **Enhanced Howland Current Pump**, proteksi isolasi **IEC 60601-1**, dan mengeliminasi resistansi kontak kulit menggunakan **metode Kelvin 4-kawat**.
3. **Kekuatan Solusi Masalah Medis (Clinical Relevance):**
   * Reviewer bidang kesehatan/kedokteran sangat memahami betapa putus asanya dokter spesialis penyakit dalam dan perawat luka kaki diabetik karena ketiadaan alat skrining dini sebelum luka borok terbentuk. PEDISCAN-BIS menawarkan solusi preventif nyata untuk menekan angka amputasi kaki di Indonesia.
4. **Visualitas & Demonstrasi Panggung PIMNAS:**
   * Di hadapan dewan juri, prototipe dapat langsung didemonstrasikan: probe ditempelkan ke kaki sukarelawan selama 5 detik, dan kurva setengah lingkaran Cole-Cole (*Nyquist Arc*) langsung terplot secara real-time di layar OLED dan aplikasi smartphone dengan indikator sudut fase yang presisi.
