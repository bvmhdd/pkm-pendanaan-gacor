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