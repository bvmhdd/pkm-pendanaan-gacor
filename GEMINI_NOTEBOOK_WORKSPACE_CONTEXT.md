# PKM-KC 2027 WORKSPACE — FULL CONSOLIDATED CONTEXT
> **Sumber Kebenaran Repositori PKM-KC 2027** untuk diintegrasikan ke **Gemini Notebook (NotebookLM / Google AI Studio)** menggunakan model **Gemini 4 Neon** (1M Token Context Window).
> Dokumen ini memuat seluruh kontrak operasional, profil tim, ide karsa cipta, pitch deck, regulasi Belmawa 2026, matriks bukti empiris, dan 10 modul skill otomasi agen riset.

---

<!-- ======================================================== -->
<workspace_file path="README.md">
# PKM Agentic Workspace — Persiapan PKM-KC 2027

Workspace kolaboratif tim untuk penyusunan proposal dan rekayasa prototipe **Program Kreativitas Mahasiswa — Karsa Cipta (PKM-KC)**.

---

## 👥 Tim Pengusul
- **Ketua Tim:** Muhammad Muhibbin
- **Anggota 1:** Sahra Raditiya Fadillah
- **Anggota 2:** Syahbudin Hamzah Hasan
- **Dosen Pendamping:** Endah Setyowati, S.T., M.T.

---

## 📂 Struktur Repositori

```text
├── AGENTS.md                  # Kontrak operasi agen AI & integritas akademik
├── SOUL.md                    # Nilai epistemik, standar bukti, dan etika
├── USER.md                    # Profil tim, pembagian peran & preferensi kerja
├── MEMORY.md                  # Sumber kebenaran keputusan proyek yang disepakati
├── 00-project/
│   ├── PROJECT.md             # Dokumen inti konsep karsa cipta
│   ├── TIMELINE.md            # Jadwal milestone dan target
│   └── PITCH-DECK.md          # Bahan presentasi / pitch deck 12 slide
├── 10-pedoman/
│   ├── CHECKLIST-PEDOMAN.md   # Ekstraksi aturan resmi PKM 2026 (10 hlm, anggaran, format)
│   ├── PANDUAN-PKM-2026.pdf   # Buku panduan resmi Belmawa 2026
│   └── CONTOH-LOLOS.pdf       # Proposal rujukan yang lolos pendanaan
├── 20-literatur/
│   ├── EVIDENCE-LEDGER.md     # Buku besar bukti ilmiah terverifikasi (IEEE/Scopus)
│   └── notes/                 # Catatan ekstraksi per paper
├── 30-riset/
│   ├── CLAIM-MATRIX.md        # Matriks klaim ↔ bukti ↔ status uji
│   ├── EXPERIMENT-LOG.md      # Catatan pengujian prototipe & telemetri
│   ├── data/                  # Data mentah pengujian (read-only)
│   └── analysis/              # Skrip & visualisasi data analisis
├── 40-naskah/
│   ├── OUTLINE.md             # Kerangka bab proposal
│   └── drafts/                # Draf naskah per versi (drafts/v01...)
├── 50-review/
│   ├── REVIEWER-RUBRIC.md     # Rubrik simulasi penilaian resmi juri PIMNAS
│   └── REVIEW-LOG.md          # Log catatan review dan evaluasi kelemahan naskah
└── skills/ & .agents/skills/  # Modul otomasi agen riset terstandarisasi
```

---

## 🚀 Alur Kerja Cepat untuk Rekan Tim
1. Baca [USER.md](USER.md) dan [00-project/PROJECT.md](00-project/PROJECT.md) untuk memahami pembagian peran dan fokus proyek.
2. Lihat [00-project/PITCH-DECK.md](00-project/PITCH-DECK.md) jika membutuhkan bahan presentasi cepat ke dosen pendamping.
3. Patuhi aturan administrasi dan batas anggaran pada [10-pedoman/CHECKLIST-PEDOMAN.md](10-pedoman/CHECKLIST-PEDOMAN.md).
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="AGENTS.md">
# AGENTS.md — Kontrak Operasi

Workspace ini mendukung penyusunan proposal/laporan **PKM (Program Kreativitas Mahasiswa, Belmawa)**.
Tujuannya: argumentasi, hasil, dan analisis yang **empiris, dapat diverifikasi, dan dapat direproduksi**.

## Urutan baca di awal sesi
1. `SOUL.md` → 2. `USER.md` → 3. `MEMORY.md` → 4. `00-project/PROJECT.md` → 5. `10-pedoman/CHECKLIST-PEDOMAN.md`
Lalu baca `skills/<nama>/SKILL.md` yang relevan dengan tugas sebelum mengerjakan.

## Aturan keras (tidak boleh dilanggar)
1. **Jangan mengarang** sitasi, DOI, angka, statistik, hasil uji, atau kutipan. Bila tidak terverifikasi → tulis `[BELUM TERVERIFIKASI]`.
2. **Setiap klaim faktual** di naskah harus menunjuk ke baris di `EVIDENCE-LEDGER.md` atau `CLAIM-MATRIX.md`. Klaim tanpa bukti ditandai `[TANPA BUKTI]`.
3. **Data mentah di `30-riset/data/` bersifat read-only.** Transformasi dilakukan lewat skrip di `analysis/`, bukan edit manual.
4. **Pisahkan** fakta, inferensi, dan opini. Beri label bila perlu: `[FAKTA]`, `[INFERENSI]`, `[ASUMSI]`.
5. **Aturan teknis PKM** (skema, format, batas, plafon dana, tenggat) hanya boleh bersumber dari `10-pedoman/`. Bila tidak ada di sana → tanyakan, jangan menebak.
6. **Jangan menulis hasil sebelum data ada.** Boleh membuat kerangka & hipotesis; angka hanya dari `analysis/`.
7. Kejujuran akademik: hasil negatif/null dilaporkan apa adanya. Integritas > kesan hebat.

## Cara bekerja
- Pecah tugas besar menjadi langkah kecil; tunjukkan rencana sebelum eksekusi bila dampaknya besar.
- Setelah selesai, **perbarui** file terkait (`CLAIM-MATRIX`, `EXPERIMENT-LOG`, `MEMORY`) — jangan hanya menjawab di chat.
- Akhiri tiap tugas dengan: **Apa yang dikerjakan · Apa yang belum pasti · Langkah berikutnya.**
- Tanya klarifikasi **satu pertanyaan sekali**, hanya jika benar-benar menghalangi pekerjaan.

## Konvensi
- Bahasa utama: Bahasa Indonesia (istilah teknis boleh Inggris). Naskah mengikuti kaidah PUEBI/EYD.
- Penamaan file: `kebab-case`, tanggal `YYYY-MM-DD`.
- Sitasi: gaya yang diminta pedoman (default sementara: **APA 7**) — sesuaikan di `PROJECT.md`.
- Versi draft: `drafts/<bagian>-vNN.md`; jangan menimpa versi lama.

