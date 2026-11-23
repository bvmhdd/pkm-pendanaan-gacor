# -*- coding: utf-8 -*-
import json
import re

with open('scratch/parsed_turbo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Data list length: {len(data)}")

# Turbo-stream flattens references. Let's find all strings in the list that look like text content
messages = []
for i, item in enumerate(data):
    if isinstance(item, str) and len(item.strip()) > 30:
        # Check if it looks like markdown or chat text
        if any(w in item.lower() for w in ['pkm', 'judul', 'latar belakang', 'kesehatan', 'telekomunikasi', 'sistem', 'sensor', 'metode', 'tujuan']):
            messages.append((i, item))

print(f"Candidate message strings: {len(messages)}")

with open('scratch/chat_messages.md', 'w', encoding='utf-8') as out:
    for idx, (pos, msg) in enumerate(messages):
        out.write(f"\n\n========================================\n")
        out.write(f"MESSAGE {idx+1} (data index {pos}):\n")
        out.write(f"========================================\n")
        out.write(msg + "\n")

print("Saved chat_messages.md! Let's preview the first few messages.")
for idx, (pos, msg) in enumerate(messages[:5]):
    print(f"--- Msg {idx+1} (len {len(msg)}) ---")
    print(msg[:300])
    print("...")
