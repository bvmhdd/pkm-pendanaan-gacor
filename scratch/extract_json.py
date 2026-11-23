# -*- coding: utf-8 -*-
with open('scratch/chatgpt_share.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
import json

# Check script 3
m_bootstrap = re.search(r'<script[^>]*id="client-bootstrap"[^>]*>(.*?)</script>', html, re.DOTALL)
if m_bootstrap:
    print("Found client-bootstrap, len:", len(m_bootstrap.group(1)))
    try:
        bs_data = json.loads(m_bootstrap.group(1))
        with open('scratch/bootstrap.json', 'w', encoding='utf-8') as out:
            json.dump(bs_data, out, indent=2)
        print("Saved bootstrap.json")
    except Exception as e:
        print("Error parsing bootstrap:", e)

# Check script 8 (streamController.enqueue)
m_stream = re.search(r'window\.__reactRouterContext\.streamController\.enqueue\((.*?)\);', html, re.DOTALL)
if m_stream:
    raw = m_stream.group(1)
    print("Found stream data, len:", len(raw))
    # It might be a JSON string or literal
    try:
        stream_data = json.loads(raw)
        with open('scratch/stream.json', 'w', encoding='utf-8') as out:
            if isinstance(stream_data, str):
                out.write(stream_data)
            else:
                json.dump(stream_data, out, indent=2)
        print("Saved stream.json")
    except Exception as e:
        print("Error parsing stream:", e)
        # write raw
        with open('scratch/stream_raw.txt', 'w', encoding='utf-8') as out:
            out.write(raw)
