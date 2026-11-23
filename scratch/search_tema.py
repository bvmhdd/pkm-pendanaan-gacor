# -*- coding: utf-8 -*-
import pypdf
import re

pdf_path = r'd:\Belajar\Semester 5\Project\PKM\10-pedoman\PANDUAN-PKM-2026_versi_full.pdf'
reader = pypdf.PdfReader(pdf_path)

# Check first 30 pages
print("--- SEARCHING FIRST 30 PAGES ---")
for i in range(min(30, len(reader.pages))):
    text = reader.pages[i].extract_text() or ''
    # Look for tema, bidang fokus, atau pilar
    for line in text.split('\n'):
        if any(w in line.lower() for w in ['tema', 'bidang fokus', 'prioritas', 'sdgs', 'tujuan pembangunan berkelanjutan', 'transformasi']):
            print(f"P.{i+1}: {line.strip()}")
