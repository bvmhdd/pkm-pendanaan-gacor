# LENTERA MEDIS v2.0 (Tactical Triage Pro)
## Rencana Implementasi Teknis Komprehensif — PKM-Karsa Cipta 2027
**Judul Usulan Resmi:**  
*LENTERA MEDIS v2.0: Gelang Triase Korban Bencana Taktis Berbasis Fusi Sensor Optik-Termal Arteri Radialis, On-Device TinyML Shock Index Predictor, dan Jaringan Hibrida LoRa-Mesh untuk Penentuan Prioritas Evakuasi Massal*

**Target Skema:** PKM-Karsa Cipta (PKM-KC) 2027 — Kemendiktisaintek / Ditjen Belmawa  
**Pagu Anggaran:** Rp 7.850.000 (Maksimal Belmawa) + Rp 1.500.000 (Co-Funding Perguruan Tinggi) = **Rp 9.350.000**  
**Target Luaran Prototipe:** **10 Unit Gelang Taktis Lentera Medis + 1 Unit Tablet Base Station Posko SAR**  
**Durasi Pelaksanaan:** 4 Bulan (16 Minggu Efektif)  
**Status Evaluasi:** `DEEP-TECH UPGRADED & ZERO-SATURATION` (Mengatasi kelemahan vasokonstriksi perifer & mengintegrasikan Edge AI)

---

## 1. Urgensi Bencana & Masalah Kritis Lapangan (The Problem)

### 1.1 Fakta Empiris Kebencanaan Indonesia
* **Kondisi Geografis & Kerentanan Massal:** Indonesia terletak di *Ring of Fire* dengan rata-rata $>1.000$ kejadian bencana alam per tahun (gempa bumi, tsunami, likuifaksi, dan tanah longsor).
* **Ketimpangan Rasio Penolong vs Korban (*Golden Hour Bottleneck*):**
  * Pada fase akut (24 jam pertama bencana massal), rasio tenaga medis terlatih dibanding korban sering kali mencapai **1 dokter berbanding 100+ korban** (BNPB & Kemenkes RI).
  * Keterlambatan evakuasi korban kritis (*Immediate / Red Tag*) selama $>60\text{ menit}$ meningkatkan angka kematian akibat syok hipovolemik hingga **>50%**.
* **Kelemahan Fatal Triase Konvensional (Pita START Kertas):**
  1. **Statis:** Pita triase kertas tidak dapat berubah warna sendiri ketika korban yang awalnya berstatus Kuning (*Delayed*) mengalami perburukan menjadi Merah (*Immediate*) akibat pendarahan internal tersembunyi.
  2. **Buta Malam & Reruntuhan:** Pada malam hari tanpa penerangan listrik atau di bawah puing gelap, pita kertas tidak terlihat. Relawan SAR harus mendekat satu per satu dan menyinari korban dengan senter.
  3. **Waktu Pemeriksaan Lambat:** Memeriksa nadi radialis manual dan menghitung napas memakan waktu 1–3 menit per korban.

---

## 2. Landasan Sains Biomedis & Biofisika Pengukuran

```
                                      Pulsatile Arterial Blood (AC)
                             +-----------------------------------------------+
                             |                                               |
         Radiasi LED Red/IR  |          Non-Pulsatile Tissue & Venous (DC)   |   Sinyal Fotodioda
       ---------------------->----+----------------------------------------->+--------------------->
                                  |                                          |   I_photo = DC + AC
                                  +------------------------------------------+
```

### 2.1 Pemecahan Masalah Vasokonstriksi Perifer (*Anti-Vasoconstriction Sensing*)
* **Mekanisme Syok Hipovolemik:** Saat korban mengalami pendarahan hebat atau hipotermia, sistem saraf simpatis memicu **vasokonstriksi perifer ekstrem** (pembuluh darah kapiler di ujung kuku/jari menciut total untuk mengalirkan darah ke organ vital).
* **Mengapa Sensor Klip Jari Konvensional Gagal?**
  Pulse oximeter klip jari biasa kehilangan sinyal pulsatile secara drastis saat syok ($AC \approx 0$), memicu pembacaan *error* atau salah mengira korban telah meninggal dunia.
