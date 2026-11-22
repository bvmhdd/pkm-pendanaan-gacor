---
name: argumentation-cer
description: Gunakan untuk menyusun atau menguji argumen ilmiah dalam naskah PKM dengan struktur Claim–Evidence–Reasoning (CER) plus bantahan, agar setiap paragraf kuat, spesifik, dan tahan uji juri PIMNAS.
---

# Argumentation (CER + Rebuttal)

## Kapan Dipakai
- Setelah draft kasar ditulis, sebelum finalisasi
- Saat menguji kekuatan klaim di `CLAIM-MATRIX.md`
- Saat mempersiapkan jawaban untuk pertanyaan juri

## Struktur Satu Paragraf Argumen
```
[1] CLAIM    — Satu kalimat spesifik, dapat diuji, dapat difalsifikasi.
                Hindari: "penelitian ini bertujuan untuk..." atau klaim kabur.
                Target: pembaca tahu apa yang dibuktikan tanpa membaca selanjutnya.

[2] EVIDENCE — Data/sitasi spesifik dengan angka dan satuan + ID ledger.
                Format: (Penulis, Tahun: angka spesifik, kondisi uji)
                Hindari: "menurut beberapa penelitian..." tanpa sitasi konkret.

[3] REASONING — Mengapa bukti itu mendukung klaim secara mekanis/logis?
                Bukan pengulangan bukti — ini penjelasan mekanisme kausalnya.
                Contoh: "Hal ini terjadi karena [mekanisme X], sehingga [efek Y]..."

[4] QUALIFIER — Batas berlakunya klaim (populasi, kondisi, skala, asumsi).
                Contoh: "dalam kondisi LOS dengan jarak < 100 meter..."

[5] REBUTTAL  — Keberatan terkuat yang bisa diajukan + tanggapan berbasis bukti.
                Jika tidak bisa dibantah → akui sebagai keterbatasan secara eksplisit.
```

## Contoh Penerapan

**Versi Lemah (❌ hindari):**
> "Jaringan komunikasi sering mengalami gangguan saat bencana sehingga sistem kami diperlukan."

**Versi Kuat (✅ target):**
> `[CLAIM]` Jaringan telekomunikasi seluler di Indonesia mengalami kegagalan operasional total pada fase akut bencana gempa bumi, mengakibatkan isolasi komunikasi tim SAR. `[EVIDENCE]` BNPB melaporkan bahwa pada gempa Cianjur 2022, lebih dari 60% BTS di zona terdampak tidak beroperasi dalam 6 jam pertama pascagempa (BNPB, 2022). `[REASONING]` Kegagalan ini terjadi karena BTS bergantung pada daya listrik jaringan PLN dan backhaul fiber optik yang terputus akibat pergerakan tanah — dua infrastruktur yang paling rentan terhadap guncangan seismik. `[QUALIFIER]` Kondisi ini berlaku pada zona episentrum dengan intensitas ≥ MMI VI. `[REBUTTAL]` Meski radio HT analog masih dapat beroperasi, kapasitasnya terbatas pada 1 kanal suara per frekuensi dan tidak mendukung transmisi data koordinat GPS secara digital.

## Uji Kualitas Mandiri (Jalankan Sebelum Finalisasi)
- [ ] Apakah klaim bisa salah? Jika tidak → terlalu kabur, perbaiki
- [ ] Apakah angka di Evidence persis dari sumber (cek EVIDENCE-LEDGER)?
- [ ] Apakah Reasoning menjelaskan mekanisme, bukan sekadar ulang Evidence?
- [ ] Apakah kata-kata sesuai kekuatan bukti?
  - `[FAKTA]` → "membuktikan", "menunjukkan"
  - `[INFERENSI]` → "mengindikasikan", "konsisten dengan"
  - `[ASUMSI]` → "diasumsikan", "diperkirakan"
- [ ] Apakah ada penjelasan alternatif yang belum dibahas?

## Pola Kesalahan Logika yang Harus Diwaspadai
| Pola | Contoh di PKM | Perbaikan |
|---|---|---|
| Korelasi = kausalitas | "Karena negara A maju, teknologi X berhasil" | Tunjukkan mekanisme penyebab langsung |
| Generalisasi tergesa | "Semua petani membutuhkan alat ini" | Batasi populasi target yang spesifik |
| Argumen otoritas | "Menurut pakar, sistem ini terbaik" | Ganti dengan data empiris dari paper |
| False dilemma | "Hanya ada dua solusi: X atau Y" | Akui ada alternatif lain, jelaskan mengapa X dipilih |
| Survivorship bias | "Semua yang lolos PIMNAS menggunakan PCB custom" | Cek juga yang tidak lolos dengan PCB custom |
| Circular reasoning | "Alat ini bagus karena performanya baik" | Definisikan "baik" dengan angka terukur |

## Output
- Paragraf siap-naskah (berisi label `[CLAIM]`, `[EVIDENCE]`, `[REASONING]` yang bisa dihapus setelah selesai)
- Baris baru di `CLAIM-MATRIX.md` jika klaim belum terdaftar
