# -*- coding: utf-8 -*-
with open('scratch/chat_messages.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect messages that are not React code
import re
blocks = text.split('========================================')
print(f"Total blocks: {len(blocks)}")

clean_messages = []
for b in blocks:
    if not b.strip(): continue
    # skip javascript / React / DIL code
    if 'function __dilSafe' in b or 'DIL.render' in b:
        continue
    clean_messages.append(b.strip())

print(f"Clean messages: {len(clean_messages)}")

with open('scratch/clean_chat.md', 'w', encoding='utf-8') as out:
    for i, cm in enumerate(clean_messages):
        out.write(f"\n\n### DIALOGUE ITEM {i+1}\n\n")
        out.write(cm + "\n")

print("Saved clean_chat.md!")
for i, cm in enumerate(clean_messages[:10]):
    lines = cm.split('\n')
    header = lines[0] if lines else ""
    preview = "\n".join(lines[1:6])
    print(f"[{i+1}] {header}")
    print(preview[:200])
    print("-" * 40)
