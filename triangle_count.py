# Vivek Keshore
# http://www.spoj.com/problems/TRICOUNT/

inputs = int(raw_input())
for inp in xrange(inputs):
    n = int(raw_input())
    print int((n * (n + 2) * ((2 * n) + 1)) / 8)
