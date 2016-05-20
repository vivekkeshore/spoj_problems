# Vivek Keshore
# http://www.spoj.com/problems/AE00/

import sys


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1)
                       if n % i == 0)))

num = int(sys.stdin.readline())
count = 0

for n in xrange(1, num + 1):
    n_facts = factors(n)
    facts_len = len(n_facts)

    if facts_len % 2:  # odd number of factors
        count += (facts_len / 2) + 1
    else:
        count += facts_len / 2

print count