## Definisi "selesai"
Bagian naskah dianggap selesai bila: (a) semua klaim punya bukti terverifikasi, (b) lolos `CHECKLIST-PEDOMAN.md`, (c) sudah diuji oleh `reviewer-simulation`, (d) angka bisa ditelusuri ke skrip + data.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="SOUL.md">
# SOUL.md — Karakter & Standar Epistemik Agent

## Peran
Anda adalah **mitra riset yang skeptis namun suportif** — gabungan asisten peneliti, reviewer internal, dan editor.
Anda membantu mahasiswa menghasilkan karya yang kuat di mata juri, **tanpa** mengorbankan kejujuran ilmiah.

## Nilai inti
1. **Empirisme di atas retorika.** Kalimat yang indah tanpa bukti lebih buruk daripada kalimat sederhana dengan bukti.
2. **Ketidakpastian dilaporkan, bukan disembunyikan.** Gunakan kata "mengindikasikan", "konsisten dengan", "belum cukup bukti" secara tepat.
3. **Falsifikasi.** Untuk setiap hipotesis, tanyakan: *apa yang akan membuktikannya salah?*
4. **Reproduksibilitas.** Orang lain harus bisa mengulang langkah dan mendapat hasil serupa.
5. **Kerendahan hati.** Akui batas pengetahuan; jangan menebak demi terdengar yakin.
6. **Mahasiswa tetap penulisnya.** Anda memperkuat penalaran mereka, bukan menggantikannya. Jelaskan *mengapa* di balik tiap saran supaya mereka belajar.

## Gaya komunikasi
- Berlapis: **konsep → teknis → langkah praktis**.
- Ringkas dan terstruktur; gunakan tabel/diagram bila membantu perbandingan.
- Jujur dan konstruktif: kritik dengan alasan + perbaikan konkret, bukan sekadar "kurang bagus".
- Jangan menjilat. Jika ide lemah, katakan dengan sopan dan tawarkan alternatif.

## Standar bukti (hierarki, dari kuat ke lemah)
1. Meta-analisis / systematic review bereputasi
2. Studi eksperimental/RCT, studi empiris dengan metode jelas, peer-reviewed
3. Studi observasional, dataset publik terdokumentasi
4. Laporan teknis/standar resmi (ISO, RFC, NIST, BPS, dsb.)
5. Preprint (tandai sebagai belum peer-review)
6. Opini ahli, artikel populer, blog → **hanya konteks, bukan bukti utama**

## Hal yang harus ditolak/dikoreksi secara aktif
- Permintaan membuat data "dummy" untuk dipresentasikan sebagai hasil nyata.
- Sitasi yang tidak bisa dilacak.
- Kesimpulan yang melampaui data (overclaiming), kausalitas dari korelasi, generalisasi dari sampel kecil.
- Plagiarisme dan parafrase tanpa atribusi.

## Penggunaan AI dalam karya
Bantu pengguna mencatat penggunaan AI secara transparan di `MEMORY.md` (apa yang dibantu, apa yang diverifikasi manual), karena kebijakan penggunaan AI pada program/lomba dapat berubah — **cek pedoman tahun berjalan**.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="USER.md">
# USER.md — Profil Pengguna

- *Nama panggilan:* Ibin, Radit, Hamzah
- *Status:* Mahasiswa, Indonesia
- *Bidang minat/riset:* teknik elektro · instrumentasi & sensor · elektronika daya / BMS · jaringan komputer · AI/ML · telekomunikasi & RF
- *Tujuan jangka panjang:* publikasi di jurnal internasional
- *Skema PKM yang dibidik:* PKM KC
- *Anggota tim & peran:* Muhammad Muhibbin (Ketua Tim), Sahra Raditiya Fadillah (Anggota Tim), Syahbudin Hamzah Hasan (Anggota Tim)
- *Dosen pendamping:* Endah Setyowati S.T., M.T.

## Preferensi kerja
- Bahasa: Indonesia
- Penjelasan: berlapis (konseptual → teknis)
- Output favorit: template, tabel perbandingan, diagram, langkah yang bisa langsung dieksekusi
- Tingkat detail teknis: Menengah
- Hal yang ingin dihindari agent: 
  - Halusinasi referensi, angka, dan DOI fiktif
  - Gaya bahasa AI klise ("era digitalisasi", retorika panjang tanpa substansi)
  - Menyembunyikan keterbatasan sistem atau kelemahan ide
  - Menulis kesimpulan hasil sebelum data/skrip di analysis/ ada
  - Merancang arsitektur sistem yang tidak realistis untuk timeline & anggaran PKM
  - Mengubah file data mentah secara langsung tanpa skrip

## Sumber daya
- Perangkat/komputasi: [ISI — laptop, GPU, cloud, lab kampus]
- Bahasa/tools analisis: [ISI — Python, R, SPSS, dsb.]
- Akses jurnal (VPN/perpustakaan kampus): [ISI]
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="MEMORY.md">
# MEMORY.md — Keputusan & Fakta Tetap

> Hanya catat hal yang **sudah disepakati**. Agent menambahkan baris baru; jangan hapus riwayat, beri tanda `(DIGANTI)`.

## Keputusan proyek
| Tanggal | Keputusan | Alasan | Dampak |
|---|---|---|---|
| 2026-11-21 | Memilih skema PKM-KC (Karsa Cipta) | Fokus pada kreasi berbasis karsa dan nalar, menghasilkan prototipe fungsional/sistem di bidang IT (AI, jaringan, keamanan, atau multimedia) | Luaran utama wajib berupa prototipe fungsional yang siap uji; metodologi berfokus pada rekayasa & pengujian sistem |
| 2026-11-21 | Adopsi Pedoman PKM 2026 | Dokumen resmi PANDUAN-PKM-2026_versi_full.pdf diekstraksi ke CHECKLIST-PEDOMAN dan REVIEWER-RUBRIC | Aturan baku terkunci: Bagian inti maks 10 hlm, tanpa cover/pengesahan di PDF, sitasi Harvard, plafon Belmawa 6-8 jt + PT maks 2 jt, larangan item biaya >1 jt |

## Fakta terverifikasi tentang proyek
- Tim terdiri dari 3 mahasiswa: Muhammad Muhibbin (Ketua Tim), Sahra Raditiya Fadillah (Anggota Tim), Syahbudin Hamzah Hasan (Anggota Tim).
- Dosen Pendamping: Endah Setyowati S.T., M.T.
- Skema terdaftar: PKM-KC (Karsa Cipta) untuk persiapan siklus PKM 2027.
- Bidang fokus integrasi: Teknik Elektro (Instrumentasi Sensor, Power Electronics/BMS, Sirkuit Elektronika), Computer Science (AI/TinyML, Rekayasa Perangkat Lunak), dan Teknik Telekomunikasi (Jaringan & RF). Teori fisika elektromagnetik & propagasi gelombang digunakan murni sebagai dasar referensi teknis rekayasa sistem.
- Tahap saat ini: Penyiapan seleksi awal tingkat fakultas / kampus daerah sebelum eskalasi ke universitas dan nasional.
- Basis acuan: Menggunakan Pedoman PKM 2026 sebagai standar baku mutu dan format sementara hingga pedoman resmi 2027 terbit.

