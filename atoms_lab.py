# Vivek Keshore
# http://www.spoj.com/problems/ATOMS/

from math import log

inputs = int(raw_input())
for inp in xrange(inputs):
    data = raw_input().split()
    n, k, m = int(data[0]), int(data[1]), int(data[2])

    if n > m:
        print 0
    else:
        print int(log(m/n) / log(k))
