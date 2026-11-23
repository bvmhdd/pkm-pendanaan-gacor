# Indeks Berkas Referensi Ilmiah (20-literatur/references)

> **Catatan Status:** Kumpulan berkas artikel ilmiah rujukan untuk eksplorasi teknologi dan pembuktian *state-of-the-art*. Dokumen ini **bukan keputusan akhir ide**, melainkan bahan kajian literatur terbuka untuk tim.

---

## Daftar 8 Paper Rujukan yang Tersedia

| No | Nama Berkas | Judul Artikel Ilmiah | Penerbit / Indeks | Fokus & Relevansi IPTEK |
|---|---|---|---|---|
| 1 | `1-s2.0-S2352711026000646-main.pdf` | **LoRaMesher: An open-source library for multi-hop LoRa mesh networks** | SoftwareX (Elsevier) | Library open-source routing multi-hop untuk jaringan mesh LoRa mandiri. |
| 2 | `A-Novel-Approach-to-Energy-Efficiency-Optimization-in-Hybrid-ESP-NOW-LoRa-Networks-Using.pdf` | **A Novel Approach to Energy Efficiency Optimization in Hybrid ESP-NOW/LoRa Networks Using Low-Power Strategies** | INATEL / IEEE Conference | Strategi optimasi efisiensi daya pada jaringan hibrida ESP-NOW dan LoRa. |
| 3 | `Field_Validated_Hybrid_ESP-NOW_and_Long_Range_IoT_Monitoring_System_for_Energy_Autonomous_Precision_Agriculture.pdf` | **Field Validated Hybrid ESP-NOW and Long Range IoT Monitoring System for Energy Autonomous Precision Agriculture** | IEEE Access (2025) | Implementasi lapangan sistem IoT hibrida ESP-NOW + LoRa otonom energi bertenaga surya. |
| 4 | `IEEE Xplore Full-Text PDF_.pdf` | **QoS Based IoT Applications in LoRa Networks Using Multi-Dimensional Allocation Strategy** | IEEE Access (2024) | Strategi alokasi multi-dimensi untuk jaminan Quality of Service (QoS) pada jaringan LoRa. |
| 5 | `LoRa-ESP32-Disaster-Response-Resilient-Wireless-Communication-System.pdf` | **LoRa-ESP32: Disaster Response Resilient Wireless Communication System** | IEEE Conference | Rancang bangun sistem komunikasi nirkabel tanggap bencana berbasis LoRa dan ESP32. |
| 6 | `sensors-26-04381.pdf` | **TDMA-Based LoRa IoT Architecture with FreeRTOS** | MDPI Sensors | Arsitektur TDMA berbasis FreeRTOS pada ESP32/LoRa untuk mencegah tabrakan paket (*collision*). |
| 7 | `sensors-26-04718-v2.pdf` | **LoRa Ad Hoc Networks for Heterogeneous Traffic** | MDPI Sensors | Penanganan lalu lintas data heterogen pada jaringan ad-hoc LoRa multi-hop. |
| 8 | `engproc-124-00067-v2.pdf` | **Off-Grid Solar Systems for Remote Sensor Networks** | MDPI Engineering Proceedings | Desain sistem catu daya surya mandiri (*energy harvesting*) untuk node sensor terisolir. |
| 9 | `Tonelli_et_al_2025_AS7341.pdf` | **A Portable and Low-Cost Single Board Computer-Based Spectrophotometric Platform for Optical Analysis in the UV and Visible Range** | *Adv. Sensor Res.* (Wiley, 2025), DOI: 10.1002/adsr.202400163 | Bukti kinerja spektrofotometer portabel AS7341 ($R^2 = 0.9998$, Passing-Bablok setara Agilent Cary 60 benchtop, $A = \log_{10} \frac{I_0-I_d}{I_s-I_d}$, housing 3D PLA). |
| 10 | `Tomar_et_al_2026_IEEE_Sensors.pdf` | **Portable Multispectral Optical Reader for Paper-Based Phosphate Detection in Saliva** | *IEEE Sensors J.* (2026), DOI: 10.1109/JSEN.2026.3734592 | Desain perangkat portabel AS7341 + ESP32, rasio rasiometrik $F4/F3$ (515/480 nm) eliminasi fluktuasi intensitas LED dan kekeruhan biologis ($R^2 \approx 0.98$, LOD 11.86 mg/L). |
| 11 | `Machado_et_al_2024_Anal_Methods.pdf` | **Evaluation of the performance of 3D printed (spectro)photometers based on multi-channel color sensors for colorimetric determinations** | *Anal. Methods* (RSC, 2024), DOI: 10.1039/d4ay01831a | Optimasi parameter AS7341 (gain 16x, LED 80 mA; per-kanal Ch1-Ch4) dan pemisahan spektral bertumpuk tartrazine (430 nm) vs sunset yellow (480 nm) recovery 99–102%. |
| 12 | `Amazon_et_al_1981_AJCP.pdf` | **Separation of Bilirubin from Hemoglobin by Recording Derivative Spectrophotometry** | *Am. J. Clin. Pathol.* (1981), DOI: 10.1093/ajcp/75.4.519 | Landasan fisika optik: serapan Soret band hemoglobin 415 nm & derivatif pertama $dA/d\lambda \approx 0$ pada 470–490 nm mengeliminasi interferensi hemoglobin pada estimasi pigmen urin. |
| 13 | `Chalmers_Snell_1993_ClinChem.pdf` | **Estimation of Plasma and Urinary Hemoglobin by a Rate Spectrophotometric Method** | *Clin. Chem.* (1993), DOI: 10.1093/clinchem/39.8.1679 | Kuantifikasi hemoglobin urin (LOD 3 mg/L, linier s.d. 200 mg/L) kebal interferensi askorbat dan bilirubin hingga 500 µmol/L; bukti urin sehat 0 mg/L Hb (marker trauma litogenik). |
| 14 | `Perrone_et_al_1996_PediatrNephrol.pdf` | **Urinary inhibitors of crystallization in hypercalciuric children with hematuria and nephrolithiasis** | *Pediatr. Nephrol.* (1996), DOI: 10.1007/s004670050133 | Bukti klinis: defisit inhibitor urin (GAGs turun >50%, sitrat turun drastis) memicu kristaluria patologis; hematuria tanpa batu terjadi saat inhibitor masih normal meski kalsium tinggi. |
| 15 | `Kavanagh_et_al_2000_ClinSci.pdf` | **Calcium oxalate crystallization kinetics studied by oxalate-induced turbidity in fresh human urine and artificial urine** | *Clin. Sci.* (2000), DOI: 10.1042/cs0980151 | Kinetika turbiditas kristalisasi CaOx (orde kedua, $n=2$), batas metastabel $ML = 1.35 \times [Ca]^{-0.81}$, rasio supersaturasi kritis ~10, pentingnya menjaga $[Ca] < 3\text{ mM}$. |
| 16 | `Kovacevic_et_al_2013_IntUrolNephrol.pdf` | **Urinary turbidity as a marker of crystallization: Is spectrophotometric assessment useful?** | *Int. Urol. Nephrol.* (2013), DOI: 10.1007/s11255-013-0466-3 | Pengukuran turbiditas CaOx pada suhu tubuh 37°C & pH 5.7 ($R^2 = 0.9757$ pada 660 nm), membedakan kinetika nukleasi vs puncak agregasi 18 menit, serta efek inhibisi sitrat. |
| 17 | `Kohri_et_al_1991_JUrol.pdf` | **Simple tests to determine urinary risk factors and calcium oxalate crystallization in the outpatient clinic** | *J. Urol.* (1991), DOI: 10.1016/s0022-5347(17)37725-7 | Landasan uji klinis rawat jalan berbasis kurva metastabilitas hiperbolik $[Ca] \times [Ox]$ dan pemantauan penurunan kecenderungan kristalisasi pasca intervensi diuresis. |
| 18 | `Laube_et_al_2016_Urolithiasis.pdf` | **Kinetics of calcium oxalate crystal formation in urine** | *Urolithiasis* (2016), DOI: 10.1007/s00240-016-0900-y | Studi 1.162 urin: fusi parameter termodinamika (Bonn Risk Index / BRI $> 1\text{ L}^{-1}$) dan kinetika (turbidity slope linear $r \ge 0.95$) untuk diferensiasi pasien batu vs sehat. |
| 19 | `Omar_MatJafri_2012_SensorReview.pdf` | **Development of optical instrument as turbidimeter: a comparative study** | *Sensor Review* (2012), DOI: 10.1108/02602281211209428 | Rancang bangun nefelometer 90° NIR ISO 7027 menggunakan LED 880 nm + fotodioda PIN BPW34 ($0.62\text{ A/W}$) + amplifier transimpedansi $10^7\text{ V/A}$ ($R^2 = 0.995$, error 1.809 NTU). |
| 20 | `Bankir_Daudon_2026_ClinKidneyJ.pdf` | **Poor compliance of recurrent stone formers to increase their fluid intake in spite of repeated recommendations** | *Clin. Kidney J.* (2026), DOI: 10.1093/ckj/sfag051 `[E040]` | Bukti kohort 181 pasien selama 6.8 tahun: 56%–84% gagal mematuhi minum air; nilai indeks $TIS_{fmu} > 2.45$ memicu kristaluria aktif $>50\%$. |
| 21 | `Porowski_et_al_2010_JUrol.pdf` | **A new approach to investigate the circadian rhythm of calcium oxalate crystallization risk in children with urolithiasis: morning spot urine versus 24-hour urine** | *J. Urol.* (2010), DOI: 10.1016/j.juro.2010.06.134 `[E041]` | Validasi klinis urin pagi spot (08.00–10.00) memiliki sensitivitas 0.788, spesifisitas 1.000, AUC 0.994 vs urin 24 jam (AUC 0.981). |
| 22 | `Baginska_Chyzy_et_al_2025_PediatrNephrol.pdf` | **The impact of urine pH on lithogenic risk profile in children with urolithiasis** | *Pediatr. Nephrol.* (2025), DOI: 10.1007/s00467-025-07044-1 `[E042]` | Target protektif pH 6.75–7.00 di mana sitrat & magnesium tertinggi dan kalsium terendah; korelasi negatif signifikan dengan risiko kristalisasi ($r = -0.287$). |
| 23 | `Silverio_et_al_2015_Urolithiasis.pdf` | **Point-of-care electrical conductivity measurement in spot morning urine for lithogenic risk and calcium oxalate sedimentation prediction** | *Urolithiasis* (2015), DOI: 10.1007/s00240-015-0812-2 `[E043]` | Kelayakan monitoring mandiri point-of-care di rumah: konduktivitas/impedansi urin pagi spot berkorelasi ($p = 0.01$) dengan AP(CaOx) EQ2 & sedimentasi kristal. |
| 24 | `Robert_et_al_1995_UrolInt.pdf` | **Evaluation of a simplified Tiselius crystallisation risk index for calcium oxalate stones** | *Urol. Int.* (1995), DOI: 10.1159/000282765 `[E044]` | Formula indeks Tiselius sederhana $Ca^{0.71} \cdot Ox \cdot V^{-1.2}$ berkorelasi kuat ($r \ge 0.97$) dengan formula lengkap, komputasi efisien di ESP32-S3. |
| 25 | `Robertson_2021_Urolithiasis.pdf` | **LITHOSCREEN: a comprehensive screening program and database for the metabolic evaluation of patients with calcium stone disease—the “stone clinic effect”** | *Urolithiasis* (2021), DOI: 10.1007/s00240-021-01284-8 `[E045]` | Database LITHOSCREEN (3.165 pasien), fenomena "Stone Clinic Effect", dan visualisasi dial risiko traffic-light (hijau-kuning-merah). |


