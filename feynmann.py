# Vivek Keshore
# http://www.spoj.com/problems/SAMER08F/

while True:
    inp = int(raw_input())
    if not inp:
        break
    else:
        s = 0
        for i in xrange(1, inp+1):
            s += ((inp - i) + 1) ** 2
        print s
