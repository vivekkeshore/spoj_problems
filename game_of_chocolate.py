# Vivek Keshore
# http://www.spoj.com/problems/NAJGC/
#
import sys
from fractions import gcd

inputs = int(sys.stdin.readline())
for inp in xrange(inputs):
    data = sys.stdin.readline().strip().split()
    data = map(int, data)
    x1, y1, x2, y2 = data[0], data[1], data[2], data[3]

    if x1 == y1 == 0:
        print 'Case {}: {}'.format(inp+1, 0)

    else:
        nr = x1 * (x2 + 1) + y1 * (y2 + 1);
        dr = (x1 + y1) * (x2 + y2 + 1);
        d = gcd(nr, dr);
        nr = nr / d;
        dr = dr / d;
        print 'Case {}: {}/{}'.format(inp+1, nr, dr)
