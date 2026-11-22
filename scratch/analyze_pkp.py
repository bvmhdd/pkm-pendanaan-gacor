import os
import glob
import re

folder = r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026"
files = sorted(glob.glob(os.path.join(folder, "*.md")))

def analyze_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    print(f"\n=======================================================")
    print(f"FILE: {filename} (Ukuran: {len(content)/1024:.1f} KB)")
    print(f"=======================================================")
    
    # Identify teams and presentations
    # Look for 'kelompok 1', 'kelompok 2', etc.
    # Look for universities: Universitas, Politeknik, Institut
    unis = set(re.findall(r'(?:Universitas|Politeknik|Institut)\s+[A-Z][a-zA-Z\s]{3,30}', content))
    print(f"Perguruan Tinggi Terdeteksi ({len(unis)}):")
    for u in list(unis)[:8]:
        print(f"  - {u.strip()}")
        
    # Search for titles or keywords
    titles = re.findall(r'(?:judul|berjudul|inovasi yang kami kembangkan|rancang bangun|pengembangan|alat kami)\s*[:\s\"\'“]*([^.\n\r\t]{15,100})', content, re.IGNORECASE)
    print(f"\nSampel Judul / Inovasi Terdeteksi:")
    seen = set()
    for t in titles:
        t_clean = re.sub(r'\s+', ' ', t).strip()
        if t_clean[:30] not in seen:
            seen.add(t_clean[:30])
            print(f"  * {t_clean}")
            if len(seen) >= 8:
                break

if __name__ == "__main__":
    for f in files:
        analyze_file(f)
