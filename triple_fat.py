# Vivek Keshore
# http://www.spoj.com/submit/EIGHTS/

inputs = int(raw_input())
for inp in xrange(inputs):
    k = int(raw_input())
    x = 192
    if k == 1:
        print x
    else:
        print ((k - 1) * 250) + x