* **Solusi Enjiniring LENTERA MEDIS v2.0:**
  1. **Pengukuran pada Arteri Radialis (Pergelangan Dalam):** Sensor optik reflektansi diletakkan langsung di bagian dasar gelang yang menekan lembut arteri radialis pergelangan tangan (aliran darah arteri utama, bukan kapiler perifer).
  2. **Kalkulasi Perfusion Index (PI):** Firmware mengekstrak rasio amplitudo gelombang:
     $$PI = \left(\frac{AC_{\text{pulsatile}}}{DC_{\text{baseline}}}\right) \times 100\%$$
     * $PI \ge 1.5\%$: Perfusi jaringan normal.
     * $0.4\% \le PI < 1.5\%$: Vasokonstriksi ringan hingga sedang.
     * $PI < 0.4\%$: **Syok Hipovolemik Berat** (Algoritma langsung memicu status MERAH Kritis, meskipun denyut nadi masih terbaca lemah).

### 2.2 Termoregulasi: Gradien Suhu Kulit-Lingkungan ($\Delta T$)
Sensor NTC termistor medis membaca suhu kulit pergelangan ($T_{\text{skin}}$), dikoreksi terhadap suhu udara sekitar ($T_{\text{ambient}}$) melalui sensor termal sekunder:
$$\Delta T = T_{\text{skin}} - T_{\text{ambient}}$$
Penurunan $T_{\text{skin}} < 35.0^\circ\text{C}$ dengan gradien $\Delta T$ yang menyempit mengonfirmasi terjadinya hipotermia aksidental atau kolaps kardiovaskular.

---

## 3. Arsitektur Perangkat Keras (Hardware Architecture)

```
        +---------------------------------------------------------------------------------+
        |                               KORBAN BENCANA MASSAL                             |
        |              (Pergelangan Tangan: Arteri Radialis & Kontak Termal Kulit)        |
        +---------------------------------------------------------------------------------+
                  |                                                      |
                  | Denyut Arteri (Reflektansi)                          | Suhu Kulit Konduktif
                  v                                                      v
        +------------------------------+                       +------------------------------+
        |  DUAL-WAVELENGTH REFLECTANCE |                       |     MEDIS NTC THERMISTOR     |
        |  OPTICAL SENSOR (660/880 nm) |                       |     (Akurasi +/- 0.1°C)      |
        |  - Arteri Radialis Wrist     |                       |  - Kontak Langsung Epidermis |
        |  - Anti-Vasokonstriksi       |                       |  - Deteksi Syok/Hipotermia   |
        +------------------------------+                       +------------------------------+
                  |                                                      |
                  +-------------------------------+----------------------+
                                                  |
                                                  v
        +---------------------------------------------------------------------------------+
        |                    ANALOG FRONT-END & FILTER AKTIF (AFE)                        |
        |  - Transimpedance Amp (TIA) + Active Bandpass Filter (0.5 Hz - 5.0 Hz)          |
        |  - Pemisahan Komponen DC & AC untuk Ekstraksi Perfusion Index (PI)              |
        +---------------------------------------------------------------------------------+
                                                  |
                                                  v
        +---------------------------------------------------------------------------------+
        |                  ESP32-S3 / ESP32-C3 SYSTEM-ON-CHIP (160/240 MHz)               |
        |  - Core 0: Akuisisi Sinyal 100 Hz, FFT Denyut, & Dynamic Power Management       |
        |  - Core 1: Model On-Device TinyML Shock & Triage Prediction (INT8 Quantized)    |
        |  - Ambient Light Sensor (ALS): Mengatur Kecerahan LED Sesuai Kegelapan Medan    |
        +---------------------------------------------------------------------------------+
                  |                                                      |
                  | Output Visual Lapangan                               | Output Radio Telemetri
                  v                                                      v
        +------------------------------+                       +------------------------------+
        |   KUBAH DOME 360° DIFUSI     |                       |   HIBRIDA RADIO DUAL-BAND    |
        |  - 6x High-Power RGB LED     |                       |  - ESP-NOW 2.4 GHz (Klaster) |
        |  - Hijau/Kuning/Merah/SOS    |                       |  - LoRa 920-923 MHz (Backbone|
        |  - Jarak Pandang 25-30 Meter |                       |    Tembus Puing Radius 2 km) |
        +------------------------------+                       +------------------------------+
                                                                         |
                                                                         v
                                                               +--------------------+
                                                               | TABLET POSKO MEDIS |
                                                               | - Dashboard BNPB   |
                                                               | - Peta Korban Real |
                                                               +--------------------+
```

