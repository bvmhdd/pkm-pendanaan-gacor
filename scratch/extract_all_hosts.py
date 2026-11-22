import glob
import os
import re

folder = r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026"

for f in sorted(glob.glob(os.path.join(folder, "*.md"))):
    name = os.path.basename(f)
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        head = fp.read(4000)
    
    # search for penilai or reviewer names in the beginning
    revs = re.findall(r'(?:penilai|reviewer|bapak|ibu)\s+([A-Z][a-zA-Z\s]{4,30})', head, re.IGNORECASE)
    print(f"=== {name} ===")
    print("Beginning snippet:")
    lines = [line.strip() for line in head.split("\n") if line.strip()][:3]
    for l in lines:
        print(" ", l[:120])
    print()