## Penggunaan AI (transparansi)
| Tanggal | Bagian | Bantuan AI | Verifikasi manusia |
|---|---|---|---|
| 2026-11-21 | Setup & Ekstraksi Pedoman | Ekstraksi template bootstrap, parsing aturan PKM-KC 2026 dari PANDUAN-PKM-2026_versi_full.pdf | Dicek dan divalidasi kesesuaian klausul batas halaman, format, anggaran, dan bobot penilaian |

## Pelajaran / kesalahan yang jangan diulang
- Jangan memasukkan halaman sampul atau pengesahan ke dalam berkas PDF proposal utama.
- Jangan menganggarkan item alat/bahan satuan melebihi Rp 1.000.000 per unit (penyebab gugur administrasi Belmawa).
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="00-project/PROJECT.md">
# PROJECT.md — Sumber Kebenaran Proyek

## Identitas
- **Judul kerja:** [ISI]
- **Skema PKM:** PKM-KC (Karsa Cipta)
- **Bidang Keilmuan:** Teknik Elektro / Teknik Telekomunikasi & Computer Science
- **Tahun/periode:** 2027
- **Tenggat internal / resmi:** Seleksi Internal Fakultas / Kampus Daerah (Menuju PKM 2027 Nasional)

## Masalah (problem statement)
- **Konteks:** [ISI]
- **Kesenjangan (gap) yang bisa dibuktikan:** [ISI — didukung min. 2–3 sumber di EVIDENCE-LEDGER]
- **Siapa yang dirugikan & seberapa besar:** [ISI — kuantifikasi bila ada]

## Tujuan & Hipotesis
- **Tujuan umum:** [ISI]
- **Tujuan khusus (terukur):** 1. [ISI] 2. [ISI]
- **Hipotesis (H1, H0):** [ISI]
- **Kriteria keberhasilan (angka/ambang):** [ISI]

## Solusi / Inovasi
- **Deskripsi:** [ISI]
- **Kebaruan dibanding yang sudah ada:** [ISI — bandingkan dengan min. 3 pendekatan terkini]
- **Alasan kenapa seharusnya berhasil (mekanisme):** [ISI]

## Metode ringkas
- **Desain:** [ISI — eksperimen / studi kasus / pengembangan sistem / survei / dst.]
- **Data/sampel:** [ISI]
- **Variabel / metrik evaluasi:** [ISI]
- **Baseline pembanding:** [ISI]
- **Analisis:** [ISI]

## Luaran
- Wajib menurut pedoman: Laporan Kemajuan, Laporan Akhir, Prototipe Fungsional Siap Uji, Akun Media Sosial
- Tambahan (artikel/jurnal/HKI/prototipe): [ISI]

## Risiko & mitigasi
| Risiko | Probabilitas | Dampak | Mitigasi |
|---|---|---|---|
| [ISI] | | | |

## Etika & kepatuhan
- Persetujuan responden / data pribadi: [ISI]
- Lisensi dataset & perangkat lunak: [ISI]
- Keamanan (mis. uji keamanan hanya pada lingkungan yang diizinkan): [ISI]

## Gaya sitasi & template
- Gaya Sitasi: Harvard style (nama belakang, tahun, alfabetis) sesuai Pedoman PKM 2026
- Format Naskah: TNR 12, spasi 1.15, margin 4-3-3-3, bagian inti maks. 10 halaman (tanpa cover/pengesahan)
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="00-project/TIMELINE.md">
# TIMELINE.md

> Tanggal resmi (pengusulan, seleksi, pelaksanaan, monev, PIMNAS bila relevan) **wajib diambil dari panduan/pedoman resmi**.

| Fase | Milestone | Deadline | PIC | Status | Bukti selesai |
|---|---|---|---|---|---|
| 0. Setup | Workspace & pedoman terunduh | [ISI] | | ☐ | |
| 1. Ideasi | Problem statement + gap terbukti | [ISI] | | ☐ | EVIDENCE-LEDGER ≥ [N] sumber |
| 2. Desain | Metode & hipotesis dikunci | [ISI] | | ☐ | PROJECT.md final |
| 3. Proposal | Draft lengkap + RAB | [ISI] | | ☐ | Lolos checklist pedoman |
| 4. Review | Simulasi reviewer + revisi | [ISI] | | ☐ | REVIEW-LOG |
| 5. Submit | Unggah & verifikasi | [ISI] | | ☐ | Bukti unggah |
| 6. Pelaksanaan | Pengumpulan data & analisis | [ISI] | | ☐ | EXPERIMENT-LOG |
| 7. Laporan | Laporan kemajuan/akhir | [ISI] | | ☐ | |
| 8. Luaran | Artikel/HKI/dsb. | [ISI] | | ☐ | |

## Buffer
Sisakan ≥ 20% waktu sebelum tiap tenggat untuk revisi dan kegagalan teknis.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="00-project/PITCH-DECK.md">
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
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="10-pedoman/CHECKLIST-PEDOMAN.md">
# CHECKLIST-PEDOMAN.md

> Sumber: Pedoman Program Kreativitas Mahasiswa (PKM) Tahun 2026 — Buku Panduan Umum & Petunjuk Teknis PKM-KC (`10-pedoman/PANDUAN-PKM-2026_versi_full.pdf`)

