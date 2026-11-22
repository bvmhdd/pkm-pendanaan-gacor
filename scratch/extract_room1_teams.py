import os
import re

with open(r"D:\Belajar\Semester 5\Project\PKM\PKP PKM 2026\pkp pkm room1.md", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Find team transitions
# Often announced by moderator: 'kelompok 1', 'kelompok nomor urut', etc.
teams = re.findall(r'(kelompok\s*(?:nomor\s*urut\s*)?(\d{1,2})[^.\n]{10,120})', text, re.IGNORECASE)
print(f"Team mentions: {len(teams)}")
for t in teams[:15]:
    print("  *", t[0])

# Let's see some specific parts: where reviewer speaks
# Usually 'Pak' or 'Bapak' or 'Terima kasih'
print("\nReviewer comments samples:")
rev_samples = re.findall(r'(?:reviewer|penilai|bapak penilai|catatan dari saya|pertanyaan saya)[^.\n]{10,150}', text, re.IGNORECASE)
for r in rev_samples[:10]:
    print("  >", r.strip())
