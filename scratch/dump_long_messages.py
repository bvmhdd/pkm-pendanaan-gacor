# -*- coding: utf-8 -*-
with open('scratch/clean_chat.md', 'r', encoding='utf-8') as f:
    text = f.read()

items = text.split('### DIALOGUE ITEM')
print(f"Total dialogue items: {len(items)}")

for idx, item in enumerate(items):
    clean = item.strip()
    if len(clean) > 200:
        lines = clean.split('\n')
        print(f"\n=============================================")
        print(f"ITEM {idx} (length {len(clean)} chars)")
        print(f"=============================================")
        print("\n".join(lines[:35]))
        if len(lines) > 35:
            print("...")
            print("\n".join(lines[-15:]))
