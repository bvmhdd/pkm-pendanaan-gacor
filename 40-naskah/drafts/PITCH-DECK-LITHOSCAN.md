# PITCH DECK: LITHOSCAN
> **Sub-judul:** Penganalisis Risiko Litogenik Urin Portabel Berbasis Nefelometri 850 nm Terstandarisasi ISO 7027, Spektrometri 11-Kanal ams AS7341, dan Stabilisasi Termal 37°C untuk Pencegahan Dini Kekambuhan Nefrolitiasis  
> **Skema:** Program Kreativitas Mahasiswa — Karsa Cipta (PKM-KC) 2027  
> **Tema PKM:** Tema 2: "Kesehatan dan Gizi Masyarakat"  
> **Tim Pengusul:** Muhammad Muhibbin (Ketua), Sahra Raditiya Fadillah, Syahbudin Hamzah Hasan  
> **Dosen Pendamping:** Endah Setyowati, S.T., M.T.  

---

## SLIDE 1: JUDUL & IDENTITAS INOVASI
- **Headline:** **LITHOSCAN** *(Point-of-Care Urine Lithogenic Risk Analyzer)*
- **Tagline:** *"Presisi Fisiologis di Genggaman: Deteksi Dini Kristaluria Batu Ginjal pada Suhu Tubuh 37°C Sebelum Mengeras."*
- **Kategori:** PKM Karsa Cipta (PKM-KC) — Rumpun Teknik Elektro, Biomedis, & Computer Science
- **Identitas Institusi:** Universitas Pendidikan Indonesia (UPI)
- **Visual Cue:**
  ![Visualisasi 3D Prototipe LITHOSCAN](file:///d:/Belajar/Semester%205/Project/PKM/40-naskah/assets/lithoscan_3d_render.jpg)
  *Render 3D fotorealistik LITHOSCAN: Perangkat genggam ergonomis putih medis dengan grip abu-abu slate, chamber optik atas terbuka sebagian memperlihatkan kuvet urin transparan 10x10 mm, layar OLED 2.4" menyala menampilkan Tiselius Risk Dial (LOW RISK), Chamber 37.0°C STABLE, Turbidity 8.2 NTU, pH 6.20, dan cincin status LED cyan.*

> 🔍 **Bank Kata Kunci Referensi (Slide 1):**
> * **Google Scholar / Scopus:** `"point-of-care urinalysis" "kidney stone" handheld analyzer "micro-optical"`
> * **Standar Acuan:** *POCT08-A: Quality Practices in Non-instrumented Point-of-Care Testing (CLSI Standard)*

---

## SLIDE 2: THE PROBLEM (EPIDEMIOLOGI & BEBAN KEKAMBUHAN BATU GINJAL)
- **Headline:** **Kekambuhan Senyap Batu Ginjal: Mengapa Pasca-Operasi Bukan Akhir Masalah?**
- **Fakta & Data Empiris:**
  - **Angka Kekambuhan Ekstrem (50% Recurrence):** Sekitar 50% penderita batu ginjal (*nefrolitiasis*) mengalami kekambuhan dalam rentang 3–5 tahun pasca-tindakan, dan melonjak hingga 70% dalam 10 tahun (NIH / EAU Guidelines 2024).
  - **Beban Biaya Katastropik BPJS:** Penanganan batu ginjal stadium lanjut (ESWL, PCNL, dan operasi terbuka) menelan anggaran kesehatan triliunan rupiah setiap tahun.
  - **Fase Kritis Terlewatkan:** Pembentukan batu ginjal diawali dari **supersaturasi mikrokristal kalsium oksalat (CaOx) dan abrasi epitel tubulus renalis** yang berlangsung berminggu-minggu tanpa rasa sakit (*silent lithogenesis*).
  - **Ketidakberdayaan Pasien di Rumah:** Pasien pasca-operasi hanya dipulangkan dengan anjuran umum *"banyak minum air putih"* tanpa ada instrumen objektif di rumah untuk memantau apakah urin mereka sedang dalam fase mengkristal aktif.

> 🔍 **Bank Kata Kunci Referensi (Slide 2):**
> * **PubMed / Scopus:** `"kidney stone recurrence rate" "5-year" "calcium oxalate" epidemiology urolithiasis`
> * **Jurnal Kunci:** *European Association of Urology (EAU) Guidelines on Urolithiasis (2023–2024)*; *The Journal of Urology*
> * **Data Nasional:** *Riset Kesehatan Dasar (Riskesdas) Kemenkes RI — Prevalensi Penyakit Ginjal & Urolitiasis*

---

## SLIDE 3: EXISTING SOLUTIONS & FATAL GAPS
- **Headline:** **Mengapa Solusi Saat Ini Gagal Mencegah Pembentukan Batu?**

| Solusi Klinis Saat Ini | Prinsip Kerja | Kelemahan Fatal dalam Pencegahan Dini |
|---|---|---|
| **Pencitraan Medis (USG / CT-Scan / BNO-IVP)** | Memantulkan gelombang suara / sinar-X | ❌ Hanya bisa melihat batu yang **sudah mengeras berukuran $>3\text{--}4\text{ mm}$**. Terlambat untuk tindakan preventif non-invasif. |
| **Dipstick Urin Kertas (Strip Celup Kimia)** | Reaksi kolorimetri kimiawi reagen | ❌ Hanya semi-kuantitatif (perubahan warna kasar); **buta terhadap partikel kristal padat**; rawan kadaluarsa kelembapan udara. |
| **Analisis Laboratorium Sentral (Urinalisis Lab)** | Mikroskopi sedimen manual analis RS | ❌ Biaya mahal (Rp 80.000–150.000 per tes); butuh waktu 1–2 hari; **tidak mungkin dilakukan pasien setiap hari di rumah**. |
| **Urinometer Portabel Komersial Biasa** | Turbidimetri cahaya tampak umum | ❌ **Fatal Bias:** Urin diuji pada suhu ruangan dingin (25°C) sehingga memicu presipitasi artifaktual; bias serapan warna kuning urin. |

- **Fatal Gap:** Ketiadaan alat pengukur risiko kristalisasi mandiri yang **non-destruktif, objektif terkuantisasi, dan bebas dari artefak presipitasi suhu ruangan**.

> 🔍 **Bank Kata Kunci Referensi (Slide 3):**
> * **PubMed / IEEE:** `"dipstick urinalysis" limitations "microscopic hematuria" "crystalluria" sensitivity specificity`
> * **Scopus / Elsevier:** `"ultrasound detection limit" nephrolithiasis "asymptomatic micro-calculi" <4mm`

---

## 4. SLIDE 4: THE SOLUTION — LITHOSCAN
- **Headline:** **LITHOSCAN: Laboratorium Urinalisis Presisi Tinggi dalam Genggaman**
- **Definisi Solusi:**
  > Penganalisis optik-kimia portabel nirkabel berbasis spektrofotometri multi-kanal dan nefelometri inframerah yang dilengkapi ruang inkubasi termal fisiologis 37.0°C untuk menghitung indeks risiko litogenik Tiselius secara real-time pada pasien rawat jalan.
- **3 Pilar Keunggulan Teknologi LITHOSCAN:**
  1. **Optical-Thermal In-Vivo Simulation (37.0°C PID Chamber):** Mengeliminasi 100% kristalisasi palsu akibat pendinginan urin di suhu ruang.
  2. **Interference-Free Nephelometry (ISO 7027 850 nm):** Mengukur kerapatan partikel kristal kalsium oksalat secara murni tanpa bias serapan pigmen urokrom kuning urin.
  3. **Multi-Spectral Hematuria Fingerprinting (ams AS7341):** Menangkap puncak serapan oksihemoglobin (415 nm Soret band & 542/577 nm Q-bands) untuk mendeteksi luka mikroskopis epitel tubulus ginjal.

> 🔍 **Bank Kata Kunci Referensi (Slide 4):**
> * **Scopus / ScienceDirect:** `"point of care" "calcium oxalate" "crystallization kinetics" spectrophotometry handheld`
> * **IEEE Xplore:** `"multi-spectral optical sensor" "biofluid analysis" point-of-care low-cost`

---

## 5. SLIDE 5: SYSTEM ARCHITECTURE & SCIENTIFIC PRINCIPLES
- **Headline:** **Arsitektur Tiga Tingkat: Fisika Optik, Bio-Termodinamika, & Elektrokimia**
- **Bagaimana LITHOSCAN Bekerja Secara Ilmiah?**
  1. **Sensor Optik 1 — Nefelometri 90° 850 nm (Standar ISO 7027):**
     * Laser inframerah dekat ($\lambda = 850\text{ nm}$) ditembakkan melintasi kuvet polistiren sekali pakai.
     * Partikel kristal kalsium oksalat monohidrat (ukuran 5–15 $\mu\text{m}$) memicu **Mie Scattering**. Fotodioda pada sudut 90° menangkap intensitas hamburan partikel padat ($I_{90^\circ}$).
     * Mengapa 850 nm? Pigmen urin (urokrom/bilirubin) memiliki koefisien serapan nol ($\epsilon \approx 0$) pada spektrum NIR, menjamin sinyal bebas bias warna urin pekat.
  2. **Sensor Optik 2 — Spektrometer Multi-Kanal ams AS7341:**
     * Menggunakan filter nano-optik CMOS 11 kanal.
     * Mengukur absorbansi diferensial pada kanal F1 (415 nm) dan F4/F5 (515/555 nm) untuk mendeteksi lisis eritrosit (*microhematuria*).
  3. **Sensor Kimia 3 — Potensiometri pH Nernstian:**
     * Membedakan etiologi kristal: pH < 5.5 (predisposisi batu asam urat) vs pH 5.5–6.8 (kalsium oksalat) vs pH > 6.8 (kalsium fosfat/struvit).

```
                      +-------------------------------------------------------+
                      |         KUVET URIN SEGAR (DISPOSABEL 10x10 mm)        |
                      +-------------------------------------------------------+
                                                  |
                 +--------------------------------+--------------------------------+
                 |                                                                 |
                 v                                                                 v
  +------------------------------+                                  +------------------------------+
  |    OPTIK 1: NEFELOMETRI 90°  |                                  |   OPTIK 2: MULTI-SPEKTRAL    |
  |  - Emitter Laser NIR 850 nm  |                                  |  - ams AS7341 (11-Ch CMOS)   |
  |  - Standar ISO 7027          |                                  |  - F1 (415 nm): Soret Band   |
  |  - Deteksi: Kristal CaOx     |                                  |  - F4/F5: Q-Bands Hemoglobin |
  +------------------------------+                                  +------------------------------+
                 |                                                                 |
                 +--------------------------------+--------------------------------+
                                                  |
                                                  v
                               +--------------------------------------+
                               |      RUANG TERMAL TERTUTUP 37.0°C    |
                               |  - Elemen PTC Keramik 12V 10W        |
                               |  - Closed-Loop PID (NTC Termistor)   |
                               |  - Mencegah Presipitasi Artifaktual  |
                               +--------------------------------------+
                                                  |
                                                  v
                               +--------------------------------------+
                               |      ESP32-S3 ON-DEVICE TinyML       |
                               |  - Fusi Parameter: I_scat, A, pH, T  |
                               |  - Estimasi Skor Risiko Tiselius     |
                               +--------------------------------------+
```

> 🔍 **Bank Kata Kunci Referensi (Slide 5):**
> * **ISO Standard:** `"ISO 7027-1:2016" "Water quality — Determination of turbidity"`
> * **PubMed / ACS Sensors:** `"ams AS7341" urine OR hematuria "optical absorption" multi-spectral`
> * **Optics / Mie Scattering:** `"Mie scattering" "calcium oxalate monohydrate" crystal size distribution nephelometry`

---

## 6. SLIDE 6: PRIMARY SCIENTIFIC NOVELTY (RUANG TERMAL 37°C PID)
- **Headline:** **Pembeda Utama: Mengapa Kontrol Termal 37.0°C Mengubah Segalanya?**
- **Bio-Termodinamika Kelarutan Urin:**
  - Urin manusia di dalam ginjal berada pada kesetimbangan metastabil terlindungi oleh inhibitor makromolekul alami (sitrat, nefrokalsin, pirofosfat).
  - Pendinginan sampel urin ke suhu ruang ($20\text{--}25^\circ\text{C}$) menurunkan batas metastabilitas termodinamika. Ion $\text{Ca}^{2+}$ dan $\text{C}_2\text{O}_4^{2-}$ mengendap secara spontan di dasar tabung.
  - **Dampak Klinis:** Alat tanpa pengatur suhu akan memberikan vonis **Positif Palsu (False Positive)**: pasien divonis berisiko tinggi batu ginjal padahal kristal tersebut baru terbentuk di luar tubuh karena udara dingin ruangan ber-AC!
- **Solusi Enjiniring LITHOSCAN:**
  - Chamber pemanas berbahan blok aluminium anodized hitam dengan elemen pemanas keramik PTC 12V 10W.
  - Algoritma kontrol PID tertanam pada ESP32-S3 menjaga suhu cairan tepat pada **$37.0^\circ\text{C} \pm 0.3^\circ\text{C}$** selama 30 detik pembacaan optik.

> 🔍 **Bank Kata Kunci Referensi (Slide 6):**
> * **PubMed / Urolithiasis:** `"calcium oxalate solubility" temperature 37 C 25 C "metastable limit" urine crystallization`
> * **Biophysics / ScienceDirect:** `"temperature dependence" "calcium oxalate monohydrate" nucleation growth kinetics`

---

## 7. SLIDE 7: MATRIKS KOMPARASI KOMPETITIF (STATE-OF-THE-ART)
- **Headline:** **Keunggulan Nyata LITHOSCAN Dibandingkan Seluruh Alternatif**

| Parameter Evaluasi | Dipstick Urin Strip Kertas | Mikroskopi Laboratorium RS | Turbidimeter Komersial Pasar | **LITHOSCAN (Inovasi Kami)** |
|---|---|---|---|---|
| **Kuantifikasi Kristaluria** | ❌ Buta Kristal (Hanya ion) | ⚠️ Manual (Subjektif mata analis) | ⚠️ Terganggu warna kuning urin | **✅ Nefelometri 90° 850 nm ISO 7027** |
| **Kontrol Suhu Pengujian** | ❌ Suhu Ruang (Rawan false +) | ❌ Suhu Ruang / Kulkas | ❌ Tanpa Pemanas | **✅ Ruang Termal 37.0°C Tertutup PID** |
| **Deteksi Mikrohematuria** | ⚠️ Semi-kuantitatif kasar | ✅ Kuantitatif hitung sel darah | ❌ Tidak Ada | **✅ Spektrometer Multi-Kanal AS7341** |
| **Kalkulasi Risiko Otomatis** | ❌ Tidak Ada | ⚠️ Perlu kalkulasi dokter urologi | ❌ Hanya angka absorbansi mentah | **✅ On-Device TinyML Indeks Tiselius** |
| **Kontaminasi Silang Antar-Sampel** | ✅ Disposabel | ⚠️ Wadah kaca dicuci ulang | ⚠️ Kuvet kaca dicuci manual | **✅ Kuvet Polistiren Disposabel (<Rp 1.000)** |
| **Biaya Alat / Operasional** | Rp 5.000/strip (Kasar) | Alat Rp 150 Juta \| Rp 120.000/tes | Alat Rp 25–45 Juta | **Prototipe Rp 3,85 Juta \| Rp 800/tes** |

> 🔍 **Bank Kata Kunci Referensi (Slide 7):**
> * **PubMed / Clinica Chimica Acta:** `"Tiselius risk index" AP(CaOx) simplified calculation urinary stone risk`
> * **IEEE Sensors:** `"low-cost point of care spectrophotometer" validation benchtop comparison`

---

## 8. SLIDE 8: SPESIFIKASI TEKNIS & PROFIL ENJINIRING (TRL 4)
- **Headline:** **Spesifikasi Enjiniring Presisi Tinggi dalam Format Handheld Ergonomis**
- **Spesifikasi Perangkat Keras LITHOSCAN:**
  - **Processor & Core:** ESP32-S3 Dual-Core Xtensa LX7 @ 240 MHz (512 KB SRAM, 8 MB Flash, Vector Extensions ESP-NN).
  - **Optical Nephelometric Subsystem:** Emitter Laser Diode NIR 850 nm collimated ($P = 5\text{ mW}$), Fotodioda responsif NIR sudut 90° dengan transimpedance amplifier berderau rendah.
  - **Multi-Spectral Sensor:** ams AS7341 (11-kanal optik, ADC internal 16-bit, antarmuka $I^2C$, rentang 350–1000 nm).
  - **Thermal Actuator & Sensor:** Elemen PTC Keramik 12V 10W + NTC Thermistor 10k $\pm 0.5\%$ + MOSFET PWM closed-loop PID.
  - **Electrochemical pH Front-End:** Miniatur glass combination electrode + AFE high-input impedance ($>10^{12}\ \Omega$) + ADS1115 16-bit ADC eksternal.
  - **User Interface & Display:** Layar grafis OLED 2.4 inci Full-Color (SPI), 3 tombol navigasi taktil, cincin status LED cyan.
  - **Daya & Portabilitas:** Baterai Li-Ion 18650 2S (7.4V 2600 mAh), modul charging USB-C PD, konsumsi daya rata-rata 4.2W saat pemanasan aktif.
  - **Dimensi & Bahan Casing:** $16.5 \times 8.2 \times 4.2\text{ cm}$, berat 280 gram, material 3D printing resin antibakteri medical-grade.

> 🔍 **Bank Kata Kunci Referensi (Slide 8):**
> * **IEEE Xplore / Embedded AI:** `"TinyML" "ESP32-S3" TensorFlow Lite Micro INT8 quantization inference latency`
> * **Hardware Datasheets:** `"ams AS7341 datasheet" optical filters; "ADS1115" Texas Instruments analog-to-digital converter`

---

## 9. SLIDE 9: METODE PELAKSANAAN & VALIDASI LABORATORIUM
- **Headline:** **Tahapan Kerja Terukur Menuju Prototipe Fungsional Siap Uji (4 Bulan)**
- **Roadmap 4 Bulan Pelaksanaan:**
  - **Bulan 1 (Desain Optik-Termal & Pengadaan Komponen):** Perancangan 3D chamber optik 90° blackout, skematik PCB utama ESP32-S3 + AFE ADS1115, pengadaan kuvet dan sensor.
  - **Bulan 2 (Fabrikasi PCB, Perakitan & Tuning PID):** Fabrikasi PCB 4-layer ENIG gold, perakitan elemen pemanas PTC, penyetelan konstanta PID ($K_p, K_i, K_d$) termal 37.0°C.
  - **Bulan 3 (Kalibrasi Spektral & Pelatihan Model TinyML):** Kalibrasi nefelometri terhadap larutan standar Formazin ISO 7027 (0–100 NTU), kalibrasi hemoglobin AS7341, pelatihan model TinyML Tiselius pada 500 sampel urin sintetis bertingkat.
  - **Bulan 4 (Validasi Reprodusibilitas & Tri-Validation Protocol):** Uji komparasi terhadap Spektrofotometer UV-Vis laboratorium kampus, uji Coefficient of Variation ($CV < 3\%$), penulisan laporan dan draf paten.
- **Kriteria Keberhasilan Kuantitatif:**
  - ✅ **Akurasi Suhu Chamber:** $37.0^\circ\text{C} \pm 0.3^\circ\text{C}$ tercapai dalam waktu $\le 60\text{ detik}$.
  - ✅ **Linearitas Turbiditas 850 nm:** Koefisien determinasi $R^2 \ge 0.98$ terhadap larutan standar formazin ISO 7027.
  - ✅ **Batas Deteksi Mikrohematuria:** Mampu mendeteksi lisis hemoglobin hingga konsentrasi $\le 0.015\text{ mg/dL}$ (setara 5–10 eritrosit/$\mu\text{L}$).
  - ✅ **Akurasi Model TinyML:** Akurasi klasifikasi risiko litogenik Tiselius $\ge 95\%$ dengan waktu inferensi on-device $<10\text{ milidetik}$.

> 🔍 **Bank Kata Kunci Referensi (Slide 9):**
> * **Analytical Chemistry:** `"formazin turbidity standard" calibration ISO 7027 linearity`
> * **Urolithiasis Research:** `"artificial urine" recipe calcium oxalate crystallization kinetics protocol`

---

## 10. SLIDE 10: RENCANA ANGGARAN BIAYA (RAB BELMAWA VALID)
- **Headline:** **Efisiensi Anggaran Maksimal: Dua Prototipe Identik Sesuai Pagu Belmawa**
- **Total Pengajuan Dana:** **Rp 7.850.000** (Dana Maksimal Belmawa) + **Rp 1.500.000** (Dana Pendamping PT) = **Rp 9.350.000**
- **Distribusi Pos Biaya (100% Sesuai Pedoman Belmawa):**
  1. **Bahan Khusus (59,55% / Rp 4.675.000):** Pengadaan komponen untuk **2 Unit Prototipe Identik (Field Unit & Lab Station)** + 100 pcs Kuvet Polistiren Disposabel (2x ESP32-S3, 2x ams AS7341, 2x Laser 850nm, 2x Fotodioda NIR, 2x PTC Heater, 2x Sensor pH & ADS1115, 2x Baterai Li-Ion 2S, filamen resin 3D biocompatible).
  2. **Sewa dan Jasa (14,65% / Rp 1.150.000):** Jasa cetak PCB 4-Layer ENIG Gold JLCPCB/PCBWay, sewa spektrofotometer UV-Vis lab biokimia kampus untuk uji validasi emas.
  3. **Transportasi Lokal (13,38% / Rp 1.050.000):** Pengadaan bahan kimia sintetis lokal dan observasi klinik urologi/laboratorium patologi klinik.
  4. **Lain-lain (12,42% / Rp 975.000):** Biaya pendaftaran Hak Cipta (HKI) algoritma firmware, biaya pendaftaran seminar nasional luaran ilmiah, materai & administrasi.

> 🔍 **Bank Kata Kunci Referensi (Slide 10):**
> * **Pedoman Resmi:** *Buku Pedoman Program Kreativitas Mahasiswa (PKM) 2026/2027 — Direktorat Belmawa Kemendiktisaintek*

---

## 11. SLIDE 11: TARGET LUARAN & BATASAN ETIKA MEDIS
- **Headline:** **Komitmen Luaran Nyata Menuju Prestasi PIMNAS 2027**
- **Luaran Wajib Belmawa:**
  1. Laporan Kemajuan Program.
  2. Laporan Akhir Program.
  3. **Prototipe Fisik Fungsional Siap Uji (2 Unit Alat LITHOSCAN + 100 Kuvet Uji).**
  4. Akun Media Sosial Resmi Edukasi Pencegahan Batu Ginjal & Dokumentasi Riset.
- **Luaran Tambahan Berkualitas Tinggi:**
  - Pendaftaran Hak Cipta (HKI) Firmware Algoritma Koreksi Optik-Termal LITHOSCAN di Kemenkumham RI.
  - Draf Paten Sederhana untuk Mekanisme Ruang Inkubasi Termal 37°C Chamber Optik Portabel.
  - Artikel Ilmiah siap publikasi di Jurnal Nasional Terakreditasi SINTA 2 / Seminar Internasional IEEE.
- **Kepatuhan Etika Akademik (Academic Integrity):**
  > *Pada tahap prototipe PKM-KC, pengujian awal menggunakan **Urin Sintetis Terstandarisasi Laboratorium (Surine / Artificial Urine ISO-standard)**, sehingga bebas dari isu pelanggaran bioetika spesimen klinis manusia, sebelum dilanjutkan ke tahap clinical trial pasca-PKM.*

> 🔍 **Bank Kata Kunci Referensi (Slide 11):**
> * **Ethics / Medical Device:** `"ethical clearance waiver" artificial biofluids synthetic urine testing medical devices`

---

## 12. SLIDE 12: SUSUNAN TIM & STRATEGI EKSEKUSI
- **Headline:** **Kolaborasi Tri-Disiplin Menuju Panggung Juara PIMNAS**
- **Struktur Tim Pengusul:**
  - **Muhammad Muhibbin (Ketua Tim — S1 Teknik Elektro):** Desain sirkuit AFE optik, layout PCB 4-layer, sirkuit driver pemanas PTC closed-loop PID 37°C, dan sistem daya baterai Li-Ion.
  - **Sahra Raditiya Fadillah (Anggota 1 — S1 Teknik Telekomunikasi):** Integrasi modul komunikasi BLE 5.0, desain mekanik housing optik 3D printing kedap cahaya, dan protokol telemetri nirkabel ke dokter urologi.
  - **Syahbudin Hamzah Hasan (Anggota 2 — S1 Informatika / CS):** Ekstraksi fitur serapan hemoglobin AS7341, implementasi on-device TinyML INT8 Tiselius Index pada ESP32-S3, dan desain antarmuka OLED 2.4".
  - **Dosen Pendamping: Endah Setyowati, S.T., M.T.** (Kepakaran di bidang instrumentasi biomedis, telekomunikasi cerdas, dan rekayasa kontrol).
- **Closing Statement:**
  > *"Batu ginjal tidak boleh lagi menunggu hingga mengeras dan memaksa operasi. LITHOSCAN menghadirkan laboratorium fisiologis presisi ke genggaman pasien: mendeteksi kristalisasi tepat pada suhu tubuh manusia, mencegah kekambuhan, dan menyelamatkan ribuan nyawa dari meja operasi."*
- **Call to Action:** *"Siap Mewakili Kampus Melangkah Menuju Medali Emas PIMNAS 2027!"*

---

## BONUS: MASTER QUERY BANK (PANDUAN PENELUSURAN REFERENSI KARYA TULIS)

Tabel berikut adalah acuan cepat string penelusuran (*search queries*) yang dapat langsung Anda salin ke mesin pencari ilmiah:

| No | Sub-sistem / Konsep | Target Database Ilmiah | String Pencarian Siap Salin (Copy-Paste Query) |
|---|---|---|---|
| **1** | **Nefelometri 850 nm (Hamburan Kristal)** | IEEE Xplore / Scopus | `"ISO 7027" AND ("nephelometry" OR "turbidity") AND (850nm OR "near-infrared") AND ("particle scattering" OR "calcium oxalate")` |
| **2** | **Spektrometri AS7341 (Mikrohematuria)** | PubMed / ACS Sensors | `("AS7341" OR "multi-spectral sensor") AND ("hemoglobin" OR "hematuria" OR "urinalysis") AND (415nm OR "Soret band" OR 540nm)` |
| **3** | **Termal 37°C vs 25°C (Kinetika Presipitasi)** | PubMed / J. Urology | `"calcium oxalate" AND ("solubility" OR "nucleation") AND ("temperature" OR "37 C" OR "room temperature") AND ("urine" OR "in-vitro")` |
| **4** | **Potensiometri pH & Nernst 37°C** | ScienceDirect / Analytical Chem | `("urinary pH" OR "glass electrode") AND ("Nernst equation" OR "temperature compensation") AND ("uric acid stone" OR "calcium phosphate")` |
| **5** | **TinyML on-Device ESP32-S3** | IEEE Access / ArXiv | `("TinyML" OR "TensorFlow Lite Micro") AND ("ESP32" OR "ESP32-S3") AND ("point-of-care" OR "biosensor" OR "classification")` |
| **6** | **Indeks Risiko Tiselius AP(CaOx)** | PubMed / Urolithiasis | `("Tiselius" OR "AP(CaOx)") AND ("crystallization risk" OR "ion-activity product") AND ("nephrolithiasis" OR "kidney stone recurrence")` |
