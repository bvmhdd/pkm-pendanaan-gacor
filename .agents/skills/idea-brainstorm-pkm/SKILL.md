---
name: idea-brainstorm-pkm
description: >-
  Gunakan untuk menggali ide PKM-KC yang anti-mainstream dan belum tersaturasi,
  khususnya di ranah Teknik Elektro (sensor analog, BMS, HV, RF) × Computer
  Science (Edge AI/TinyML, embedded RTOS) × Teknik Telekomunikasi. Menghasilkan:
  peta kelayakan ide, mekanisme kebaruan, dan implementation plan konkret per fase
  yang realistis untuk timeline 3–4 bulan & anggaran Rp 6–8 juta PKM-KC.
---

# Idea Brainstorm for PKM-KC

## Kapan Dipakai
Fase paling awal (zero-to-one) atau saat tim perlu **pivot** dari topik yang sudah jenuh.

## Filter Anti-Saturasi (Jalankan Dulu Sebelum Mengusulkan Ide)
Tolak otomatis ide yang memiliki ciri berikut, kecuali ada mekanisme kebaruan yang sangat spesifik dan terukur:
- Topik LoRa / ESP32 + bencana alam / monitoring lingkungan generik
- Smart home / smart farming tanpa diferensiasi teknis nyata
- Aplikasi mobile / web biasa tanpa komponen hardware orisinal
- Sistem yang sudah ada produk komersialnya dengan spesifikasi identik (Meshtastic, RALIVIDE, dll.)
- Topik yang reviewer bisa cari >10 paper serupa dalam 2 menit di Google Scholar

## Kriteria Ide Layak PKM-KC
Ide lolos semua kriteria berikut:
1. **Orisinal & Non-Generik:** Tidak ada produk komersial dengan spesifikasi identik di pasar Indonesia.
2. **Fungsional & Siap Uji:** Bisa menghasilkan prototipe yang dapat didemonstrasikan langsung di depan juri PIMNAS dalam 3–4 bulan.
3. **Anggaran Realistis:** Komponen inti prototipe < Rp 5 juta (menyisakan ruang untuk bahan habis pakai, uji, dan tak terduga).
4. **Kompetensi Tim Tercakup:** Setiap anggota tim punya peran hardware/firmware/software yang jelas berdasarkan kemampuan aktual di `USER.md`.
5. **Masalah Riil Terukur:** Ada data empiris (dari BPS, BNPB, Kemenkes, PLN, dll.) yang membuktikan skala masalah, bukan hanya narasi.
6. **Gap Literatur Terbuka:** Sepanjang penelusuran (query + tanggal), belum ada solusi identik yang diterbitkan di IEEE/Scopus 2022–2025.

## Proses Kerja (Urutan Wajib)

### Langkah 1 — Scan Isu Genting Nasional
Identifikasi masalah dengan data kuantitatif:
- Sumber: BPS, Kemenkes, BNPB, PLN, BRIN, laporan industri resmi
- Filter: Masalah yang berdampak luas (ribuan hingga jutaan orang/unit) **DAN** belum ada solusi murah yang tersedia

### Langkah 2 — Pemetaan Domain Teknis
Padankan masalah ke kemampuan tim:
```
Masalah → Sensor/aktuator apa? → Pemrosesan sinyal bagaimana? → AI/Edge computing di mana?
        → Komunikasi/transmisi data bagaimana? → Form factor hardware apa?
```

### Langkah 3 — Filter Saturasi & Kompetitor
Periksa:
- Produk komersial yang ada (Alibaba, Digi-Key, lokal)
- Paper PKM/PIMNAS terdahulu (database SIMBELMAWA publik)
- Paper IEEE/Scopus 2022–2025 yang persis sama
- Karya kampus seperti Telkom University, ITS, UGM, UI di topik ini

### Langkah 4 — Formulasi Mekanisme Kebaruan
Jawab secara spesifik: **"Apa yang belum pernah dilakukan dan mengapa secara teknis ini memungkinkan sekarang?"**
Format: `[TEKNOLOGI_A] + [TEKNOLOGI_B] → menyelesaikan [GAP_X] yang sebelumnya tidak bisa diselesaikan oleh [SOLUSI_LAMA]`

### Langkah 5 — Uji Kelayakan Cepat (30-Menit Feasibility Check)
| Dimensi | Pertanyaan | Status |
|---|---|---|
| Hardware | Komponen utama bisa dibeli di Tokopedia/Shopee/LCSC? Harga total < Rp 5 juta? | ✅/❌ |
| Firmware | Tim bisa menulis kode ini dalam 4–8 minggu? Ada library open-source yang bisa jadi dasar? | ✅/❌ |
| Dataset | Ada dataset publik (IEEE Dataport/Mendeley) untuk melatih model AI? Jika tidak, bisa dikumpulkan sendiri dalam 2 minggu? | ✅/❌ |
| Uji Lapangan | Ada lokasi/mitra uji yang bisa diakses dalam 4 bulan? (lab kampus, PLN ULP, Dinkes, Dintan, dll.) | ✅/❌ |
| Visualitas | Prototipe terlihat menarik secara fisik di panggung PIMNAS? Bisa dipegang/dioperasikan langsung? | ✅/❌ |

### Langkah 6 — Implementation Plan (4 Fase)
Rancang per fase dengan PIC dan deadline realistis:

```
FASE 0 — Studi & Dataset (Minggu 1–2)
├── Penelusuran literatur SOTA (keyword + database + tanggal)
├── Wawancara/observasi pengguna/mitra uji
└── Pengumpulan/akuisisi dataset awal

FASE 1 — Desain Sistem (Minggu 3–5)
├── Skematik hardware & Bill of Materials
├── Arsitektur firmware & pipeline AI
└── Simulasi/modeling awal

FASE 2 — Fabrikasi & Pemrograman (Minggu 6–10)
├── Fabrikasi PCB & perakitan komponen
├── Pelatihan model AI + integrasi firmware
└── Prototipe v1 (mungkin masih ada bug — normal)

FASE 3 — Pengujian & Validasi (Minggu 11–14)
├── Uji laboratorium (kondisi terkontrol)
├── Uji lapangan (kondisi nyata, ada mitra/izin)
├── Pengumpulan data metrik (akurasi/sensitivitas/latensi/dll.)
└── Penyempurnaan berdasarkan hasil uji

FASE 4 — Dokumentasi & Pelaporan (Minggu 15–16)
├── Laporan kemajuan & laporan akhir
└── Draf paten / draf artikel ilmiah
```

### Langkah 7 — Output ke Workspace
- Peta Gagasan → diskusi di chat / artifact
- Mekanisme kebaruan → `30-riset/CLAIM-MATRIX.md` (klaim C-xxx)
- Literatur awal → `20-literatur/EVIDENCE-LEDGER.md` (ID E-xxx, hanya jika sudah diverifikasi)
- Kesepakatan ide final → `00-project/PROJECT.md`

## Output Format
```
## [NAMA IDE]
- Masalah: [1 kalimat + data empiris + sumber]
- Gap: [apa yang belum bisa dilakukan solusi yang ada]
- Mekanisme Kebaruan: [TEKNOLOGI_A + TEKNOLOGI_B → solusi GAP]
- Komponen Utama: [daftar + estimasi harga]
- Metrik Keberhasilan: [angka spesifik + ambang kelulusan]
- Risiko Utama: [1–2 risiko + mitigasi]
- Feasibility Score: [X/5 ✅ per dimensi]
```

