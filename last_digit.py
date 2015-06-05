# Vivek Keshore
# http://www.spoj.com/problems/LASTDIG/

inputs = int(raw_input())
for inp in xrange(inputs):
    d = raw_input().split()
    a, b, c = int(d[0]), int(d[1]), 10

    x = 1
    while b > 0:
        if b & 1 == 1:
            x = (x * a) % c
        a = (a * a) % c
        b >>= 1

    print x % c