### 3.1 Sub-sistem Kubah Optik 360° (*Adaptive Dome Diffuser*)
* **Optik Lapangan 360 Derajat:** Menggunakan kubah polikarbonat berkabut (*frosted optical dome*) dengan 6 buah LED RGB SMD 5050 yang disusun melingkar di bawah lensa kubah. Cahaya terbiaskan merata ke seluruh arah mata angin tanpa titik buta (*zero blind-spot*).
* **Modulasi Daya Adaptif (ALS):** Dilengkapi sensor fototransistor ambient light:
  * Siang hari / Ruang Terang: LED beroperasi pada *duty cycle* 25% (menghemat daya baterai hingga tahan $\ge 24\text{ jam}$).
  * Malam hari / Puing Gelap: LED beralih otomatis ke *burst strobing* 100% (terlihat jelas dari jarak **25–30 meter**).
* **Pola Visual Sesuai Protokol Triase Internasional (START):**
  * 🟢 **HIJAU (Minor):** Berkedip lambat ($0.5\text{ Hz}$). Korban sadar dan stabil.
  * 🟡 **KUNING (Delayed):** Menyala konstan stabil. Korban membutuhkan perawatan lanjutan, namun tanda vital masih kompensasi.
  * 🔴 **MERAH (Immediate):** Berkedip cepat gawat darurat ($2\text{ Hz}$). Korban mengalami syok hipovolemik, hipoksia, atau bradikardia/takikardia parah.
  * ⚪ **STROBE PUTIH (Drone Rescue Ping):** Kedipan pulsa tinggi khusus yang dapat dideteksi kamera optik drone pencari dari udara.

### 3.2 Sub-sistem Jaringan Hibrida Nirkabel (ESP-NOW + Sub-GHz LoRa Mesh)
* **ESP-NOW (2.4 GHz, Zero-Handshake):** Setiap gelang saling bertukar paket status dengan gelang lain dalam radius 50–100 meter, membentuk *ad-hoc local cluster*.
* **LoRa SX1262 (920–923 MHz Standar Kominfo):** Node gelang yang berada paling dekat dengan permukaan tanah bertindak sebagai *relay bridge* yang memancarkan sinyal agregat menembus puing reruntuhan beton hingga **jarak 2 kilometer** menuju Tenda Medis Lapangan BNPB.
* **Protokol Paket Taktis (8-Byte Compact Payload):**
  `[Device_ID (2B) | Status_Triage (1B) | HR (1B) | SpO2 (1B) | Temp (1B) | PI (1B) | Checksum (1B)]`

---

## 4. Arsitektur On-Device TinyML (Shock & Deterioration Predictor)

Alih-alih rumus `IF-ELSE` statis biasa, LENTERA MEDIS v2.0 menggunakan model kecerdasan buatan tertanam:

```
Input Sinyal Mentah (100 Hz)
  ├── Denyut PPG Radialis  ──> [Bandpass Filter 0.5-5Hz] ──> Ekstraksi: HR & Pulse Variability
  ├── Amplitudo AC/DC      ──> [Kalkulasi Envelope]      ──> Ekstraksi: Perfusion Index (PI)
  ├── Suhu Kulit Perifer   ──> [Kalman Filter Termal]    ──> Ekstraksi: T_skin & Gradien Delta-T
  └── Rasio Red/IR         ──> [R-Curve Lookup]          ──> Ekstraksi: SpO2 (%)
                                                                     |
                                                                     v
                                                   Vektor Fitur Input (6 Dimensi):
                                                   x = [HR, SpO2, T_skin, PI, Delta-T, HRV_proxy]
                                                                     |
                                                                     v
                                                   +------------------------------------+
                                                   | MODEL TinyML INT8 (1D-CNN / FCNN)  |
                                                   | - Input Layer: 6 Node              |
                                                   | - Hidden Layer 1: 16 Node (ReLU)   |
                                                   | - Hidden Layer 2: 8 Node (ReLU)    |
                                                   | - Output Layer: 4 Kelas (Softmax)  |
                                                   +------------------------------------+
                                                                     |
                                                                     v
                                                   Status Prediktif Triase:
                                                   [HIJAU | KUNING | MERAH | DETERIORATION_ALERT]
```

### Keunggulan Fitur *Dynamic Deterioration Alert*:
Model mampu mendeteksi penurunan kondisi yang sedang berlangsung (*ongoing shock progression*):
Jika korban saat ini memiliki tanda vital dalam batas Kuning, namun parameter $PI$ turun dengan kemiringan $\frac{d(PI)}{dt} < -0.1\%/\text{menit}$ dan denyut nadi meningkat progresif, gelang akan langsung menyalakan **Lampu Merah Berkedip Ganda**, memperingatkan relawan bahwa pasien ini akan kolaps dalam 15 menit jika tidak segera diinfus/dievaluasi!

---

## 5. Pembagian Peran Tim (5 Mahasiswa + 1 Dosen Pembimbing)

Sesuai susunan pada *PITCH-DECK-LENTERAMEDIS.md*, tim beranggotakan 5 mahasiswa dengan kompetensi terdistribusi secara presisi:

| No | Nama Anggota | Program Studi / Bidang | Peran Fungsional di Tim | Tanggung Jawab Teknis Spesifik |
|---|---|---|---|---|
| **1** | **Muhammad Muhibbin** | S1 Teknik Elektro | **Ketua Tim / Hardware Lead** | • Desain layout PCB 2-layer ultra-kompak untuk 10 unit gelang.<br>• Perancangan AFE sensor optik arteri radialis dan filtering analog.<br>• Manajemen daya efisiensi tinggi baterai Li-Po 500 mAh & proteksi overcharge.<br>• Integrasi switching daya kubah 6x LED RGB SMD 5050. |
| **2** | **Sahra Raditiya Fadillah** | S1 Teknik Telekomunikasi | **Anggota 1 / RF & Mesh Lead** | • Implementasi protokol hibrida ESP-NOW dan LoRa Sub-GHz (920–923 MHz).<br>• Desain antena PCB miniatur untuk transmisi tembus puing reruntuhan.<br>• Pengujian Packet Delivery Ratio (PDR) dan jangkauan telemetri ke Posko SAR.<br>• Alokasi slot transmisi TDMA anti-tabrakan untuk 10 node gelang. |
| **3** | **Syahbudin Hamzah Hasan** | S1 Informatika / CS | **Anggota 2 / Edge AI & Firmware Lead** | • Pengembangan model TinyML INT8 Shock Index Predictor (TFLite Micro).<br>• Pemrograman firmware FreeRTOS dual-core pada ESP32-S3/C3.<br>• Algoritma ekstraksi Perfusion Index (PI) dan pemfilteran derau gerak (*motion artifact*).<br>• Integrasi layar OLED mikro monokrom samping. |
| **4** | **Abyan Fauzan** | S1 Informatika / CS | **Anggota 3 / Dashboard & Telemetry Lead** | • Pengembangan aplikasi Android / Web Dashboard Posko SAR BNPB.<br>• Pemetaan visual real-time status 10 korban di layar tablet posko.<br>• Sistem audio alarm posko saat ada korban beralih ke status Merah Kritis.<br>• Integrasi ekspor log data medis triase untuk rekam medis darurat. |
| **5** | **Rafly** | S1 Teknik Mesin / Industri | **Anggota 4 / Mechanical & Field Testing Lead** | • Desain housing silikon unibody IP67 tahan air, debu, dan benturan.<br>• Fabrikasi lensa kubah difusi optik 360° menggunakan 3D print resin transparan berkabut.<br>• Desain sistem tali *one-way tactical ratchet* ergonomis.<br>• Koordinasi skenario uji simulasi triase lapangan bersama relawan/SAR. |
| **6** | **Endah Setyowati, S.T., M.T.** | Dosen Pembimbing | **Advisor / Technical Validator** | • Supervisi kepatuhan frekuensi radio terhadap regulasi Kominfo.<br>• Validasi protokol pengujian instrumentasi dan etika biomedis.<br>• Bimbingan penyusunan narasi proposal, laporan kemajuan, dan strategi PIMNAS. |