---

## Referensi Empiris Penilaian Kemajuan (PKP2) Belmawa 2026

Transkrip resmi presentasi kemajuan PKM yang didanai Belmawa tersimpan di [`PKP PKM 2026/`](file:///d:/Belajar/Semester%205/Project/PKM/PKP%20PKM%202026/) dengan ringkasan lengkap di [`INDEX-ANALISIS-PKP2.md`](file:///d:/Belajar/Semester%205/Project/PKM/PKP%20PKM%202026/INDEX-ANALISIS-PKP2.md).

### Arketipe Ide Unggulan PKM-KC sebagai Benchmark Tim:
1. **Arketipe Tenaga Listrik & Proteksi Cerdas (Inspirasi Polines - Room 1):**
   - *Karya Asli:* Alat Perbaikan Kualitas Daya Listrik & Deteksi Harmonisa THD via FFT di ESP32.
   - *Peluang Elevasi Tim:* **Deteksi Emisi Partial Discharge (PD) Non-Kontak pada Trafo PLN berbasis Antena Micro-strip UHF & TinyML** (Mengeliminasi kelemahan relay mekanik & sensor komersial terbatas).
2. **Arketipe Akustik Presisi & Edge AI (Inspirasi UGM - Room 1):**
   - *Karya Asli:* Stetoskop Digital Cerdas & Breathing Mask untuk Deteksi Gangguan Paru di Faskes Primer via ESP32-S3 TinyML.
   - *Peluang Elevasi Tim:* **Bio-Acoustic Wood Stethoscope untuk Deteksi Dini Hama Penggerek Batang Kelapa Sawit (Kumbang Badak) berbasis TinyML** (Mengadopsi metodologi akustik & ESP32-S3 UGM, bebas izin etik medis).
3. **Arketipe Instrumen Uji Mutu Cepat (Inspirasi Room 2):**
   - *Karya Asli:* Monitoring pasif suhu/pH kolam ikan burayak.
   - *Peluang Elevasi Tim:* **Probe Handheld Bio-Impedansi Multi-Frekuensi untuk Skrining Cepat Kesegaran Ikan & Formalin Nelayan Rakyat** (Transformasi dari monitoring pasif menjadi instrumen uji aktif).