## Ketentuan umum
| Aspek | Ketentuan menurut pedoman | Halaman/Pasal |
|---|---|---|
| Skema yang dipilih & definisinya | PKM Karsa Cipta (PKM-KC): Karya berupa hasil konstruksi karsa yang fungsional, siap uji, dan non-generik (belum ada produk dengan spesifikasi identik di pasar). | Hlm. 4, 78, 80 |
| Syarat tim (jumlah, jenjang, dosen pendamping) | 3–5 mahasiswa aktif jenjang D-3, D-4, atau S-1. Disarankan berasal dari minimal 2 angkatan berbeda. Kolaborasi lintas prodi/bidang sangat dianjurkan. Dosen pendamping 1 orang ber-NIDN/NIDK relevan. Pengusul tidak boleh ikut PPK Ormawa/P2MW di tahun yang sama. | Hlm. 10, 83 |
| Syarat administrasi & penamaan berkas | Berkas PDF diunggah ke simbelmawa dengan format `namaketua_namaPT_PKM-KC.pdf`. **TIDAK ADA halaman sampul dan halaman pengesahan** dalam file PDF proposal. Judul maks. 20 kata, huruf kapital, bahasa Indonesia, tanpa singkatan non-baku. | Hlm. 84-85 |
| Sistematika proposal/naskah | DAFTAR ISI, DAFTAR GAMBAR (jika ada), DAFTAR TABEL (jika ada), DAFTAR LAMPIRAN, BAB 1 PENDAHULUAN, BAB 2 TINJAUAN PUSTAKA, BAB 3 TAHAP PELAKSANAAN, BAB 4 BIAYA DAN JADWAL KEGIATAN, DAFTAR PUSTAKA, LAMPIRAN (1–6). | Hlm. 85-88 |
| Batas halaman | Bagian Inti (Bab 1 s.d. Daftar Pustaka) **maksimum 10 (sepuluh) halaman**. Penomoran Daftar Isi romawi kecil (i, ii..) di kanan bawah; Bagian Inti angka arab (1, 2..) di kanan atas dimulai angka 1 dari Bab 1. | Hlm. 84-85 |
| Format naskah | Font Times New Roman 12, spasi 1.15, rata kiri-kanan (justify), kertas A4 satu kolom, margin kiri 4 cm, kanan 3 cm, atas 3 cm, bawah 3 cm. Gaya sitasi Harvard style. | Hlm. 85, 88 |
| Plafon & komponen biaya | Belmawa: Rp 6.000.000 s.d. Rp 8.000.000. Dana pendamping PT (wajib): maks. Rp 2.000.000 (tunai/barang). Dana mitra (opsional): maks. Rp 1.000.000. Komposisi: Bahan habis pakai maks. 60%, Sewa & jasa maks. 15%, Transport lokal maks. 30%, Lain-lain maks. 15%. | Hlm. 83-84, 87 |
| Luaran wajib | 1. Laporan Kemajuan, 2. Laporan Akhir, 3. Prototipe fungsional siap uji, 4. Akun Media Sosial. | Hlm. 10, 81 |
| Kebijakan GenAI & Orisinalitas | Mengikuti Panduan GenAI Ditbelmawa (transparansi penggunaan AI), uji similaritas/Turnitin (direkomendasikan < 10%). | Lampiran 6 & Panduan Umum |

## Kriteria penilaian resmi (Formulir Penilaian Proposal Lampiran 7 Hlm. 98)
| Kriteria | Bobot | Cara kami memenuhinya | Bukti di naskah |
|---|---|---|---|
| **Kreativitas: Gagasan** (orisinalitas, unik, dan manfaat masa depan) | 20 | Tunjukkan pembeda unik dibanding produk/riset yang sudah ada di pasar/literatur melalui tabel komparatif. | Bab 1 (Tabel 1.1 & Latar Belakang) |
| **Kreativitas: Kemutakhiran IPTEK** yang diadopsi | 20 | Adopsi teknologi mutakhir (mis. AI model terbaru, arsitektur sensor canggih, fusi data). | Bab 1 & Bab 2 |
| **Kesesuaian Tahap Pelaksanaan** | 15 | Flowchart tahapan terukur, acceptance criteria kuantitatif (akurasi, latensi, toleransi error), UAT pengguna. | Bab 3 |
| **Potensi Program: Kontribusi produk** terhadap solusi & perkembangan IPTEK | 25 | Buktikan masalah riil terselesaikan secara solutif melalui prototipe yang siap diuji. | Bab 1 & Bab 3 |
| **Potensi Publikasi Ilmiah / Kekayaan Intelektual** | 10 | Targetkan draf paten/desain industri atau artikel ilmiah terindeks sebagai luaran tambahan. | Bab 1 (Sub 1.6) |
| **Penjadwalan Kegiatan & Personalia** | 5 | Bar chart 3–4 bulan realistis, pembagian peran 3–5 anggota jelas tanpa tumpang tindih. | Bab 4 & Lampiran 5 |
| **Penyusunan Anggaran Biaya** | 5 | Rinci, wajar, patuh batas persentase, dan tidak ada komponen yang dilarang. | Bab 4 & Lampiran 4 |

## Larangan Keras / Penyebab Gugur Administrasi
1. Mengunggah proposal dengan halaman sampul (cover) dan/atau halaman pengesahan di dalam file PDF.
2. Panjang Bagian Inti (Bab 1 s.d. Daftar Pustaka) melebihi 10 halaman.
3. Jumlah anggota di luar batas 3–5 orang atau pengusul terdaftar di PPK Ormawa/P2MW.
4. Dana usulan ke Belmawa di luar batas Rp 6.000.000 – Rp 8.000.000.
5. Pembelian alat/bahan > Rp 1.000.000 per item dalam anggaran.
6. Memasukkan pos biaya honorarium tim/dosen/narasumber, konsumsi, hadiah.
7. Memasukkan biaya sewa PC, laptop, printer, ponsel, kamera, tempat/aula.
8. Pembelian flashdisk, harddisk, atau media penyimpanan data.
9. Pembelian kuota internet > Rp 100.000 per bulan per tim.
10. Biaya seminar atau biaya publikasi jurnal ilmiah di dalam RAB.
11. Surat pernyataan ketua tim tidak bermeterai Rp 10.000 atau format lampiran tidak sesuai standar.

## Pemeriksaan akhir sebelum submit
- [ ] Berkas proposal PDF tanpa cover dan lembar pengesahan.
- [ ] Bagian Inti persis $\le 10$ halaman (dimulai angka arab 1 di Bab 1, kanan atas).
- [ ] Format: TNR 12, spasi 1.15, margin 4-3-3-3, rata kiri-kanan.
- [ ] Format penamaan file: `namaketua_namaPT_PKM-KC.pdf`.
- [ ] Sitasi menggunakan Harvard style dan konsisten timbal balik antara teks dan Daftar Pustaka.
- [ ] Anggaran Belmawa Rp 6–8 juta + dana pendamping PT maks Rp 2 juta (tidak ada item dilarang).
- [ ] Surat pernyataan ketua bermeterai Rp 10.000 dan bertanda tangan basah/asli.
- [ ] Similaritas lolos uji plagiasi.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="20-literatur/EVIDENCE-LEDGER.md">
# EVIDENCE-LEDGER.md — Daftar Bukti Terverifikasi

> Satu baris = satu bukti spesifik. Hanya masukkan sumber yang **sudah dibuka & dibaca langsung** (bukan sekadar dari ringkasan AI).

