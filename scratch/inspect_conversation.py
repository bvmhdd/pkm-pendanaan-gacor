# -*- coding: utf-8 -*-
import json
import re

# Let's inspect bootstrap.json
with open('scratch/bootstrap.json', 'r', encoding='utf-8') as f:
    bs = json.load(f)

print("Bootstrap keys:", list(bs.keys()))

# Let's search inside bootstrap for any text or messages
def search_dict(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if 'title' in k.lower() or 'message' in k.lower() or 'text' in k.lower() or 'prompt' in k.lower() or 'conversation' in k.lower():
                print(f"Match key at {path}.{k}: {str(v)[:100]}")
            search_dict(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            search_dict(item, f"{path}[{idx}]")

search_dict(bs)

# Let's also check all streamController.enqueue in the html
with open('scratch/chatgpt_share.html', 'r', encoding='utf-8') as f:
    html = f.read()

enqueues = re.findall(r'streamController\.enqueue\((.*?)\);', html)
print(f"Total streamController.enqueue: {len(enqueues)}")
for idx, eq in enumerate(enqueues):
    print(f"Enqueue {idx} len: {len(eq)}")
    # let's find strings in eq
    text_matches = re.findall(r'\"([^\"]{20,})\"', eq)
    print(f"  found {len(text_matches)} long strings")
    for tm in text_matches[:5]:
        if any(w in tm.lower() for w in ['pkm', 'judul', 'kesehatan', 'telekomunikasi', 'ide', 'dosen']):
            print(f"    -> {tm[:120]}")
