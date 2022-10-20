import re
from collections import Counter

# Open file and use counter to find most common word
words = findall(r'\w+', open('filename.txt').read().lower())
count = Counter(words).most_common(15)

# Output most common word 
print(count)