| ID | Sitasi lengkap | DOI/URL | Jenis (SR/RCT/empiris/standar/preprint) | Temuan/fakta spesifik | Halaman/Tabel | Konteks & batasan | Terverifikasi (tgl, oleh) |
|---|---|---|---|---|---|---|---|
| E001 | IEEE / Scopus Disaster Communications Study on LoRa Multi-Hop Mesh (2022-2024) | https://semanticscholar.org / IEEE Xplore | Studi Empiris (Simulasi & Lab) | Topologi multi-hop LoRa mesh meningkatkan Packet Delivery Ratio (PDR) di area terhalang dari ~40% menjadi 70-80%, namun lonjakan traffic bencana menyebabkan tabrakan paket (collision) drastis dan latensi tinggi pada Spreading Factor besar (SF11/SF12). | Bagian Hasil & Evaluasi PDR | Pengujian terbatas pada modulasi tunggal LoRa tanpa mekanisme pemisahan band frekuensi lokal. | 2026-11-21, Tim PKM |
| E002 | Hybrid LoRa and ESP-NOW Architecture in Off-Grid IoT Networks (2023-2024) | https://lorameshdevices.com / ResearchGate | Studi Desain & Implementasi | Penggabungan ESP-NOW (2.4 GHz, 1 Mbps, zero-handshake) untuk klaster mikro lokal dan LoRa (Sub-GHz) sebagai bridge backbone mampu mereduksi beban kanal frekuensi radio jarak jauh secara signifikan. | Bagian Arsitektur Topologi | Mayoritas implementasi bersifat statis (gateway tetap) dan belum mengadopsi mekanisme penjadwalan antrean prioritas QoS darurat. | 2026-11-21, Tim PKM |
| E003 | Kementerian Komunikasi dan Digital RI (Kominfo) — Regulasi Spektrum Frekuensi Radio LPWAN / ISM Band Indonesia | Permen Kominfo No. 1 / Regulasi Spektrum 920-923 MHz | Standar Regulasi Resmi | Alokasi frekuensi resmi untuk teknologi LPWAN (termasuk LoRa) di Indonesia berada pada rentang 920–923 MHz dengan batasan daya pancar maksimal dan kepatuhan duty cycle. | Ketentuan Teknis Alokasi Frekuensi | Membatasi durasi transmisi berkelanjutan di udara (airtime limit). | 2026-11-21, Tim PKM |
| E004 | Disaster Victim Telemetry using ESP32 Standalone Captive Portal (2023) | IJRAR / IEEE Regional Conference | Studi Empiris | ESP32 mampu menjalankan web server internal dan DNS redirect (captive portal) mandiri tanpa internet, memungkinkan ponsel korban mengirim formulir identitas dan koordinat secara instan. | Implementasi Firmware | Jangkauan Wi-Fi captive portal terbatas radius 50-100 meter dari node utama. | 2026-11-21, Tim PKM |

## Aturan
- ID tidak pernah dipakai ulang.
- Tulis temuan **dengan kata sendiri** + angka persis dari sumber.
- Catat batasan (populasi, dataset, kondisi) agar tidak overclaim.
- Sumber yang gagal diverifikasi dipindah ke bagian bawah dengan label `DITOLAK` + alasan.

## Ditolak / tidak bisa diverifikasi
| Sumber | Alasan |
|---|---|
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="30-riset/CLAIM-MATRIX.md">
# CLAIM-MATRIX.md — Klaim ↔ Bukti ↔ Status

| ID | Klaim (satu kalimat, dapat diuji) | Jenis | Bukti pendukung | Bukti yang menentang/membatasi | Kekuatan | Status | Lokasi di naskah |
|---|---|---|---|---|---|---|---|
| C001 | Jaringan seluler konvensional di Indonesia rentan runtuh total pada jam-jam awal bencana, menyebabkan isolasi komunikasi pencarian dan penyelamatan korban. | Latar Belakang | E001, Data BNPB / IRBI | Jaringan radio darurat analog (HT) masih bisa beroperasi terbatas | Kuat | Terverifikasi | Bab 1 Pendahuluan |
| C002 | Sistem LoRa mesh murni (single radio) mengalami degradasi Packet Delivery Ratio (PDR) dan latensi tinggi saat terjadi lonjakan transmisi pesan darurat secara serentak. | Metodologis / Latar | E001, E003 | PDR membaik jika kepadatan node sangat rendah | Kuat | Terverifikasi | Bab 1 & Bab 2 Tinjauan Pustaka |
| C003 | Arsitektur hibrida ESP-NOW (2.4 GHz) dan LoRa (920-923 MHz) mampu membagi beban lalu lintas komunikasi antara klaster lokal korban dan transmisi jarak jauh posko SAR. | Metodologis / Solusi | E002, E004 | Memerlukan sinkronisasi dual-radio di tingkat firmware (RTOS) | Sedang | Perlu data uji | Bab 1 (Kebaruan) & Bab 3 |
| C004 | Mekanisme antrean QoS adaptif pada node bridge dapat memprioritaskan paket sinyal darurat (SOS dan koordinat GPS) agar terkirim dengan latensi $\le 2$ detik melintasi multi-hop. | Solusi / Hipotesis | E001, E002 | Tergantung jumlah hop dan kondisi interferensi RF | Hipotesis | Perlu data uji (EXP) | Bab 1 & Bab 3 |

## Skala kekuatan
- **Kuat:** ≥2 sumber independen berkualitas tinggi **atau** hasil eksperimen sendiri dengan analisis tepat
- **Sedang:** 1 sumber kuat atau beberapa sumber lemah konsisten
- **Lemah:** inferensi/opini → wajib dilunakkan bahasanya atau dibuang

## Aturan
- Klaim "Hasil" hanya boleh `Terverifikasi` bila terhubung ke `EXP-xxx` dan skrip analisis.
- Klaim berstatus `Perlu data` tidak boleh muncul sebagai fakta di naskah.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="30-riset/EXPERIMENT-LOG.md">
# EXPERIMENT-LOG.md

> Catat **sebelum** dan **sesudah** setiap eksperimen/pengumpulan data. Ini inti reproduksibilitas dan bahan bab Metode/Hasil.

## Template entri

### EXP-001 — [judul singkat]
- **Tanggal & pelaksana:** YYYY-MM-DD, [nama]
- **Pertanyaan/hipotesis yang diuji:** [H1 …]
- **Prediksi sebelum dijalankan (pre-registration ringan):** [ISI]
- **Setup:** perangkat keras/lunak + versi, parameter, seed acak, dataset (versi/hash), commit/skrip
- **Prosedur (langkah ulang-bisa):**
  1. …
- **Metrik & cara hitung:** [ISI]
- **Hasil mentah:** lokasi file `30-riset/data/...`
- **Hasil analisis:** `30-riset/analysis/...` (tabel/gambar)
- **Anomali/kegagalan:** [ISI — jangan dihapus]
- **Interpretasi (dipisah dari hasil):** [ISI]
- **Klaim terkait:** C00x
- **Langkah berikutnya:** [ISI]
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="40-naskah/OUTLINE.md">
# OUTLINE.md — Kerangka Naskah

> **Sistematika final mengikuti pedoman skema yang dipilih.** Berikut kerangka kerja generik; sesuaikan/ganti.

| Bagian | Tujuan argumentatif | Klaim yang dipakai | Bukti | Status draft |
|---|---|---|---|---|
| Abstrak / Ringkasan | Masalah → metode → hasil/target → dampak | | | ☐ |
| Pendahuluan / Latar Belakang | Urgensi + gap terbukti | C001… | E001… | ☐ |
| Tujuan & Luaran | Terukur | | | ☐ |
| Tinjauan Pustaka | Posisi karya di antara penelitian lain | | | ☐ |
| Metode | Dapat direproduksi, sesuai tujuan | | EXP | ☐ |
| Hasil & Analisis (atau Target Hasil) | Data → interpretasi → keterbatasan | | | ☐ |
| Pembahasan | Mengapa terjadi, implikasi, perbandingan dengan literatur | | | ☐ |
| Kesimpulan & Saran | Menjawab tujuan, tidak melampaui data | | | ☐ |
| Daftar Pustaka | Semua sitasi terverifikasi | | | ☐ |
| RAB & Jadwal | Realistis & konsisten dengan metode | | | ☐ |
| Lampiran | Data, instrumen, bukti pendukung | | | ☐ |

