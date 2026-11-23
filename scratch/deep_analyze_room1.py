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

def analyze_room1_file(filename):
    filepath = os.path.join(folder, filename)
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
        
    print(f"\n{'='*70}")
    print(f"BEDAH DETAIL: {filename}")
    print(f"{'='*70}")
    
    # 1. Reviewer names
    reviewers = re.findall(r'(?:selamat pagi|selamat siang|selamat sore|penilai|reviewer|bapak|ibu)\s+([A-Z][a-zA-Z\s]{4,30}(?:M\.\w+|S\.\w+|Ph\.D|Dr\.|Prof\.)?)', text[:4000], re.IGNORECASE)
    print("Reviewer / Pembuka:", list(set([r.strip() for r in reviewers[:6]])))
    
    # 2. Scheme mentions
    schemes = set(re.findall(r'PKM-[A-Z]{1,4}', text, re.IGNORECASE))
    print("Skema PKM:", schemes)
    
    # 3. Find presentations (extract team name / title / campus)
    # Search for blocks where teams present
    # Usually: 'kelompok [N]', 'Universitas [X]', 'judul [Y]'
    pattern = r'(?:kami dari tim|judul(?:nya)?|berjudul|karsa cipta|inovasi)[^.\n]{15,140}'
    matches = re.findall(pattern, text, re.IGNORECASE)
    print(f"\nSampel Judul / Topik Terdeteksi ({len(matches)} temuan):")
    seen = set()
    count = 0
    for m in matches:
        clean = re.sub(r'\s+', ' ', m).strip()
        # filter out generic sentences
        if any(w in clean.lower() for w in ['rancang', 'pengembangan', 'analisis', 'rekayasa', 'alat', 'sistem', 'sintesis', 'smart', 'inovasi', 'penerapan', 'produksi', 'pemanfaatan']):
            if clean[:35] not in seen:
                seen.add(clean[:35])
                count += 1
                print(f"  {count}. {clean}")
                if count >= 10:
                    break

if __name__ == "__main__":
    for rf in room1_files:
        analyze_room1_file(rf)
