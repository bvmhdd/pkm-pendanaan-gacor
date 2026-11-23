# KOMPARASI LENGKAP DUA OPSI PROPOSAL PKM-KC 2027

> Dokumen komparatif untuk memudahkan Muhammad Muhibbin dan tim (didampingi Endah Setyowati S.T., M.T.) dalam memilih opsi terbaik yang akan diajukan ke seleksi PKM-KC.
> Kedua opsi dirancang dengan pagu anggaran maksimal: **Rp 7.850.000 (Belmawa) + Rp 1.500.000 (Perguruan Tinggi) = Total Rp 9.350.000**.

---

## Matriks Perbandingan Komprehensif

| Kriteria Evaluasi | OPSI 1: LITHOSCAN (Batu Ginjal) | OPSI 2: ASMA-GUARD (Asma Nokturnal Anak) |
|---|---|---|
| **Judul Lengkap** | **LITHOSCAN:** Perangkat Point-of-Care Multi-Wavelength Spectrophotometry dan Nephelometric Turbidimetry Terintegrasi Thermal-Stabilized Chamber dan TinyML untuk Deteksi Dini Risiko Litogenik Batu Ginjal (Nefrolitiasis) | **ASMA-GUARD:** Perangkat Wearable Pemantau Akustik Trakea Berbasis Sensor Piezoelektrik PVDF dan TinyML Terintegrasi Bedside Gateway untuk Deteksi Dini Eksaserbasi Asma Nokturnal pada Anak |
| **Kategori Masalah Medis** | Penyakit ginjal & saluran kemih kronis / rekuren (prevalensi batu ginjal tinggi, angka kambuh 50% dalam 5 tahun). | Kegawatdaruratan respirasi pediatrik nokturnal (70% kematian asma anak terjadi saat tidur malam). |
| **Pola Juara PIMNAS** | Mengadopsi prinsip spektroskopi optik **Orside UGM (Medali Emas PIMNAS 38)** & **Nirwana AI UPI (PKP 2026 Room 7)**. | Mengadopsi prinsip akustik biomedis **ITS TB Batuk (Medali Emas PIMNAS 38)**, **Stetoskop TinyML UGM (PKP 2026)**, & **Cardioguard UGM (Medali Emas PIMNAS 38)**. |
| **Keselarasan dengan Arahan Dosen** | Sangat Baik (HealthTech terjangkau, menyelesaikan masalah nyata, instrumen optik terpadu). | **100% Identik** (Sesuai eksplisit dengan topik *Pulmo-Scan* & *Breath-Alert* di tautan obrolan dosen pembimbing). |
| **Sensor Utama** | Chip Spektrometer 11-Kanal AMS AS7341 (415–910 nm) + Fotodioda Hamamatsu Si-PIN (Nefelometri 90°) + Elektroda pH. | Film Sensor Piezoelektrik Kontak PVDF (TE Connectivity LDT0-028K) + Pre-Amp OPA2350 + Active Bandpass Filter. |
| **Keunikan Rekayasa Fisik** | Ruang uji termal (*Thermal Chamber*) $37,0^\circ\text{C}$ terkontrol PID (mencegah kristalisasi dingin palsu pada urin). | Patch silikon trakea leher yang 100% menolak bising suara udara kamar tidur (kipas, AC, dengkuran). |
| **Arsitektur Sistem** | **Dual-Unit System:** 1 Unit Handheld Field Device (portabel) + 1 Unit Lab Benchmark Station (stasioner). | **Dual-Device Ecosystem:** 2 Unit Wearable Trakea Anak + 1 Unit Bedside Gateway Display Layar TFT 2.4" Meja Kamar. |
| **Bebas Kontaminasi Silang** | **Sangat Terjamin:** Menggunakan kuvet plastik polistiren sekali pakai (*disposable*) seharga Rp 850/buah. | **Sangat Terjamin:** Menggunakan patch perekat medis hipoalergenik sekali pakai (*disposable medical adhesive*). |
| **Validasi Eksperimental di Kampus** | **Sintetis In-Vitro:** Menguji 500 sampel larutan kristal kalsium oksalat bertingkat di lab kimia + kalibrasi Spektrofotometer UV-Vis lab. | **Simulator Akustik + Database Medis:** Mengalirkan database suara mengi resmi (ICBHI 2017) ke Tracheal Acoustic Phantom di lab. |
| **Hambatan Izin Etik Pasien** | **Nol:** Validasi full berbasis larutan kimia sintetis standar analitik (seperti metode Nirwana AI UPI). | **Nol:** Validasi fungsi alat menggunakan simulator trakea dan database klinis terbuka resmi dunia. |
| **Beban Peran Teknik Elektro (Muhibbin)** | Rangkaian transimpedansi fotodioda nanoampere, driver LED spektral, kontroler pemanas PID $37^\circ\text{C}$, PCB 4-layer. | Rangkaian filter analog aktif pita sempit (100–1.800 Hz), Automatic Gain Control (AGC), sirkuit piezoelektrik PVDF. |
| **Beban Peran Komputer / AI (Sahra)** | Preprocessing 11-kanal spektral, regresi indeks Tiselius, klasifikasi TinyML INT8 on-device ESP32-S3. | Ekstraksi fitur audio MFCC 13 koefisien, Spectral Centroid, model 1D-CNN INT8 klasifikasi wheezing. |
| **Beban Peran Telekomunikasi (Syahbudin)** | Telemetri BLE 5.0 transmisi skor risiko urin ke smartphone/dashboard Puskesmas. | Protokol komunikasi nirkabel BLE/ESP-NOW dari patch anak ke Bedside Gateway layar TFT meja kamar orang tua. |
| **Total RAB Belmawa** | **Rp 7.850.000** (Bahan 57,96%, Sewa 13,63%, Transport 19,49%, Lain-lain 8,92%) | **Rp 7.850.000** (Bahan 57,83%, Sewa 13,76%, Transport 19,49%, Lain-lain 8,92%) |
| **Dana Pendamping PT** | **Rp 1.500.000** (Kuvet kuarsa master & casing boks aluminium CNC) | **Rp 1.500.000** (Sound Level Meter terkalibrasi & boks gateway akrilik meja) |
| **Tingkat Kejenuhan Topik** | **Sangat Rendah (Anti-Mainstream):** Belum ada tim PKM yang membuat spektrofotometer POC batu ginjal termal. | **Sedang:** Banyak tim respirasi/stetoskop, tetapi kebaruan sensor kontak PVDF non-udara + Bedside Gateway sangat menonjol. |

