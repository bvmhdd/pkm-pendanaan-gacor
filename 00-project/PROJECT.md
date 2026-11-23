# PROJECT.md — Sumber Kebenaran Proyek

## Identitas
- **Judul Resmi:** LITHOSCAN: Perangkat Point-of-Care Multi-Wavelength Spectrophotometry dan Nephelometric Turbidimetry Terintegrasi Thermal-Stabilized Chamber dan TinyML untuk Deteksi Dini Risiko Litogenik Batu Ginjal (Nefrolitiasis)
- **Skema PKM:** PKM-Karsa Cipta (PKM-KC)
- **Bidang Keilmuan:** Teknik Elektro (Instrumentasi Sensor & Sirkuit Optoelektronika) × Computer Science (TinyML & Edge AI) × Teknik Telekomunikasi (Telemetri Nirkabel BLE/LoRa)
- **Tahun/periode:** 2027 (Persiapan seleksi proposal 2026/2027)
- **Dosen Pendamping:** Endah Setyowati S.T., M.T.
- **Susunan Tim Pengusul:**
  1. Muhammad Muhibbin (Ketua Tim — Teknik Elektro / Sistem Tertanam)
  2. Sahra Raditiya Fadillah (Anggota 1 — Pemrosesan Sinyal & TinyML)
  3. Syahbudin Hamzah Hasan (Anggota 2 — Telekomunikasi & Telemetri)
- **Tenggat Resmi:** Seleksi Internal Perguruan Tinggi $\rightarrow$ Submisi Nasional Simbelmawa

---

## Masalah (Problem Statement)
- **Konteks:** Nefrolitiasis (penyakit batu ginjal) merupakan salah satu gangguan saluran kemih dengan morbiditas tinggi di Indonesia (prevalensi nasional ~0,5–1% dengan angka kejadian berulang mencapai 50% dalam 5 tahun pasca operasi).
- **Kesenjangan (Gap) Diagnostik Klinis:**
  1. Modalitas radiologi rumah sakit (USG abdomen dan Non-Contrast CT) hanya mampu mendeteksi kalkulus yang telah mengeras dengan diameter $> 3\text{--}4 \text{ mm}$ yang kerap kali telah menyumbat ureter dan memicu nyeri kolik ginjal akut serta hematuria masif.
  2. Pemeriksaan urinalisis dipstick konvensional di Puskesmas hanya memberikan hasil semi-kuantitatif kasar tanpa mampu mengukur indeks supersaturasi kristal mikroskopis dan partikel presipitasi aktif secara real-time.
  3. Pasien pasca terapi (operasi/ESWL) tidak memiliki perangkat pemantau mandiri (*point-of-care testing*) di rumah atau faskes primer untuk mendeteksi kapan urin mereka kembali memasuki fase litogenik aktif sebelum batu terbentuk kembali.
- **Pihak Terdampak:** Pasien pasca-operasi batu ginjal, masyarakat berisiko tinggi (dehidrasi kronis, asam urat tinggi, riwayat keluarga), serta fasilitas kesehatan tingkat pertama (Puskesmas/Posyandu Lansia).

---

## Tujuan & Hipotesis
- **Tujuan Umum:** Merancang bangun dan memvalidasi prototipe ganda (*dual-unit*) spektrofotometer dan nefelometer portabel berbasis sensor optik 11-kanal, ruang ukur termal $37^\circ\text{C}$ terkontrol PID, dan model inferensi TinyML on-device untuk skrining risiko pembentukan batu ginjal.
- **Tujuan Khusus (Terukur):**
  1. Mengembangkan ruang baca optik terstabilisasi termal ($37,0 \pm 0,2^\circ\text{C}$) dengan jalur ganda: transmisi $180^\circ$ (Spektrometer AS7341 415–910 nm) dan hamburan $90^\circ$ (Nefelometri IR 850 nm ISO 7027).
  2. Mengimplementasikan model inferensi TinyML (INT8 quantized) pada mikrokontroler ESP32-S3 untuk mengestimasi konsentrasi presipitasi kalsium oksalat, pH urin, dan indeks risiko Tiselius dengan akurasi $\ge 95\%$ dan latensi $< 20 \text{ ms}$.
  3. Memproduksi 2 unit prototipe fungsional identik (Handheld Field Unit & Lab Benchmark Unit) dengan variabilitas antar-alat (*Coefficient of Variation*) $< 3\%$.
