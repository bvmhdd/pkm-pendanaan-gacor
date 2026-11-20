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