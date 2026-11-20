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
