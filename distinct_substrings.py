# Vivek Keshore
# http://www.spoj.com/problems/SUBST1/

import sys


inputs = int(sys.stdin.readline())
for inp in xrange(inputs):
    s = sys.stdin.readline().strip()

    d = {}
    count = 0
    flag = False
    for i in xrange(len(s)):
        for j in xrange(len(s), i, -1):
            ss = s[i:j]
            try:
                d[ss]
                flag = True
                break
            except KeyError:
                d[ss] = True
                count += 1

        if flag:
            break

    sys.stdout.write(str(count) + '\n')
