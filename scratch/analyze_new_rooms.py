import os
import glob
import re

folder = r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026"
new_files = ["pkp pkm room6.md", "pkp pkm room7.md", "pkp pkm room8.md", "pkp pkm room9.md", "pkp pkm room10.md"]

def analyze_room(filename):
    filepath = os.path.join(folder, filename)
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    
    print(f"\n{'='*60}")
    print(f"ANALISIS: {filename} ({len(text)/1024:.1f} KB, {len(text):,} karakter)")
    print(f"{'='*60}")
    
    # 1. Identify Reviewers
    head = text[:5000]
    reviewers = re.findall(r'(?:penilai|reviewer|bapak|ibu)\s+([A-Z][a-zA-Z\s]{4,30})', head, re.IGNORECASE)
    print(f"Penilai/Host Awal Terdeteksi: {list(set([r.strip() for r in reviewers[:6]]))}")
    
    # 2. Identify Schemes
    schemes = set(re.findall(r'PKM-[A-Z]{1,4}', text, re.IGNORECASE))
    print(f"Skema yang Disebut: {schemes}")
    
    # 3. Identify Universities
    unis = set(re.findall(r'(?:Universitas|Politeknik|Institut)\s+[A-Z][a-zA-Z\s]{3,25}', text))
    print(f"Kampus Terdeteksi ({len(unis)}): {list(unis)[:6]}")
    
    # 4. Identify Teams & Titles
    # Look for 'judul', 'berjudul', 'alat kami', 'karya cipta', 'inovasi kami'
    titles = re.findall(r'(?:judul|berjudul|inovasi yang kami kembangkan|rancang bangun|alat kami|produk kami)\s*[:\s\"\'“]*([^.\n\r\t]{15,120})', text, re.IGNORECASE)
    print(f"\nSampel Inovasi / Judul Terdeteksi ({len(titles)}):")
    seen = set()
    count = 0
    for t in titles:
        t_clean = re.sub(r'\s+', ' ', t).strip()
        if t_clean[:35] not in seen and len(t_clean) > 20:
            seen.add(t_clean[:35])
            count += 1
            print(f"  {count}. {t_clean}")
            if count >= 8:
                break

if __name__ == "__main__":
    for nf in new_files:
        analyze_room(nf)