---

## 6. Rencana Anggaran Biaya (RAB) Belmawa 2026/2027

Anggaran dirancang presisi untuk memproduksi **10 Unit Gelang Taktis + 1 Unit Tablet Base Station Receiver**, dengan pagu maksimal Belmawa **Rp 7.850.000** ditambah dana pendamping PT **Rp 1.500.000** (Total Rp 9.350.000):

### Rekapitulasi Rencana Anggaran Biaya
| No | Jenis Pengeluaran | Alokasi Belmawa (Rp) | Alokasi PT (Rp) | Total Anggaran (Rp) | Persentase Belmawa |
|---|---|---|---|---|---|
| 1 | Bahan Khusus (maks 60%) | Rp 4.690.000 | Rp 500.000 | Rp 5.190.000 | 59,75% (Valid) |
| 2 | Sewa dan Jasa (maks 15%) | Rp 1.150.000 | Rp 400.000 | Rp 1.550.000 | 14,65% (Valid) |
| 3 | Transportasi Lokal (maks 30%) | Rp 1.050.000 | Rp 300.000 | Rp 1.350.000 | 13,38% (Valid) |
| 4 | Lain-lain (maks 15%) | Rp 960.000 | Rp 300.000 | Rp 1.260.000 | 12,22% (Valid) |
| **TOTAL** | | **Rp 7.850.000** | **Rp 1.500.000** | **Rp 9.350.000** | **100,00%** |

---

### Rincian Detail Belanja Bahan Khusus (Akun 1 — 10 Gelang + 1 Base Station)
| Komponen / Bahan | Spesifikasi Teknis | Volume | Harga Satuan (Rp) | Total (Rp) | Sumber Dana |
|---|---|---|---|---|---|
| Mikrokontroler Node ESP32-C3 / S3 Mini | 32-bit RISC-V/Xtensa, Wi-Fi, BLE, ultra-low power | 11 unit | Rp 95.000 | Rp 1.045.000 | Belmawa |
| Modul Transceiver LoRa SX1262 (915/920 MHz) | Transceiver Sub-GHz tembus reruntuhan, SPI | 5 unit | Rp 115.000 | Rp 575.000 | Belmawa |
| Sensor Optik Reflektansi PPG Radialis | Dual-Wavelength Red/IR + Low Noise TIA AFE | 10 unit | Rp 85.000 | Rp 850.000 | Belmawa |
| Termistor Medis NTC Epoksi 10k | Akurasi $\pm 0.1^\circ\text{C}$ kontak kulit | 10 unit | Rp 35.000 | Rp 350.000 | Belmawa |
| High-Power RGB SMD LED 5050 | Ultra-bright untuk kubah 360° | 10 set | Rp 25.000 | Rp 250.000 | Belmawa |
| Layar OLED Mikro Monokrom 0.91" I2C | Tampilan telemetri darurat pergelangan | 5 unit | Rp 45.000 | Rp 225.000 | Belmawa |
| Baterai Li-Po 3.7V 500 mAh + Protection IC | Cell rechargeable 500 mAh tahan $>24\text{ jam}$ | 10 unit | Rp 45.000 | Rp 450.000 | Belmawa |
| Filamen Resin 3D Print UV Transparan Berkabut | Material kubah difusi optik 360° (500 gr) | 1 botol | Rp 385.000 | Rp 385.000 | Belmawa |
| Bahan Silikon Taktis Safety Orange & Strap | Silikon medis elastis unibody IP67 | 1 lot | Rp 560.000 | Rp 560.000 | Belmawa |
| Tablet Android Receiver Posko SAR (Refurb/Second) | Layar 8 inci untuk display dashboard base station | 1 unit | Rp 500.000 | Rp 500.000 | PT (Co-Funding) |
| **Subtotal Akun 1** | | | | **Rp 5.190.000** | |