## Alur argumen utama (satu paragraf)
Masalah **[X]** terbukti besar (E00x) → pendekatan yang ada **gagal pada [Y]** (E00x) → kami usulkan **[Z]** dengan mekanisme **[M]** → diuji dengan **[metode]** pada **[data]** → kriteria sukses **[ambang]**.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="50-review/REVIEWER-RUBRIC.md">
# REVIEWER-RUBRIC.md — Rubrik Penilaian Resmi PKM-KC 2026

> Disesuaikan persis dengan **Lampiran 7: Formulir Penilaian Proposal PKM-KC** (Panduan PKM 2026, Hlm. 98).
> Skala Skor: 1 = Buruk; 2 = Sangat kurang; 3 = Kurang; 5 = Cukup; 6 = Baik; 7 = Sangat baik.
> Nilai = Bobot $\times$ Skor (Maksimal 700).

| No | Kriteria Penilaian | Bobot | Pertanyaan Evaluasi Reviewer | Skor (1-7) | Nilai | Catatan & Perbaikan Kritis |
|---|---|---|---|---|---|---|
| 1.1 | **Kreativitas Gagasan:** Orisinalitas, keunikan, dan kemanfaatan masa depan | 20 | Apakah ide benar-benar orisinal/non-generik? Apakah ada perbandingan komparatif dengan produk/riset terdahulu? | | | |
| 1.2 | **Kreativitas IPTEK:** Kemutakhiran IPTEK yang diadopsi | 20 | Apakah teknologi yang digunakan mutakhir (state-of-the-art), relevan, dan memiliki justifikasi ilmiah yang kuat? | | | |
| 2 | **Kesesuaian Tahap Pelaksanaan** | 15 | Apakah alur perancangan, pembuatan, dan pengujian logis? Apakah ada acceptance criteria kuantitatif dan UAT pengguna? | | | |
| 3.1 | **Potensi Program: Kontribusi Solusi** terhadap masalah & IPTEK | 25 | Apakah prototipe mampu memecahkan masalah riil target pengguna secara signifikan? Apakah prototipe fungsional dan siap uji? | | | |
| 3.2 | **Potensi Luaran Tambahan:** Publikasi Ilmiah / Kekayaan Intelektual | 10 | Apakah karya memiliki prospek dipatenkan (HKI/Desain Industri) atau dipublikasikan di prosiding/jurnal bereputasi? | | | |
| 4 | **Penjadwalan & Personalia:** Kesesuaian waktu dan tim | 5 | Apakah alokasi waktu 3–4 bulan realistis? Apakah pembagian tugas 3–5 anggota jelas, seimbang, dan tidak tumpang tindih? | | | |
| 5 | **Penyusunan Anggaran Biaya:** Rinci, wajar, dan jelas peruntukannya | 5 | Apakah total dana Belmawa Rp 6–8 juta? Apakah patuh pada batas persentase (bahan maks 60%, sewa maks 15%, transport maks 30%, lain maks 15%) dan bebas dari pos dilarang? | | | |
| **Total** | | **100** | | | **/700** | |

---

## 10 Pertanyaan Juri / Reviewer yang Sering Menggugurkan PKM-KC
1. **Kebaruan:** *Apa perbedaan mendasar prototipe Anda dengan sistem/aplikasi yang sudah dijual di e-commerce atau hasil riset terdahulu?*
2. **Kesiapterapan (TRL):** *Apakah prototipe ini benar-benar fungsional dan siap diuji lapangan, atau baru sebatas simulasi/konsep di atas kertas?*
3. **Justifikasi Komponen:** *Mengapa memilih komponen/arsitektur X daripada alternatif Y yang lebih murah/stabil?*
4. **Metrik Keberhasilan:** *Bagaimana Anda membuktikan alat ini bekerja? Apa angka/ambang batas kuantitatif pengujiannya?*
5. **Keamanan & Kenyamanan Pengguna:** *Apakah prototipe aman jika digunakan oleh manusia secara langsung (panas, radiasi, beban mekanis, privasi data)?*
6. **Keterbatasan Alat:** *Dalam kondisi lingkungan apa prototipe Anda akan gagal bekerja, dan bagaimana Anda mengantisipasinya?*
7. **Kewajaran Anggaran:** *Kenapa membeli bahan X? Apakah ada item di atas Rp 1.000.000 per unit atau komponen yang melanggar aturan Belmawa?*
8. **Validasi Pengguna:** *Apakah target pengguna sudah pernah dilibatkan dalam wawancara/survei kebutuhan awal?*
9. **Kekompakan Tim:** *Apa kontribusi spesifik setiap anggota tim dan bagaimana pembagian jam kerjanya?*
10. **Keberlanjutan Pasca-Program:** *Setelah lolos PIMNAS, ke mana prototipe ini akan dibawa (hilirisasi, paten, atau PKM-KI tahun depan)?*
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="50-review/REVIEW-LOG.md">
# REVIEW-LOG.md

| Tanggal | Versi naskah | Reviewer (agent/manusia) | Temuan kritis | Tindakan | Status |
|---|---|---|---|---|---|
| YYYY-MM-DD | v01 | | | | ☐ |
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/argumentation-cer/SKILL.md">
---
name: argumentation-cer
description: Gunakan untuk menyusun argumen ilmiah dengan struktur Claim–Evidence–Reasoning (CER) plus bantahan, agar setiap paragraf kuat dan dapat diuji juri.
---

# Argumentation (CER + Rebuttal)

## Struktur satu paragraf argumen
1. **Claim** — satu kalimat spesifik dan dapat diuji.
2. **Evidence** — data/sitasi spesifik (angka, kondisi) dengan ID ledger.
3. **Reasoning** — *mengapa* bukti itu mendukung klaim (mekanisme/logika).
4. **Qualifier** — batas berlaku (populasi, kondisi).
5. **Rebuttal** — keberatan terkuat + tanggapan (atau akui sebagai keterbatasan).

## Uji kualitas
- Apakah klaim bisa salah? Jika tidak → terlalu kabur.
- Apakah bukti benar-benar relevan (bukan sekadar topik sama)?
- Apakah ada penjelasan alternatif? Sudahkah dibahas?
- Apakah kata-kata sesuai kekuatan bukti? (membuktikan ≠ mengindikasikan ≠ menyarankan)

## Pola kesalahan logika untuk diwaspadai
Korelasi=kausalitas · generalisasi tergesa · argumen otoritas · false dilemma · straw man · circular reasoning · survivorship bias · base-rate neglect.

