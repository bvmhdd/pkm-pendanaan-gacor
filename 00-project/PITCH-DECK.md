# PITCH DECK: RESCUEMESH
> **Sub-judul:** Jaringan Komunikasi Darurat Taktis Hibrida LoRa + ESP-NOW dengan Prioritas QoS Adaptif untuk Penyelamatan Korban Bencana di Daerah Terisolir  
> **Skema:** Program Kreativitas Mahasiswa — Karsa Cipta (PKM-KC) 2027  
> **Tim Pengusul:** Muhammad Muhibbin (Ketua), Sahra Raditiya Fadillah, Syahbudin Hamzah Hasan  
> **Dosen Pendamping:** Endah Setyowati, S.T., M.T.  

---

## SLIDE 1: JUDUL & IDENTITY
- **Headline:** **RESCUEMESH**
- **Tagline:** *"Menyambung Asa di Wilayah Buta: Jaringan Komunikasi Darurat Mandiri Tanpa Internet & Tanpa Menara Seluler."*
- **Kategori:** PKM Karsa Cipta (PKM-KC) — Rumpun Computer Science & Teknik Telekomunikasi
- **Identitas Tim:** Universitas Pendidikan Indonesia / Fakultas / Kampus Daerah
- **Visual Cue:** Render 3D prototipe node RESCUEMESH dengan latar belakang area bencana dan peta topologi jaringan mesh bercahaya hijau/oranye.

---

## SLIDE 2: THE PROBLEM (KONDISI GENTING INDONESIA)
- **Headline:** **72 Jam Pertama Pasca-Bencana: Saat Jaringan Lumpuh, Korban Terisolasi**
- **Fakta & Data Empiris:**
  - Indonesia berada di *Ring of Fire* dengan rata-rata ribuan kejadian bencana per tahun (BNPB).
  - Saat gempa bumi, banjir bandang, atau longsor: **90% menara BTS seluler runtuh atau padam total** dalam 4–8 jam akibat putusnya suplai listrik PLN dan robohnya kabel fiber optik.
  - **Golden Time Penyelamatan (72 Jam Pertama):** Tim SAR buta koordinat, keluarga korban kehilangan kontak, dan bantuan logistik terhambat karena ketiadaan sinyal telekomunikasi.
- **Visual Cue:** Foto kolase menara BTS roboh saat gempa dan infografis peta titik blankspot bencana di Indonesia.

---

## SLIDE 3: EXISTING SOLUTIONS & THE FATAL GAPS
- **Headline:** **Mengapa Solusi yang Ada Saat Ini Belum Cukup?**
- **Analisis Masalah Teknologi Eksisting:**
  1. **Handy Talkie (HT / Radio Analog):**
     - ❌ Sinyal rentan terhalang bukit/puing beton (*Line-of-Sight* buruk).
     - ❌ Suara kresek-kresek, rentan salah dengar, dan **tidak bisa mengirim koordinat GPS otomatis**.
  2. **Telepon Satelit (Satellite Phone):**
     - ❌ Biaya perangkat sangat mahal (>Rp 15–20 juta/unit) dan tarif pulsa jutaan rupiah.
     - ❌ Jumlahnya sangat sedikit, mustahil dibagikan ke masyarakat umum/pengungsi.
  3. **LoRaWAN Konvensional:**
     - ❌ Masih bergantung pada *Gateway* tunggal. Begitu *Gateway* rusak, seluruh sensor mati total (*Single Point of Failure*).
     - ❌ Terjadi tabrakan paket parah (*packet collision*) saat banyak korban mengirim sinyal serentak.
- **Visual Cue:** Tabel perbandingan silang merah antara HT, Telepon Satelit, dan LoRa Konvensional.

---

## SLIDE 4: THE SOLUTION — RESCUEMESH
- **Headline:** **Inovasi Karsa Cipta: RESCUEMESH**
- **Definisi Solusi:**
  > Sistem node komunikasi darurat taktis *ad-hoc* berskala mikro-makro yang membentuk jaringan jala mandiri (*self-healing mesh*) secara instan, menghubungkan ponsel warga biasa ke posko SAR tanpa pulsa, tanpa internet, dan tanpa aplikasi khusus.
- **3 Pilar Solusi Utama:**
  1. **Zero-Infrastructure:** 100% bertenaga baterai Li-Ion 18650 + panel surya mini, beroperasi terus-menerus tanpa listrik PLN.
  2. **Zero-App Accessibility:** Korban cukup menyalakan Wi-Fi ponsel biasa, halaman darurat langsung terbuka otomatis (*Captive Portal*).
  3. **Multi-Hop Autonomous Relay:** Data pesan melompat dari node ke node hingga menembus perbukitan/reruntuhan sejauh berkilo-kilometer.
- **Visual Cue:** Diagram ilustrasi korban membuka ponsel $\to$ terhubung ke node RESCUEMESH $\to$ paket melompat via LoRa $\to$ diterima di layar laptop posko SAR.

---

