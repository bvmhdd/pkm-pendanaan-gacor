import urllib.request
import json
import re

url = 'https://chatgpt.com/share/6b03da57-b7a4-83ec-9699-2d20ddb5a9bb'
req = urllib.request.Request(
    url, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
)

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"HTML length: {len(html)}")
        with open('scratch/chatgpt_share.html', 'w', encoding='utf-8') as f:
            f.write(html)
        
        m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html)
        if m:
            print("Found __NEXT_DATA__!")
            data = json.loads(m.group(1))
            with open('scratch/chatgpt_share.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            print("Saved __NEXT_DATA__ to scratch/chatgpt_share.json")
        else:
            print("No __NEXT_DATA__ tag found. Preview:")
            print(html[:500])
except Exception as e:
    print(f"Error fetching URL: {e}")
