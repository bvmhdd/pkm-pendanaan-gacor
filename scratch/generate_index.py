import os
import glob
import re

folder = r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026"
output_file = os.path.join(folder, "INDEX-ANALISIS-PKP2.md")

rooms_info = {
    "pkp pkm room1.md": {"room": "Room 1", "skema": "PKM-KC (Karsa Cipta)", "penilai": "Bapak Guntur Eka Saputra & Bapak Muhammad Izzuddin Mahali"},
    "pkp pkm room2.md": {"room": "Room 2", "skema": "PKM-KC & PKM-PI (Teknologi & IoT)", "penilai": "Tim Penilai PKP2 Room 2"},
    "pkp pkm room3.md": {"room": "Room 3", "skema": "PKM-K (Kewirausahaan Produk Alami)", "penilai": "Tim Penilai PKP2 Room 3"},
    "pkp pkm room 4.md": {"room": "Room 4", "skema": "PKM-K & PKM-RE (Kewirausahaan & Farmasi)", "penilai": "Tim Penilai PKP2 Room 4"},
    "pkp pkm room5.md": {"room": "Room 5", "skema": "PKM-PM (Pengabdian Masyarakat)", "penilai": "Tim Penilai PKP2 Room 5"},
}

with open(output_file, "w", encoding="utf-8") as out:
    out.write("# Repository & Analisis Transkrip Penilaian Kemajuan (PKP2) PKM 2026\n\n")
    out.write("> Dokumen ini dibuat otomatis sebagai basis pengetahuan (knowledge base) dan indeks komparatif untuk tim, merangkum pola tanya-jawab, kritik reviewer nasional, serta ide-ide yang lolos pendanaan di PKP2.\n\n")
    out.write("---\n\n")
    
    for f in sorted(glob.glob(os.path.join(folder, "pkp pkm room*.md"))):
        name = os.path.basename(f)
        info = rooms_info.get(name, {"room": name, "skema": "Umum", "penilai": "Reviewer Belmawa"})
        
        with open(f, "r", encoding="utf-8", errors="ignore") as fp:
            text = fp.read()
            
        out.write(f"## {info['room']} — {info['skema']}\n")
        out.write(f"- **File Sumber:** `{name}` (Ukuran: {len(text)/1024:.1f} KB, ~{len(text):,} karakter)\n")
        out.write(f"- **Reviewer / Penilai:** {info['penilai']}\n\n")
        
        # Extract universities
        unis = sorted(list(set(re.findall(r'(?:Universitas|Politeknik|Institut)\s+[A-Z][a-zA-Z\s]{3,25}', text))))
        out.write(f"### Perguruan Tinggi yang Tampil ({len(unis)} Kampus):\n")
        out.write(", ".join(unis[:12]) + ("..." if len(unis) > 12 else "") + "\n\n")
        
        # Sample projects
        out.write("### Rekap Tim & Karya Inovasi Terdeteksi:\n")
        # Find distinct project titles
        matches = re.finditer(r'(?:judul|berjudul|inovasi yang kami kembangkan|rancang bangun|pengembangan|alat kami)\s*[:\s\"\'“]*([^.\n\r\t]{15,120})', text, re.IGNORECASE)
        seen = set()
        count = 0
        for m in matches:
            clean = re.sub(r'\s+', ' ', m.group(1)).strip()
            if clean[:35] not in seen and len(clean) > 20:
                seen.add(clean[:35])
                count += 1
                out.write(f"{count}. **{clean}**\n")
                if count >= 6:
                    break
        out.write("\n---\n\n")

print("Generated INDEX-ANALISIS-PKP2.md successfully.")
