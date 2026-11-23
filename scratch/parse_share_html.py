# -*- coding: utf-8 -*-
import re
import json

with open('scratch/chatgpt_share.html', 'r', encoding='utf-8') as f:
    html = f.read()

m_title = re.search(r'<title>(.*?)</title>', html)
if m_title:
    print('Title:', m_title.group(1))

# Check meta description
m_desc = re.search(r'<meta name="description" content="(.*?)"', html)
if m_desc:
    print('Description:', m_desc.group(1))

# Search for conversation text in self.__next_f
matches = re.findall(r'self\.__next_f\.push\(\[1,\s*\"(.*?)\"\]\)', html)
print(f"Total next_f chunks: {len(matches)}")

extracted_text = []
for m in matches:
    # unescape string
    try:
        # replace escaped quotes and newlines
        unescaped = m.encode().decode('unicode_escape')
        # check if it contains parts of the conversation
        if any(w in unescaped.lower() for w in ['pkm', 'karsa cipta', 'judul', 'rekomendasi', 'ide', 'sistem']):
            extracted_text.append(unescaped)
    except Exception:
        pass

print(f"Relevant chunks found: {len(extracted_text)}")
with open('scratch/extracted_share_text.txt', 'w', encoding='utf-8') as out:
    for chunk in extracted_text:
        out.write("--- CHUNK ---\n")
        out.write(chunk + "\n")

print("Saved to scratch/extracted_share_text.txt")
