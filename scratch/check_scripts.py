# -*- coding: utf-8 -*-
with open('scratch/chatgpt_share.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

scripts = re.findall(r'<script([^>]*)>(.*?)</script>', html, re.DOTALL)
print(f"Total script tags: {len(scripts)}")
for i, (attrs, content) in enumerate(scripts):
    print(f"Script {i}: attrs='{attrs.strip()}', len={len(content)}")
    if len(content) > 100:
        print(f"   preview: {content[:150]}...")