## SLIDE 5: SYSTEM ARCHITECTURE & NOVELTY
- **Headline:** **Arsitektur Hibrida Dual-Radio & Mekanisme Kebaruan**
- **Bagaimana RESCUEMESH Bekerja?**
  - **Layer 1 (Lokal / Klaster Pengungsi - 2.4 GHz):** Menggunakan protokol **ESP-NOW** berkecepatan 1 Mbps untuk pertukaran data lokal cepat tanpa membebani kanal jarak jauh.
  - **Layer 2 (Backbone Jarak Jauh - 920–923 MHz LoRa):** Menembus jarak 2–10 km antar-posko evakuasi pada frekuensi legal regulasi Kominfo RI.
  - **Layer 3 (Adaptive QoS Scheduling Engine):**
    - Paket darurat dikelompokkan ke 3 prioritas:
      - 🔴 **Prioritas 1 (Kritis):** Sinyal SOS + Geolokasi GPS $\to$ bypass antrean, transmisi instan (<2 detik).
      - 🟡 **Prioritas 2 (Penting):** Status medis/kebutuhan logistik $\to$ antrean kedua.
      - 🟢 **Prioritas 3 (Reguler):** Pesan teks warga ke keluarga $\to$ dikirim bergantian sesuai kapasitas kanal.
- **Visual Cue:** Diagram blok sistem teknis dengan warna kontras memisahkan jalur 2.4 GHz (ESP-NOW) dan Sub-GHz (LoRa).

---

## SLIDE 6: COMPETITIVE MATRIX (STATE-OF-THE-ART)
- **Headline:** **Keunggulan Kompetitif Dibanding Produk Sejenis**

| Parameter | HT Analog Polos | Telepon Satelit | Meshtastic Standar | **RESCUEMESH (Inovasi Kami)** |
|---|---|---|---|---|
| **Ketergantungan Internet** | Tidak butuh | Tidak butuh | Tidak butuh | **Tidak butuh (100% Off-Grid)** |
| **Butuh Install Aplikasi Khusus?** | Tidak | Tidak | **Ya (Wajib App)** | **TIDAK (Web Captive Portal)** |
| **Pengiriman Koordinat GPS** | Manual/Suara | Ya (Otomatis) | Ya (Otomatis) | **Ya (Auto-Tagged ke Sinyal SOS)** |
| **Prioritas Paket Darurat (QoS)** | Tidak ada | Tidak ada | Tidak ada (Flooding) | **Ada (Adaptive QoS 3-Tier)** |
| **Jangkauan Multi-Hop** | Terbatas | Satelit | Terbatas Bandwidth | **Multi-Hop Hibrida (Dual-Radio)** |
| **Estimasi Biaya per Node** | Rp 500rb - 1jt | > Rp 15.000.000 | ~Rp 600rb - 900rb | **< Rp 350.000 per unit** |

- **Visual Cue:** Tabel matriks dengan tanda centang hijau tebal pada kolom RESCUEMESH.

---

## SLIDE 7: SPESIFIKASI PROTOTIPE & HARDWARE
- **Headline:** **Rancang Bangun Prototipe Siap Uji (TRL 4)**
- **Spesifikasi Teknis:**
  - **Processor & Gateway:** ESP32-S3 Dual-Core Xtensa LX7 (240 MHz, Wi-Fi, BLE, ESP-NOW).
  - **Long-Range Transceiver:** Modul LoRa Semtech SX1262/SX1276 (920–923 MHz, daya pancar +22 dBm).
  - **Positioning Module:** GNSS / GPS U-Blox NEO-6M dengan antena keramik presisi.
  - **Power Subsystem:** Dual 18650 Li-Ion (6800 mAh total) + Modul Charging TP4056 + Panel Surya Monocrystalline 5V/5W.
  - **Casing & Durabilitas:** Custom 3D Printed PETG Casing dengan seal silikon waterproof IP65.
  - **Visual Indicator:** Layar OLED 0.96 inch I2C untuk status node & jumlah hop aktif.
- **Visual Cue:** Render model 3D exploded view memperlihatkan komponen di dalam casing tahan air.

---

## SLIDE 8: METODE PELAKSANAAN & ACCEPTANCE CRITERIA
- **Headline:** **Tahapan Kerja Terukur Menuju Prototipe Fungsional (4 Bulan)**
- **Roadmap 4 Bulan:**
  - **Bulan 1 (Desain & Pengadaan):** Skematik PCB, simulasi routing mesh, pengadaan komponen (Bahan habis pakai).
  - **Bulan 2 (Fabrikasi & Firmware):** Perakitan 3 node fisik, pembuatan web captive portal, integrasi driver LoRa + ESP-NOW.
  - **Bulan 3 (Implementasi QoS & Kalibrasi Lab):** Pengujian algoritma antrean prioritas SOS, benchmarking latensi & PDR.
  - **Bulan 4 (Simulasi Bencana & UAT):** Uji lapangan di area perbukitan dan gedung beton bertulang, dokumentasi video demonstrasi.
