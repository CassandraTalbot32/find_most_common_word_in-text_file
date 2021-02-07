import re

from collections import Counter

words = findall(r'\w+', open('filename.txt').read().lower())
count = Counter(words).most_common(15)
print(count)
