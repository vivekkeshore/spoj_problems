# Vivek Keshore
# http://www.spoj.com/problems/IITWPC4A/

import re

inputs = int(raw_input())
for inp in xrange(inputs):
    text = raw_input()
    d = raw_input().split()
    m, n = int(d[0]), int(d[1])
    t_len = len(text)
    ma = 'a' * m
    nb = 'b' * n

    positions = [x.start() for x in re.finditer(ma, text)]
    p_len = len(positions)

    if m < n:
        print t_len, (t_len - (len(ma) * p_len) + (len(nb) * p_len))
    elif m > n:
        print (t_len - (len(ma) * p_len) + (len(nb) * p_len)), t_len
    else:
        print t_len, t_len