---

## Rekomendasi Eksekutif untuk Diskusi dengan Dosen Pembimbing

1. **Jika Ingin Ide yang Paling Minim Pesaing & Unik di PIMNAS:**
   Pilih **LITHOSCAN**. Topik deteksi dini risiko batu ginjal via spektrofotometri multi-spektral urin dan nefelometri $90^\circ$ hampir tidak pernah diajukan oleh tim lain, namun secara sains sangat kuat dan diakui di dunia nefrologi. Juri PIMNAS akan sangat terkesan dengan adanya *Thermal Chamber $37^\circ\text{C}$* dan kuvet disposabel.
   - Dokumen lengkap: [ImplementationPlan-LITHOSCAN-PKMKC.md](file:///C:/Users/muhib/.gemini/antigravity/brain/309818d2-e3b3-4c0a-8cc9-aeccb4b882b0/ImplementationPlan-LITHOSCAN-PKMKC.md)

2. **Jika Ingin Ide yang Paling Mudah Mendapat Persetujuan Dosen (100% Selaras):**
   Pilih **ASMA-GUARD**. Ide ini menjawab langsung arahan Bu Endah pada tautan ChatGPT (*Pulmo-Scan / Breath-Alert*). Masalah asma nokturnal anak sangat emosional dan dekat dengan masyarakat, serta ekosistem *Bedside Gateway* memberikan diferensiasi nyata dibanding aplikasi ponsel biasa.
   - Dokumen lengkap: [ImplementationPlan-ASMAGUARD-PKMKC.md](file:///C:/Users/muhib/.gemini/antigravity/brain/309818d2-e3b3-4c0a-8cc9-aeccb4b882b0/ImplementationPlan-ASMAGUARD-PKMKC.md)
