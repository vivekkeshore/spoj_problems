# Vivek Keshore
# http://www.spoj.com/problems/HC/

import sys


inputs = int(sys.stdin.readline())
for inp in xrange(inputs):
    n = int(sys.stdin.readline())
    lxh = 0
    for i in xrange(n):
        s = raw_input()
        if s == 'lxh':
            lxh += 1

    if lxh % 2:
        print 'lxh'
    else:
        print 'hhb'
