# Vivek Keshore
# http://www.spoj.com/problems/BINGO/

import re
from fractions import gcd

text = ''
while True:
    try:
        text += raw_input()
    except EOFError:
        break

groups = text.split('BULLSHIT')
groups.pop()
grp_len = len(groups)

sum_words = 0
for group in groups:
    words = group.split()
    all_words = []
    for word in words:
        word = word.lower()
        wordset = re.split(r"[^a-z]", word)
        for w in wordset:
            word = re.sub('\W+', '', w)
            if len(word):
                all_words.append(word)

    all_words = set(all_words)
    sum_words += len(all_words)

g = gcd(sum_words, grp_len)
print sum_words/g, '/', grp_len/g
