# Vivek Keshore
# http://www.spoj.com/problems/MYQ1/

inputs = int(raw_input())
for inp in xrange(inputs):
    n = int(raw_input())

    if n == 1:
        print 'poor conductor'
        continue

    x = n % 10
    v = n
    if x == 2 or x == 1:
        p = 'W'
    elif x == 3 or x == 0 or x == 4 or x == 9:
        p = 'A'
    elif x == 5 or x == 8:
        p = 'M'
    else:
        p = 'W'

    if x == 2 or x == 3 or x == 1 or x == 0:
        d = 'L'
    else:
        d = 'R'

    if x == 2 or x == 3 or x == 4 or x == 6:
        n += (5-x)
    elif x == 1:
        n -= 1
    else:
        if x != 0 and x != 5:
            n += (10-x)

    print n/5, p, d
