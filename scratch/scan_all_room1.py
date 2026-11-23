import os
import glob
import re

folder = r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026"
room1_files = [
    "pkp pkm room1-1.md",
    "pkp pkm room1-2.md",
    "pkp pkm room1-3.md",
    "pkp pkm room1-4.md",
    "pkp pkm room1-5.md"
]

def scan_room1_part(filename):
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        return
        
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
        
    print(f"\n{'='*70}")
    print(f"FILE: {filename} ({len(text)/1024:.1f} KB, {len(text):,} karakter)")
    print(f"{'='*70}")
    
    # 1. Search for universities
    unis = set(re.findall(r'(?:Universitas|Politeknik|Institut)\s+[A-Z][a-zA-Z\s]{3,28}', text))
    print(f"Perguruan Tinggi ({len(unis)}): {list(unis)[:8]}")
    
    # 2. Search for team names, numbers, or titles
    # Often 'kelompok [nomor]' or 'judul' or 'perkenalkan kami'
    team_intros = re.finditer(r'(?:kelompok\s*(?:nomor\s*urut\s*)?(\d{1,2})|urutan\s*(?:ke-?\s*)?(\d{1,2})|judul\s*[:\s\"\'“]*([^.\n\r\t]{15,100})|berjudul\s*[:\s\"\'“]*([^.\n\r\t]{15,100})|inovasi yang kami kembangkan yaitu\s*([^.\n\r\t]{10,80}))', text, re.IGNORECASE)
    
    snippets = []
    for m in team_intros:
        snippets.append(m.group(0).strip())
        
    print(f"\nDeteksi Transisi Tim / Judul ({len(snippets)} temuan):")
    seen = set()
    for s in snippets[:15]:
        s_clean = re.sub(r'\s+', ' ', s)
        if s_clean[:30] not in seen:
            seen.add(s_clean[:30])
            print(f"  * {s_clean}")

if __name__ == "__main__":
    for rf in room1_files:
        scan_room1_part(rf)
