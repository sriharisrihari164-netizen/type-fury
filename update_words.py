import urllib.request
import re

print("Downloading 50,000 word frequency list...")
url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/en/en_50k.txt"
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    lines = response.read().decode('utf-8').splitlines()

# Extract words (first column) and filter length > 2
words = []
for line in lines:
    parts = line.strip().split()
    if parts:
        word = parts[0]
        # remove quotes and ensure it's a typing friendly word
        if len(word) > 2 and word.isalpha() and word.isascii():
            words.append(word)
    if len(words) >= 30000:
        break

# Format into JS array
js_array = "const COMMON_WORDS = [\n    "
js_array += ",\n    ".join([", ".join(f'"{w}"' for w in words[i:i+15]) for i in range(0, len(words), 15)])
js_array += "\n];"

file_path = r"c:\Users\lenovo\Pictures\Screenshots\typeing\game.js"
print("Reading game.js...")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace existing COMMON_WORDS
pattern = re.compile(r"const COMMON_WORDS = \[\s*.*?\s*\];", re.DOTALL)
new_content = pattern.sub(js_array, content)

print("Writing to game.js...")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Successfully updated game.js with {len(words)} common words!")