- **Hipotesis (H1):** Kombinasi spektrofotometri multi-spektral 11-kanal dan hamburan nefelometri $90^\circ$ pada suhu fisiologis $37^\circ\text{C}$ mampu memisahkan serapan warna kimia urin dari hamburan fisik kristal kalsium oksalat mikroskopis dengan korelasi analitik $R^2 \ge 0,95$ terhadap spektrofotometer laboratorium standar.
- **Kriteria Keberhasilan:**
  - Korelasi spektral vs Spektrofotometer UV-Vis Lab: $R^2 \ge 0,95$.
  - Batas deteksi kekeruhan nefelometri: Rentang $1 \text{ s.d. } 400 \text{ NTU}$ terkalibrasi Formazin.
  - Akurasi klasifikasi TinyML on-device: $\ge 95\%$ pada 500 sampel uji in-vitro.
  - Waktu pengukuran per sampel: $< 10 \text{ detik}$.
  - Biaya bahan uji per sampel: $< \text{Rp } 1.000$ (kuvet polistiren sekali pakai).

---

## Solusi / Inovasi (LITHOSCAN V2)
- **Deskripsi:** Perangkat genggam *point-of-care* terintegrasi kuvet optik semi-mikro disposabel, sensor spektrometer multi-spektral 11-kanal (AMS AS7341), detektor nefelometri $90^\circ$ (Hamamatsu Si-PIN), sensor pH presisi, dan *Thermal Chamber* $37^\circ\text{C}$ terkontrol PID, dieksekusi oleh ESP32-S3 dengan TinyML on-device dan telemetri nirkabel BLE 5.0.
- **Kebaruan Dibandingkan Solusi yang Ada:**
  1. *Dibandingkan USG/CT Scan:* Deteksi preventif pada fase kristaluria biokimiawi, bukan deteksi pasif setelah batu berukuran besar menyumbat ginjal.
  2. *Dibandingkan Urinalisis Dipstick:* Kuantifikasi objektif konsentrasi kristal (mM) dan turbiditas partikulat (NTU) berbasis algoritma fisika optik ganda (absorbansi + hamburan).
  3. *Dibandingkan Uji Urin Lab Suhu Ruang:* Adanya *Thermal Chamber $37^\circ\text{C}$* mencegah *false positive* kristalisasi dingin akibat suhu ruangan.
  4. *Dibandingkan Prototipe PKM Lain:* Menggunakan kuvet disposabel murah yang menjamin 100% bebas kontaminasi silang antar-sampel.

---

## Metode Ringkas
- **Desain:** *Experimental Engineering Design & In-Vitro Analytical Validation*.
- **Data/Sampel Uji:** 500 sampel larutan presipitasi kalsium oksalat sintetis ($0,1 \text{ s.d. } 5,0 \text{ mM}$), larutan asam urat buatan, dan larutan standar kekeruhan Formazin (0–400 NTU) yang dibuat di laboratorium kimia kampus, ditambah uji interferensi zat pengganggu (urea, glukosa, bilirubin, asam askorbat).
- **Variabel Evaluasi:** Nilai absorbansi spektral $A(\lambda)$, intensitas hamburan $90^\circ$ (NTU), nilai pH, konsentrasi $CaC_2O_4$, akurasi TinyML, latensi inferensi, stabilitas suhu ruang baca, dan reprodusibilitas antar-alat ($CV$).
- **Baseline Pembanding:** Spektrofotometer UV-Vis Double Beam laboratorium terpadu kampus, Turbidimeter standar industri, dan Mikroskop Fase Kontras 1000x.

---

## Rencana Anggaran Biaya (RAB)
- **Sumber Dana Belmawa:** Rp 7.850.000
  - Pos 1: Bahan Habis Pakai (57,96%) = Rp 4.550.000
  - Pos 2: Sewa dan Jasa (13,63%) = Rp 1.070.000
  - Pos 3: Transportasi Lokal (19,49%) = Rp 1.530.000
  - Pos 4: Lain-lain (8,92%) = Rp 700.000
- **Sumber Dana Perguruan Tinggi (PT):** Rp 1.500.000 (Kuvet kuarsa suprasil master & casing boks aluminium CNC)
- **Total Anggaran Program:** **Rp 9.350.000** (100% patuh pedoman Belmawa 2026).

---

## Luaran Target
1. **Luaran Wajib Belmawa:**
   - Laporan Kemajuan
   - Laporan Akhir
   - 2 Unit Prototipe Fungsional Siap Uji (Handheld Unit & Lab Benchmark Unit)
   - Akun Media Sosial Resmi Kegiatan (Instagram aktif >10 postingan edukatif)
2. **Luaran Tambahan:**
   - Hak Cipta (HKI) Source Code Firmware TinyML di Ditjen KI Kemenkumham
   - Draf Artikel Ilmiah siap submisi ke seminar nasional/jurnal terakreditasi SINTA

---

## Gaya Sitasi & Template
- **Gaya Sitasi:** Harvard Style (nama belakang, tahun, alfabetis)
- **Format Naskah:** Times New Roman 12, spasi 1.15, kertas A4 satu kolom, margin 4-3-3-3, Bagian Inti $\le 10$ halaman tanpa cover dan tanpa lembar pengesahan.