## Hasil
Paragraf siap-naskah + baris di `CLAIM-MATRIX.md`.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/budget-rab/SKILL.md">
---
name: budget-rab
description: Gunakan untuk menyusun Rencana Anggaran Biaya (RAB) yang realistis, dapat dipertanggungjawabkan, dan konsisten dengan metode serta aturan pedoman.
---

# Budget / RAB

## Prinsip
- Setiap pos biaya harus **terhubung ke kegiatan di metode** dan **sesuai komponen yang diizinkan pedoman** (cek `CHECKLIST-PEDOMAN.md`). Jangan menebak plafon/persentase.
- Gunakan harga yang dapat ditelusuri (katalog/marketplace/surat penawaran); simpan bukti di `00-project/`.

## Tabel
| No | Komponen | Uraian & kaitan ke kegiatan | Volume | Satuan | Harga satuan | Subtotal | Sumber harga |
|---|---|---|---|---|---|---|---|

## Pemeriksaan
- Total = jumlah subtotal; sesuai plafon pedoman.
- Tidak ada pos yang tak terhubung ke metode, atau metode yang butuh sumber daya tapi tak dianggarkan.
- Skenario pemotongan anggaran: pos mana yang diprioritaskan.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/citation-verification/SKILL.md">
---
name: citation-verification
description: Gunakan sebelum sitasi masuk naskah, dan saat audit akhir. Memastikan setiap referensi nyata, tepat, dan mendukung klaim.
---

# Citation Verification

## Checklist per sumber
1. **Eksistensi:** DOI/URL resolve; judul, penulis, tahun, venue cocok.
2. **Integritas:** bukan jurnal predator / retracted (cek Retraction Watch, indeksasi, SINTA/Scopus).
3. **Relevansi:** isi benar-benar mendukung klaim (baca bagian terkait, bukan hanya abstrak).
4. **Akurasi angka:** angka/kutipan di naskah = angka di sumber (catat halaman/tabel).
5. **Format:** sesuai gaya sitasi dari pedoman.
6. **Konsistensi:** setiap sitasi dalam teks ada di daftar pustaka, dan sebaliknya.

## Penanganan hasil
- Lolos → `EVIDENCE-LEDGER.md` dengan tanggal verifikasi.
- Gagal/ragu → tulis `[BELUM TERVERIFIKASI]`, jangan dipakai sebagai fakta.
- Referensi yang disarankan AI **selalu dianggap tidak valid sampai dicek manual**.

## Audit akhir
Ambil acak 20% sitasi dan telusuri ulang ke sumber asli; bila ada satu kesalahan, audit 100%.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/data-analysis/SKILL.md">
---
name: data-analysis
description: Gunakan saat menganalisis data riset: pembersihan, statistik deskriptif/inferensial, visualisasi, dan interpretasi jujur. Semua angka harus keluar dari skrip.
---

# Data Analysis

## Prinsip
- Semua angka di naskah berasal dari skrip di `30-riset/analysis/`, dengan seed tetap dan versi library tercatat.
- Data mentah tidak diedit; pembersihan dilakukan lewat skrip yang terdokumentasi.

## Alur
1. **Audit data:** ukuran, tipe, missing, duplikat, outlier, distribusi, ketidakseimbangan kelas, potensi kebocoran.
2. **Deskriptif:** rata-rata/median, sebaran, tabel ringkas, visualisasi yang jujur (sumbu tidak menyesatkan).
3. **Pilih uji sesuai asumsi:** cek normalitas/varians; gunakan uji non-parametrik bila perlu.
4. **Inferensial:** laporkan statistik uji, p-value, **ukuran efek**, dan **interval kepercayaan** (bukan p-value saja).
5. **Ulangi untuk stabilitas:** beberapa seed / cross-validation / bootstrap; laporkan mean ± SD.
6. **Ablation & analisis galat:** komponen mana yang berkontribusi; kasus mana yang gagal dan mengapa.
7. **Sensitivitas:** apakah kesimpulan berubah jika asumsi/parameter diubah?
8. **Interpretasi:** pisahkan **hasil** (apa yang teramati) dari **makna** (apa artinya). Hindari kausalitas dari korelasi.
9. Tulis keterbatasan secara eksplisit.

## Format pelaporan
| Item | Isi |
|---|---|
| Pertanyaan | |
| Data & versi | |
| Metode/uji + alasan | |
| Hasil (angka + CI + efek) | |
| Interpretasi | |
| Keterbatasan | |
| Skrip & lokasi output | |

## Larangan
- Memilih-milih hasil (p-hacking / cherry-picking), membuang hasil negatif tanpa alasan tercatat.
- Mengevaluasi pada data latih; melaporkan satu run sebagai bukti kuat.
- Membuat data sintetis tanpa label jelas sebagai sintetis.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/idea-brainstorm-pkm/SKILL.md">
---
name: idea-brainstorm-pkm
description: >-
  Gunakan untuk menggali ide-ide PKM-KC yang anti-mainstream, berdasarkan gap riset terkini di Computer Science / Teknik Telekomunikasi, dengan konteks isu genting Indonesia. Menghasilkan: landscape riset, peta novelty, dan implementation plan awal.
---

# Idea Brainstorm for PKM-KC

## Kapan dipakai
Pada fase paling awal (zero-to-one), saat tim belum memiliki topik, untuk:
1. Memetakan kondisi riil yang mendesak (isu genting Indonesia yang terukur).
2. Mengidentifikasi gap teknologi yang terbuka berdasarkan literatur terbaru.
3. Merumuskan gagasan karsa cipta yang memenuhi kriteria PKM-KC: **orisinal, fungsional, siap uji, non-generik**.

## Proses Kerja
1. **Scan isu genting nasional** → padankan ke bidang CS/Telekomunikasi.
2. **Identifikasi gap teknologi** → cari paper 2022–2025 yang menunjukkan keterbatasan solusi sebelumnya.
3. **Formulasikan konsep prototipe** → spesifik pada mekanisme kebaruan (*novelty mechanism*).
4. **Rancang implementation plan** (Fase 0–3: Studi, Desain, Prototyping, Validasi) untuk timeline 3–4 bulan PKM.
5. **Susun daftar literatur awal** → masuk ke EVIDENCE-LEDGER.

## Output
- Peta Gagasan (ide, masalah, gap, kebaruan)
- Implementation Plan per fase
- Daftar kata kunci & sumber untuk proses literature-review lebih lanjut
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/literature-review/SKILL.md">
---
name: literature-review
description: Gunakan saat mencari, menyaring, dan mensintesis literatur untuk membuktikan gap dan kebaruan. Output masuk ke EVIDENCE-LEDGER.
---

# Literature Review

## Kapan dipakai
Menyusun latar belakang, tinjauan pustaka, atau membuktikan kebaruan.

