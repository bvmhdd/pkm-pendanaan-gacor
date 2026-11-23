# -*- coding: utf-8 -*-
with open('scratch/clean_chat.md', 'r', encoding='utf-8') as f:
    text = f.read()

items = text.split('### DIALOGUE ITEM')
print("--- FULL TEXT OF ITEM 104 (8 IDEAS) ---")
print(items[104])

print("--- FULL TEXT OF ITEM 442 (HEALTHTECH + TITLES) ---")
print(items[442][:4000])
