import re

with open(r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026\pkp pkm room1.md", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's find sections around 'Pak Guntur' or 'Pak Izudin' or 'Pak Muhammad'
matches = list(re.finditer(r'(?:Pak Guntur|Pak Izudin|Pak Muhammad|Pak Izzudin|Guntur|Izudin)', text, re.IGNORECASE))
print(f"Reviewer name mentions: {len(matches)}")

for i, m in enumerate(matches[:8]):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 600)
    print(f"\n--- Mention {i+1} ---")
    print(text[start:end])
