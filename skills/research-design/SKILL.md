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