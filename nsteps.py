# Vivek Keshore
# http://www.spoj.com/problems/NSTEPS/

inputs = int(raw_input())
for inp in xrange(inputs):
    d = raw_input().split()
    x, y = int(d[0]), int(d[1])

    if x == y or (x - 2) == y:
        if (x % 2 == 0) and (y % 2 == 0):
            print x + y

        elif (x % 2 != 0) and (y % 2 != 0):
            print x + y - 1

        else:
            print 'No Number'
    else:
        print 'No Number'
