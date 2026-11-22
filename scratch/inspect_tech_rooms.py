import os
import re

folder = r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026"

def inspect_engineering_in_rooms(filename):
    filepath = os.path.join(folder, filename)
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    
    print(f"\n==========================================")
    print(f"ANALISIS TEKNOLOGI DI {filename}")
    print(f"==========================================")
    
    # search for IoT, sensor, mikrokontroler, mesin, prototype
    tech_matches = re.finditer(r'(?:iot|sensor|mikrokontroler|arduino|esp32|mesin|otomatis|alat|prototipe|sistem)[^.\n]{20,120}[.?!]', text, re.IGNORECASE)
    seen = set()
    count = 0
    for m in tech_matches:
        s = re.sub(r'\s+', ' ', m.group(0)).strip()
        if s[:30] not in seen:
            seen.add(s[:30])
            count += 1
            print(f"  [{count}] {s}")
            if count >= 8:
                break

if __name__ == "__main__":
    inspect_engineering_in_rooms("pkp pkm room7.md")
    inspect_engineering_in_rooms("pkp pkm room10.md")
