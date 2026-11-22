---
name: literature-review
description: Gunakan saat mencari, menyaring, dan mensintesis literatur untuk membuktikan gap dan kebaruan. Output masuk ke EVIDENCE-LEDGER. Wajib dijalankan setelah ide dikunci di PROJECT.md dan sebelum penulisan Bab 2.
---

# Literature Review

## Kapan Dipakai
- Menyusun Bab 2 Tinjauan Pustaka & membuktikan kebaruan di Bab 1
- Memvalidasi gap yang diklaim sebelum klaim masuk `CLAIM-MATRIX.md`
- Mengisi `EVIDENCE-LEDGER.md` dengan bukti terverifikasi

## Sumber Pencarian (Prioritas)
1. IEEE Xplore (`ieeexplore.ieee.org`)
2. Scopus / Web of Science (via VPN kampus)
3. ScienceDirect / MDPI / Wiley
4. ACM Digital Library (untuk CS/software)
5. Google Scholar (hanya untuk temuan awal, selalu verifikasi ke sumber asli)
6. Preprint: arXiv, TechRxiv (tandai `[PREPRINT]`)
7. Lokal: SINTA Garuda, Semantic Scholar

## Proses Wajib

### 1. Rumuskan Pertanyaan Pencarian
Format: `[MASALAH] + [DOMAIN TEKNOLOGI] + [METRIK/HASIL YANG DICARI]`
Contoh: `Partial Discharge detection + UHF sensor + accuracy classification TinyML 2022-2025`

Catat selalu:
- Query string yang dipakai
- Database yang dicari
- Tanggal pencarian
- Jumlah hasil sebelum dan sesudah filter

### 2. Kriteria Inklusi/Eksklusi
| Kriteria | Inklusi | Eksklusi |
|---|---|---|
| Tahun | 2020–2025 (utamakan 2023–2025) | Sebelum 2020 (kecuali paper foundational) |
| Bahasa | Inggris, Indonesia | Lainnya |
| Jenis | Peer-reviewed journal, conference IEEE/Scopus | Blog, Wikipedia, laporan tidak resmi |
| Relevansi | Langsung mendukung klaim | Topik sama tapi metrik berbeda (catat sebagai konteks) |

### 3. Saring Bertahap (PRISMA-lite)
```
Hasil pencarian → Filter judul → Filter abstrak → Baca teks penuh → Ekstraksi data
   (catat N)       (catat N)      (catat N)         (catat N)         (masuk ledger)
```

### 4. Ekstraksi per Paper
Untuk setiap paper yang lolos teks penuh, catat:
- Tujuan & pertanyaan penelitian
- Metode / teknologi yang digunakan
- Metrik evaluasi & **angka hasil spesifik** (bukan "cukup baik")
- Keterbatasan yang diakui penulis
- Gap yang terbuka (peluang karya kita)

### 5. Sintesis per Tema (Bukan per Paper)
Kelompokkan berdasarkan tema, bukan kronologi:
```
Tema A: Metode X → konsensus apa, angka terbaik berapa, keterbatasan apa
Tema B: Metode Y → idem
Gap: Belum ada yang menggabungkan X+Y untuk mengatasi Z
```

### 6. Peta Kebaruan (Tabel Wajib di Bab 2)
| Aspek | Karya A | Karya B | Karya C | KARYA KITA |
|---|---|---|---|---|
| Metode | | | | ✅ Baru |
| Dataset/kondisi uji | | | | ✅ Baru |
| Metrik unggulan | | | | ✅ Target X% |

### 7. Masukkan ke EVIDENCE-LEDGER
Hanya paper yang sudah dibaca teks penuh, dengan format:
```
| E-xxx | Penulis, Tahun. Judul. Venue, DOI | Empiris/SR/Standar | Temuan spesifik + angka | Halaman | Keterbatasan | Tgl verifikasi |
```

## Larangan
- Merangkum paper dari abstrak saja lalu klaim "sudah membaca"
- Menyebut "belum ada penelitian" tanpa log pencarian yang mendukung — gunakan: *"Sepanjang penelusuran kami ([query], [database], [tanggal]), belum ditemukan..."*
- Memasukkan sitasi yang dihasilkan AI ke EVIDENCE-LEDGER tanpa verifikasi manual ke sumber asli
- Menggunakan paper dari jurnal predator (cek DOAJ, Beall's List, indeksasi Scopus)

## Output
- Log pencarian (query + database + tanggal + jumlah hasil)
- Tabel ekstraksi
- Peta kebaruan
- Paragraf sintesis bersitasi (ID ledger)
- Daftar gap yang terbuka → masuk `CLAIM-MATRIX.md`
