# -*- coding: utf-8 -*-
with open('scratch/chatgpt_share.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
import json

enqueues = re.findall(r'streamController\.enqueue\((.*?)\);', html, re.DOTALL)
print(f"Total enqueues: {len(enqueues)}")

eq0 = enqueues[0]
with open('scratch/eq0_raw.txt', 'w', encoding='utf-8') as f:
    f.write(eq0)

# In turbo-stream or react-router, eq0 is often a JSON-escaped string like:
# "[{...}, ...]"
# Let's try parsing it as json
try:
    # It might start with a quote
    parsed = json.loads(eq0)
    print("Parsed JSON type:", type(parsed))
    with open('scratch/eq0_parsed.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, indent=2)
except Exception as e:
    print("Failed direct json.loads:", e)
    # try unescaping
    try:
        # replace double escapes
        raw_clean = eq0.strip()
        if raw_clean.startswith('"') and raw_clean.endswith('"'):
            # decode json string
            inner = json.loads(raw_clean)
            inner_parsed = json.loads(inner)
            print("Successfully double unescaped JSON!")
            with open('scratch/eq0_parsed.json', 'w', encoding='utf-8') as f:
                json.dump(inner_parsed, f, indent=2)
    except Exception as e2:
        print("Failed double unescape:", e2)

# Also let's extract all unicode strings
strings = re.findall(r'\"([^\"]*)\"', eq0)
print(f"Total string tokens: {len(strings)}")
with open('scratch/eq0_strings.txt', 'w', encoding='utf-8') as f:
    for s in strings:
        # unescape unicode
        try:
            u = s.encode('utf-8').decode('unicode_escape')
            if len(u.strip()) > 5:
                f.write(u + "\n---\n")
        except:
            f.write(s + "\n---\n")

print("Saved eq0_strings.txt")
