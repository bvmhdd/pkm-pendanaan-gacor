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