# Vivek Keshore
# http://www.spoj.com/problems/EQBOX/

import sys

inputs = int(sys.stdin.readline())
for inp in xrange(inputs):
    data = sys.stdin.readline().split()
    data = map(int, data)
    a, b, x, y = data[0], data[1], data[2], data[3]

    if max(a, b) >= min(x, y):
        sys.stdout.write('Escape is possible.\n')
    else:
        sys.stdout.write('Box cannot be dropped.\n')
