# Vivek Keshore
# http://www.spoj.com/problems/EBOXES/

import sys


inputs = int(sys.stdin.readline())
for inp in xrange(inputs):
    data = sys.stdin.readline().split()
    data = map(int, data)
    n, k, t, f = data[0], data[1], data[2], data[3]
    print n + k * ((f - n) / (k - 1))
