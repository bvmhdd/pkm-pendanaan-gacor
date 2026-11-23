# -*- coding: utf-8 -*-
with open('scratch/chatgpt_share.html', 'r', encoding='utf-8') as f:
    html = f.read()

import json
import re

start_marker = 'streamController.enqueue('
p_start = html.find(start_marker, 552000)
if p_start != -1:
    p_start += len(start_marker)
    # The enqueue call is streamController.enqueue("...");</script>
    p_end = html.find(');</script>', p_start)
    raw_enq = html[p_start:p_end]
    print(f"Captured raw_enq len: {len(raw_enq)}")
    
    with open('scratch/full_stream_raw.txt', 'w', encoding='utf-8') as out:
        out.write(raw_enq)
    
    # It's a JSON string literal: "..."
    # Let's decode it
    try:
        decoded_str = json.loads(raw_enq)
        print("Successfully json.loads decoded_str! Length:", len(decoded_str))
        with open('scratch/decoded_stream.txt', 'w', encoding='utf-8') as out:
            out.write(decoded_str)
        
        # Now let's try to parse decoded_str as JSON (it's turbo-stream / react-router data)
        try:
            parsed_data = json.loads(decoded_str)
            print("Successfully parsed turbo-stream json! Type:", type(parsed_data))
            with open('scratch/parsed_turbo.json', 'w', encoding='utf-8') as out:
                json.dump(parsed_data, out, indent=2)
        except Exception as pe:
            print("decoded_str is not pure JSON, parsing line-by-line or turbo-stream chunks:", pe)
    except Exception as e:
        print("Failed json.loads on raw_enq:", e)
