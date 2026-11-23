import os
import re

folder = r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026"

with open(os.path.join(folder, "pkp pkm room1-1.md"), "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's find teams in room1-1
teams = re.finditer(r'(kelompok\s*(?:nomor\s*urut\s*)?(\d{1,2})[^.\n]{10,150})', text, re.IGNORECASE)
print("=== TEAMS IN ROOM1-1 ===")
for t in teams:
    print("  *", t.group(0).strip()[:100])

# Find titles / innovations in room1-1
print("\n=== TITLES / INNOVATIONS IN ROOM1-1 ===")
matches = re.finditer(r'(?:judul|berjudul|inovasi|alat|produk|mengembangkan|rancang bangun)[^.?!]{15,140}[.?!]', text, re.IGNORECASE)
seen = set()
for m in matches:
    clean = re.sub(r'\s+', ' ', m.group(0)).strip()
    if any(w in clean.lower() for w in ['pkm', 'alat', 'mesin', 'sensor', 'iot', 'aplikasi', 'sistem', 'karya', 'bantu', 'terapi', 'komunikasi']):
        if clean[:35] not in seen:
            seen.add(clean[:35])
            print("  •", clean[:120])