- **Kriteria Keberhasilan Kuantitatif:**
  - ✅ **Packet Delivery Ratio (PDR):** $\ge 90\%$ pada jaringan 3–5 node multi-hop.
  - ✅ **Latensi Paket SOS Prioritas:** $\le 2\text{ detik}$ end-to-end.
  - ✅ **Jangkauan per Hop:** $\ge 2\text{ km}$ (Line-of-Sight) & $\ge 500\text{ m}$ (Hambatan Gedung).
  - ✅ **Daya Tahan Baterai:** $\ge 24\text{ jam}$ transmisi aktif tanpa bantuan sinar matahari.
- **Visual Cue:** Timeline Gantt Chart berwarna dengan checklist target terukur.

---

## SLIDE 9: RENCANA ANGGARAN BIAYA (RAB RASIONAL)
- **Headline:** **Efisiensi Anggaran Mematuhi Pedoman Belmawa 2026**
- **Total Pengajuan:** **Rp 7.500.000** (Rentang aman Belmawa Rp 6–8 Juta) + **Dana Pendamping Kampus Rp 1.500.000**
- **Distribusi Pos Biaya:**
  1. **Bahan Habis Pakai (55% / Rp 4.125.000):** Mikrokontroler ESP32-S3, modul LoRa SX1262, GPS NEO-6M, baterai 18650, panel surya, filamen 3D print PETG, komponen elektronik & PCB. *(Semua item $\le$ Rp 1.000.000 per unit)*.
  2. **Sewa dan Jasa (15% / Rp 1.125.000):** Jasa cetak PCB Fabrikasi, jasa laser cut akrilik, sewa alat ukur RF Spectrum Analyzer lab.
  3. **Transportasi Lokal (20% / Rp 1.500.000):** Transportasi survei area uji lapangan (hutan/perbukitan/pesisir) dan pengadaan komponen.
  4. **Lain-lain (10% / Rp 750.000):** Kuota internet komunikasi tim (sesuai pagu Rp 100rb/bln), publikasi media sosial, dan materi uji coba.
- **Visual Cue:** Diagram lingkaran (*pie chart*) alokasi anggaran yang patuh regulasi Belmawa.

---

## SLIDE 10: TARGET LUARAN & DAMPAK KEBERLANJUTAN
- **Headline:** **Target Capaian & Kontribusi Terhadap SDGs**
- **Luaran Wajib Belmawa:**
  1. Laporan Kemajuan Pelaksanaan.
  2. Laporan Akhir Program.
  3. **Prototipe Fisik Fungsional Siap Uji (3 Unit Node RESCUEMESH).**
  4. Akun Media Sosial Resmi (Dokumentasi proses & edukasi kebencanaan).
- **Luaran Tambahan Potensial (Kunci Emas PIMNAS):**
  - Hak Cipta (HKI) atas Firmware Protokol Mesh & Desain Tata Letak Sirkuit Terpadu.
  - Draf Artikel Ilmiah di Prosiding Internasional / Jurnal Nasional SINTA 2.
- **Dampak SDGs:** Mendukung **SDG 11 (Kota dan Komunitas Berkelanjutan)** dan **SDG 13 (Penanganan Perubahan Iklim & Tanggap Bencana)**.
- **Visual Cue:** Ikon logo SDGs 11 & 13 dan badge medali PIMNAS.

---

## SLIDE 11: SUSUNAN TIM (THE WINNING TEAM)
- **Headline:** **Sinergi Tim Pengusul Berbasis Kompetensi Nyata**
- **Struktur Tim:**
  - **Muhammad Muhibbin (Ketua Tim - Teknik/CS):**
    - *Role:* System Architect & Mesh Routing Protocol Lead.
    - *Tugas:* Perancangan arsitektur jaringan, algoritma adaptive QoS, koordinasi proposal & pengujian sistem.
  - **Sahra Raditiya Fadillah (Anggota 1):**
    - *Role:* UI/UX Captive Portal, Data Telemetri & Media Lead.
    - *Tugas:* Desain antarmuka web captive portal ponsel, pengolahan data pengujian, video demo, dan logbook administrasi.
  - **Syahbudin Hamzah Hasan (Anggota 2):**
    - *Role:* Embedded Hardware, RF & Power Subsystem Lead.
    - *Tugas:* Desain PCB, wiring sirkuit, integrasi panel surya & baterai, perakitan fisik 3D casing dan pengujian jangkauan radio.
  - **Dosen Pendamping:** **Endah Setyowati, S.T., M.T.** (Kepakaran di bidang rekayasa sistem, instrumentasi, dan telekomunikasi).
- **Visual Cue:** Foto profesional anggota tim bersanding dengan bagan pembagian peran.

---

## SLIDE 12: CLOSING & CALL TO ACTION
- **Headline:** **Saat Sinyal Terputus, Harapan Tidak Boleh Terputus.**
- **Closing Statement:**
  > *"RESCUEMESH bukan sekadar tugas kuliah atau proyek lomba, melainkan karsa nyata mahasiswa Indonesia untuk memastikan setiap suara korban bencana dapat didengar dan diselamatkan tepat waktu."*
- **Call to Action:** *"Siap Mewakili Fakultas & Universitas Menuju Panggung Emas PIMNAS 2027."*
- **Kontak & Repositori:** Tim PKM-KC RESCUEMESH
