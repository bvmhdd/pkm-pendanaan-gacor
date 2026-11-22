---
name: proposal-writing
description: Gunakan untuk menulis atau merevisi bagian proposal PKM-KC agar padat, runtut, bersitasi terverifikasi, dan sesuai pedoman Belmawa 2026. Hanya dijalankan setelah ide dikunci di PROJECT.md dan CLAIM-MATRIX.md terisi.
---

# Proposal Writing

## Prasyarat Sebelum Menulis
- [ ] `00-project/PROJECT.md` sudah diisi lengkap (judul, masalah, tujuan, metode, luaran)
- [ ] `30-riset/CLAIM-MATRIX.md` memiliki setidaknya klaim C001–C004 berstatus `Terverifikasi`
- [ ] `20-literatur/EVIDENCE-LEDGER.md` memiliki ≥ 5 entri terverifikasi
- [ ] `10-pedoman/CHECKLIST-PEDOMAN.md` sudah dibaca dan dipahami
- Jangan menulis Bab 2 sebelum `literature-review` skill selesai dijalankan

## Prinsip Penulisan PKM-KC

### Piramida Terbalik
> Kesimpulan/poin utama dulu → rincian kemudian
> Juri membaca proposal dalam waktu singkat — kalimat pertama setiap paragraf harus sudah menyampaikan isi.

### Kuantifikasi Wajib
- Gunakan angka dan satuan konkret: ✅ `"PDR ≥ 90% pada 3 hop relay"` bukan ❌ `"performa sangat baik"`
- Target hasil ditulis sebagai **target terukur** (proposal), bukan seolah sudah tercapai
- Setiap angka punya ID evidence di EVIDENCE-LEDGER atau ID eksperimen di EXPERIMENT-LOG

### Konsistensi Istilah
- Definisikan singkatan di kemunculan pertama: `"Partial Discharge (PD)"`
- Gunakan istilah yang sama konsisten sepanjang dokumen — jangan berganti-ganti sinonim

### Larangan Keras dalam Naskah
- ❌ Frasa klise: "di era industri 4.0", "Indonesia yang kaya akan...", "sangat diharapkan dapat"
- ❌ Klaim tanpa bukti: semua klaim faktual harus ada ID ledger-nya
- ❌ Kutipan sekunder: "X mengutip Y" — kutip Y langsung
- ❌ Kata sifat subjektif tanpa angka: "signifikan", "sangat akurat", "cukup efisien"

## Alur Kerja per Bagian

### Bab 1 — Pendahuluan
1. **Latar Belakang (maks. 1 halaman):** Masalah (data empiris) → Gap solusi yang ada → Alasan solusi baru diperlukan (mekanisme kebaruan) → Urgensi
2. **Rumusan Masalah:** 2–3 pertanyaan spesifik, dapat dijawab oleh prototipe
3. **Tujuan:** Jawaban langsung dari rumusan masalah, bukan ulang rumusan
4. **Luaran:** Prototipe + laporan + artikel/paten (sesuai pedoman)
5. **Kebaruan (Tabel Komparatif wajib):** Kolom = aspek teknis; Baris = karya A, B, C, dan KARYA KITA

### Bab 2 — Tinjauan Pustaka
- Sintesis per tema, bukan per paper (output dari `literature-review` skill)
- Tutup dengan: *"Berdasarkan kajian di atas, [GAP] belum diatasi, yang menjadi dasar pengembangan [NAMA ALAT] dalam penelitian ini."*

### Bab 3 — Tahap Pelaksanaan
- Flowchart alur pelaksanaan (gambar wajib)
- Spesifikasi teknis komponen utama (tabel)
- Rancangan pengujian: variabel, metrik, baseline, kondisi uji
- Kriteria keberhasilan (acceptance criteria) berbentuk angka

### Bab 4 — Biaya & Jadwal
- Gunakan `budget-rab` skill untuk RAB
- Bar chart kegiatan (Gantt-lite) per 2 minggu selama 3–4 bulan
- Kolom personalia: nama + peran per fase

## Alur Revisi
`Draft kasar` → `argumentation-cer` (perkuat paragraf) → `Pangkas kata (maks. 10 halaman inti)` → `citation-verification` → `CHECKLIST-PEDOMAN.md` → `reviewer-simulation`

## Abstrak / Ringkasan (Tulis Terakhir)
Urutan wajib: **Masalah (data) → Gap → Solusi/Metode → Target terukur → Dampak**
Panjang: 1 paragraf, maks. 250 kata