## Proses
1. **Rumuskan pertanyaan** (PICO/PEO atau 1 kalimat) + kata kunci (sinonim EN/ID) + kriteria inklusi/eksklusi (tahun, bahasa, jenis studi).
2. **Cari** di sumber bereputasi (Scopus, Web of Science, IEEE Xplore, ACM DL, ScienceDirect, SINTA/Garuda, Google Scholar, arXiv sebagai preprint). Catat query & tanggal pencarian.
3. **Saring** judul → abstrak → teks penuh. Catat jumlah di tiap tahap (gaya PRISMA ringan).
4. **Ekstraksi** per sumber: tujuan, metode, data, metrik, hasil (angka), keterbatasan.
5. **Sintesis** per tema (bukan per paper): konsensus, kontradiksi, gap.
6. **Peta kebaruan:** tabel perbandingan karya Anda vs 3–7 pendekatan terdekat.
7. Masukkan hanya yang sudah dibaca ke `EVIDENCE-LEDGER.md`.

## Output
- Tabel ekstraksi · peta kebaruan · paragraf sintesis bersitasi ID ledger · daftar gap.

## Larangan
- Merangkum paper dari abstrak saja lalu mengklaim "sudah membaca".
- Menyebut "belum ada penelitian" tanpa log pencarian yang mendukung — gunakan "sepanjang penelusuran kami (query, tanggal) belum ditemukan…".
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/proposal-writing/SKILL.md">
---
name: proposal-writing
description: Gunakan untuk menulis/merevisi bagian proposal atau laporan PKM agar padat, runtut, bersitasi terverifikasi, dan sesuai pedoman.
---

# Proposal Writing

## Sebelum menulis
- Baca `CHECKLIST-PEDOMAN.md` dan `OUTLINE.md`; ketahui batas halaman & format.
- Pastikan klaim yang akan ditulis ada di `CLAIM-MATRIX.md` dengan status `Terverifikasi`.

## Prinsip penulisan
- **Piramida terbalik:** kesimpulan dulu, rincian kemudian.
- Satu paragraf = satu ide; kalimat pembuka = klaim.
- Kuantifikasi: gunakan angka dan satuan, bukan "sangat/banyak/signifikan" tanpa angka.
- Konsisten istilah & singkatan (definisikan di kemunculan pertama).
- Tulis target hasil sebagai **target terukur**, bukan seolah sudah tercapai (pada tahap proposal).
- Orisinalitas: parafrase dengan atribusi, jangan menyalin; cek similarity sebelum kirim.

## Alur kerja per bagian
1. Draft kasar dari klaim + bukti → 2. Rapikan argumen (`argumentation-cer`) → 3. Pangkas kata → 4. Cek sitasi (`citation-verification`) → 5. Cek pedoman → 6. Uji `reviewer-simulation`.

## Ringkasan/abstrak (urutan)
Masalah (berangka) → gap → solusi/metode → hasil atau target terukur → dampak. Tulis terakhir.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/reproducibility/SKILL.md">
---
name: reproducibility
description: Gunakan untuk memastikan hasil dapat diulang orang lain: lingkungan, versi, seed, struktur kode & data, dan dokumentasi.
---

# Reproducibility

## Checklist
- ☐ Lingkungan terkunci (`requirements.txt`/`environment.yml`/Docker) + versi OS & hardware
- ☐ Seed acak tetap dan dicatat
- ☐ Versi dataset (hash/tanggal unduh/lisensi) dicatat
- ☐ Satu perintah untuk menjalankan alur (`make run` / `run_all.sh`)
- ☐ Konfigurasi di file (bukan hard-coded), tersimpan per eksperimen
- ☐ Kode di version control (git), tag per versi naskah
- ☐ README: cara instal, cara jalankan, keluaran yang diharapkan
- ☐ Tabel/gambar di naskah dihasilkan otomatis dari skrip
- ☐ Orang lain (rekan tim) berhasil mengulang dari nol

## Ancaman umum
Kebocoran data · seed tidak tercatat · versi library berubah · preprocessing manual yang tidak terdokumentasi.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/research-design/SKILL.md">
---
name: research-design
description: Gunakan untuk merancang metode: hipotesis, variabel, baseline, sampel, metrik, ancaman validitas, dan rencana analisis sebelum data dikumpulkan.
---

# Research Design

## Langkah
1. **Pertanyaan → hipotesis** yang dapat difalsifikasi (H0/H1) + prediksi arah dan ukuran efek yang bermakna.
2. **Variabel:** independen, dependen, kontrol, pengganggu (confounder).
3. **Baseline & pembanding:** minimal satu baseline kuat + satu sederhana; samakan kondisi uji.
4. **Data/sampel:** sumber, ukuran, teknik sampling, pembagian train/validation/test (tanpa kebocoran data), perhitungan kecukupan sampel/power bila relevan.
5. **Metrik:** pilih sesuai tujuan (mis. ML: precision/recall/F1/AUC; jaringan: latency/throughput/packet loss/jitter; multimedia: PSNR/SSIM/MOS; keamanan: detection rate/false positive rate). Jelaskan alasannya.
6. **Rencana analisis (pre-specified):** uji statistik, ambang signifikansi, koreksi perbandingan ganda, ukuran efek + interval kepercayaan, ablation.
7. **Ancaman validitas:** internal, eksternal, konstruk, kesimpulan — dan mitigasinya.
8. **Etika & keamanan:** persetujuan, anonimisasi, lisensi data, ruang lingkup uji (hanya pada sistem yang berizin).
9. **Kriteria berhenti & kriteria gagal** ditentukan di awal.

## Output
Bagian Metode yang bisa direplikasi + tabel desain eksperimen → masuk `PROJECT.md` & `EXPERIMENT-LOG.md`.
</workspace_file>

<!-- ======================================================== -->
<workspace_file path="skills/reviewer-simulation/SKILL.md">
---
name: reviewer-simulation
description: Gunakan untuk menilai naskah seperti juri/reviewer yang kritis sebelum submit, memakai REVIEWER-RUBRIC dan kriteria resmi pedoman.
---

# Reviewer Simulation

## Peran
Bertindaklah sebagai reviewer **skeptis tapi adil**. Tujuan: menemukan kelemahan **sebelum** juri menemukannya.

## Langkah
1. Baca naskah tanpa membela penulis. Catat klaim tanpa bukti, loncatan logika, angka tidak konsisten.
2. Nilai per kriteria di `REVIEWER-RUBRIC.md` (skor + alasan + bukti kutipan lokasi).
3. Daftar **5 kelemahan terbesar**, urut dampak, masing-masing dengan perbaikan konkret.
4. Buat **10 pertanyaan juri tersulit** + draf jawaban berbasis bukti.
5. Periksa kepatuhan pedoman & konsistensi lintas bagian (abstrak ↔ metode ↔ RAB ↔ luaran).
6. Catat di `REVIEW-LOG.md`.

## Format keluaran
| Temuan | Lokasi | Tingkat (Kritis/Penting/Minor) | Perbaikan |
|---|---|---|---|

## Aturan
Kritik harus spesifik dan dapat ditindaklanjuti. Jangan memberi skor tinggi demi menyenangkan.
</workspace_file>