---

### Rincian Detail Belanja Sewa dan Jasa (Akun 2)
| Item Sewa / Jasa | Justifikasi / Output | Volume | Harga Satuan (Rp) | Total (Rp) | Sumber Dana |
|---|---|---|---|---|---|
| Jasa Cetak PCB Fabrikasi 2-Layer Miniatur | Fabrikasi JLCPCB/PCBWay ENIG gold untuk 11 board | 2 batch | Rp 425.000 | Rp 850.000 | Belmawa |
| Sewa Simulator Pasien Fluke ProSim (Lab Kampus) | Kalibrasi akurasi SpO2 dan Nadi standar klinis | 3 sesi | Rp 100.000 | Rp 300.000 | Belmawa |
| Jasa Laser Cutting Moulding Silikon | Cetakan bodi gelang tahan air IP67 | 1 paket | Rp 400.000 | Rp 400.000 | PT (Co-Funding) |
| **Subtotal Akun 2** | | | | **Rp 1.550.000** | |

---

### Rincian Detail Transportasi Lokal (Akun 3)
| Kegiatan Perjalanan | Destinasi / Tujuan | Volume | Biaya (Rp) | Total (Rp) | Sumber Dana |
|---|---|---|---|---|---|
| Pengadaan Komponen Elektronik & Silikon | Pasar Elektronika Lokal & Agen Logistik | 3 trip | Rp 150.000 | Rp 450.000 | Belmawa |
| Koordinasi & Survei ke Posko SAR / BPBD Daerah | Wawancara SOP triase lapangan bersama personel SAR | 4 trip | Rp 150.000 | Rp 600.000 | Belmawa |
| Uji Lapangan Simulasi Bencana Massal | Lokasi perbukitan / lapangan kampus uji jangkauan LoRa | 2 trip | Rp 150.000 | Rp 300.000 | PT (Co-Funding) |
| **Subtotal Akun 3** | | | | **Rp 1.350.000** | |

---

### Rincian Detail Lain-lain (Akun 4)
| Item Pengeluaran | Justifikasi | Volume | Biaya (Rp) | Total (Rp) | Sumber Dana |
|---|---|---|---|---|---|
| Pendaftaran Hak Cipta (HKI) Algoritma Triase TinyML | Perlindungan kekayaan intelektual Kemenkumham | 1 paket | Rp 425.000 | Rp 425.000 | Belmawa |
| Publikasi Artikel Ilmiah di Seminar Nasional | Luaran tambahan prosiding ber-ISBN/SINTA | 1 artikel | Rp 300.000 | Rp 300.000 | Belmawa |
| Administrasi Logbook, Penjilidan, Materai | Kelengkapan dokumen administrasi Belmawa | 1 paket | Rp 235.000 | Rp 235.000 | Belmawa |
| Kuota Internet & Sinkronisasi Dataset Cloud | Komunikasi riset tim 4 bulan | 3 paket | Rp 100.000 | Rp 300.000 | PT (Co-Funding) |
| **Subtotal Akun 4** | | | | **Rp 1.260.000** | |

---

## 7. Jadwal Pelaksanaan 4 Bulan (Gantt Chart 16 Minggu)

