import re

with open('input.txt', 'r') as f:
    text = f.read()

pattern = r'(\d{4})/(\d{1,2})/(\d{1,2})'
replacement = r'\2/\3/\1'
new_text = re.sub(pattern, replacement, text)

with open('output.txt', 'w') as f:
    f.write(new_text)
