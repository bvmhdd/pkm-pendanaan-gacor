import os
import glob
import re

folder = r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026"
index_file = os.path.join(folder, "INDEX-ANALISIS-PKP2.md")

rooms_info = {
    "pkp pkm room6.md": {"room": "Room 6", "skema": "PKM-RSH (Riset Sosial Humaniora)", "fokus": "Linguistik Konflik, Etnosemantik Gangguan Jiwa, Gamifikasi AR Dayak, Masterplan Agraria"},
    "pkp pkm room7.md": {"room": "Room 7", "skema": "PKM-PM (Pengabdian Masyarakat)", "fokus": "Edukasi Siswa SLB Tunarungu, Terapi Musik Rindik Ibu Hamil, Vertical Farming PKK, Pengolahan Sampah"},
    "pkp pkm room8.md": {"room": "Room 8", "skema": "PKM-K (Kewirausahaan Produk Kreatif)", "fokus": "Kapsul Organik Pengusir Hama Burung, Skincare Balm Tengkawang, Dekorasi Limbah Popok, Pet Care"},
    "pkp pkm room9.md": {"room": "Room 9", "skema": "PKM-RSH (Riset Sosial Humaniora)", "fokus": "Linguistik Forensik Child Grooming Medsos, Akuntansi Lingkungan Tri Hita Karana, Etnomedisin Dayak"},
    "pkp pkm room10.md": {"room": "Room 10", "skema": "PKM-PI & PKM-KI (Penerapan Iptek & Karya Inovatif)", "fokus": "Mesin Briket Hidrolik, Mesin Pengering Minyak Nilam, Aplikasi Android Akuntansi & Pajak UMKM"},
}

with open(index_file, "a", encoding="utf-8") as out:
    out.write("\n---\n\n# Analisis Pembaruan: Room 6 s.d. Room 10\n\n")
    
    for fname in ["pkp pkm room6.md", "pkp pkm room7.md", "pkp pkm room8.md", "pkp pkm room9.md", "pkp pkm room10.md"]:
        fpath = os.path.join(folder, fname)
        if not os.path.exists(fpath):
            continue
        info = rooms_info[fname]
        with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
            text = fp.read()
            
        out.write(f"## {info['room']} — {info['skema']}\n")
        out.write(f"- **File Sumber:** `{fname}` (Ukuran: {len(text)/1024:.1f} KB, ~{len(text):,} karakter)\n")
        out.write(f"- **Fokus Bidang:** {info['fokus']}\n\n")
        
        # Extract universities
        unis = sorted(list(set(re.findall(r'(?:Universitas|Politeknik|Institut)\s+[A-Z][a-zA-Z\s]{3,25}', text))))
        out.write(f"### Perguruan Tinggi Terdeteksi ({len(unis)} Kampus):\n")
        out.write(", ".join(unis[:10]) + ("..." if len(unis) > 10 else "") + "\n\n")
        
        # Sample projects
        out.write("### Rekap Tim & Judul Utama:\n")
        titles = re.findall(r'(?:judul|berjudul|inovasi yang kami kembangkan|rancang bangun|alat kami|produk kami)\s*[:\s\"\'“]*([^.\n\r\t]{15,120})', text, re.IGNORECASE)
        seen = set()
        count = 0
        for t in titles:
            clean = re.sub(r'\s+', ' ', t).strip()
            if clean[:35] not in seen and len(clean) > 20:
                seen.add(clean[:35])
                count += 1
                out.write(f"{count}. **{clean}**\n")
                if count >= 5:
                    break
        out.write("\n")

    out.write("\n### Pelajaran Baru dari Room 6–10 untuk PKM-KC:\n")
    out.write("1. **Otentisitas Pembuatan Prototipe (Room 10 - PKM-PI/KI):** Reviewer mengejar secara mendalam: *'Alat ini dibuat di mana? Siapa yang merancang dan siapa yang merakit?'* Jangan sampai ada kesan tim hanya memesan alat jadi ke bengkel luar tanpa keterlibatan desain teknik langsung.\n")
    out.write("2. **Validasi Masalah Hama & Pasca-Panen (Room 8 & 10):** Isu serangan hama dan pengolahan hasil panen (briket, minyak nilam, repellent hama) muncul berulang kali di berbagai skema, membuktikan bahwa tema **Kemandirian Pangan & Pertanian** adalah salah satu topik favorit juri Belmawa.\n")
    out.write("3. **Pemisahan Karakteristik Antar-Skema:** Room 6 dan 9 memperlihatkan riset sosial murni (tanpa prototipe fisik). Untuk PKM-KC, kekuatan tim kita tetap berada pada **Karsa Cipta Hardware + Embedded AI** seperti di Room 1.\n")

print("Updated INDEX-ANALISIS-PKP2.md with Room 6-10.")
