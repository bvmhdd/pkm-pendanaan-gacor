# -*- coding: utf-8 -*-
with open('scratch/chatgpt_share.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

pos = html.find("Alternatif Judul PKM")
print(f"Position of title: {pos}")
if pos != -1:
    print("Surrounding 1000 characters:")
    print(html[max(0, pos-200):pos+1500])
