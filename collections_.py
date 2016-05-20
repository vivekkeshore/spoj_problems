# Vivek Keshore
# http://www.spoj.com/problems/IITKWPCO/

import sys


inputs = int(sys.stdin.readline())
for inp in xrange(inputs):
    n = int(sys.stdin.readline())
    data = sys.stdin.readline().split()
    data = map(int, data)
    data.sort()
    count = 0
    lst_len = len(data)
    i = 0

    while len(data) > 1 and i < len(data):
        try:
            x = data.index(data[i] * 2)
            data.pop(x)
            data.pop(i)
            count += 1

        except ValueError:
            i += 1

    print count
