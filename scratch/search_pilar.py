# -*- coding: utf-8 -*-
import pypdf
import re

pdf_path = r'd:\Belajar\Semester 5\Project\PKM\10-pedoman\PANDUAN-PKM-2026_versi_full.pdf'
reader = pypdf.PdfReader(pdf_path)
print(f"Total pages: {len(reader.pages)}")

# Search for pilar, tema, fokus
pilar_pages = []
for idx, page in enumerate(reader.pages):
    txt = page.extract_text() or ''
    if re.search(r'\bpilar\b', txt, re.I):
        pilar_pages.append((idx + 1, txt))

print(f"Total pages with 'pilar': {len(pilar_pages)}")
for pno, txt in pilar_pages:
    print(f"\n--- Page {pno} ---")
    lines = txt.split('\n')
    for l in lines:
        if re.search(r'pilar|tema|prioritas|kesehatan', l, re.I):
            print("  ", l.strip())
