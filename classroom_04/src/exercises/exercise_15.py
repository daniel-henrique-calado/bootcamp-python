"""
Detect how many times a word apears in phrase.
"""
text = "The brown fox jumps over a lazy dog." 

words = text.split()
count_words = {}

for word in words:
    if word in count_words:
        count_words[word] += 1
    else:
        count_words[word] = 1

print(count_words)