```
Aktivitas / Minggu              | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10| M11| M12| M13| M14| M15| M16|
--------------------------------+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
FASE 0: STUDI & PERSIAPAN       |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Survei SOP triase BNPB/SAR    |████|████|    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Pengadaan komponen 10 gelang  |    |████|████|    |    |    |    |    |    |    |    |    |    |    |    |    |
FASE 1: PERANCANGAN SISTEM      |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Skematik AFE optik radialis   |    |    |████|████|    |    |    |    |    |    |    |    |    |    |    |    |
- Desain PCB miniatur & antena  |    |    |    |████|████|    |    |    |    |    |    |    |    |    |    |    |
- Desain 3D kubah 360° & housing|    |    |    |    |████|████|    |    |    |    |    |    |    |    |    |    |
FASE 2: FABRIKASI & PEMROGRAMAN |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Perakitan PCB 10 unit gelang  |    |    |    |    |    |████|████|    |    |    |    |    |    |    |    |    |
- Pelatihan model TinyML INT8   |    |    |    |    |    |    |████|████|    |    |    |    |    |    |    |    |
- Pemrograman LoRa Mesh posko   |    |    |    |    |    |    |    |████|████|    |    |    |    |    |    |    |
- Fabrikasi silikon IP67        |    |    |    |    |    |    |    |    |████|████|    |    |    |    |    |    |
FASE 3: PENGUJIAN & VALIDASI    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Kalibrasi Fluke ProSim lab    |    |    |    |    |    |    |    |    |    |████|████|    |    |    |    |    |
- Uji jangkauan LoRa 2 km puing |    |    |    |    |    |    |    |    |    |    |████|████|    |    |    |    |
- Uji simulasi triase 10 korban |    |    |    |    |    |    |    |    |    |    |    |████|████|    |    |    |
FASE 4: LAPORAN & LUARAN        |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
- Laporan Kemajuan Belmawa      |    |    |    |    |    |    |    |████|    |    |    |    |    |    |    |    |
- Pendaftaran HKI Algoritma     |    |    |    |    |    |    |    |    |    |    |    |████|████|    |    |    |
- Laporan Akhir & Artikel Ilmiah|    |    |    |    |    |    |    |    |    |    |    |    |████|████|
```

---

## 8. Protokol Validasi & Kriteria Keberhasilan Kuantitatif

Untuk menjamin prototipe lolos review mutu Belmawa dengan nilai tertinggi:

| Parameter Uji | Standar Acuan | Target Kuantitatif LENTERA MEDIS v2.0 | Metode Pengujian |
|---|---|---|---|
| **Akurasi Denyut Nadi (HR)** | ISO 80601-2-61 | Error $\le \pm 2\text{ bpm}$ | Dibandingkan terhadap Patient Simulator Fluke ProSim |
| **Akurasi Saturasi Oksigen ($SpO_2$)** | ISO 80601-2-61 | Error $\le \pm 2\%$ pada rentang 80%–100% | Uji komparasi bertingkat simulator optik |
| **Akurasi Suhu Kulit** | ASTM E1112 | Error $\le \pm 0.1^\circ\text{C}$ | Kalibrasi water bath termal terstandarisasi |
| **Waktu Respon Perubahan Triase** | Protokol START | $\le 2\text{ detik}$ sejak parameter turun | Stress-test injeksi data sinyal darurat |
| **Jarak Pandang Kubah 360°** | Standar SAR Night Ops | Terlihat jelas dari jarak $\ge 25\text{ meter}$ | Pengujian lux-meter di lapangan terbuka gelap |
| **Jangkauan Transmisi LoRa** | Standar LPWAN Bencana | $\ge 1.5\text{--}2.0\text{ km}$ menembus halangan | Pengujian di area perbukitan dan gedung kampus |
| **Daya Tahan Baterai** | Operasi Lapangan BNPB | $\ge 24\text{ jam}$ operasi pemantauan aktif | Pengujian *continuous logging* 10 unit |
