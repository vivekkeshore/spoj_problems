# Vivek Keshore
# Problem link - http://www.spoj.com/problems/FACTMUL/

mod = 109546051211  # prime factors 186583 and 587117
n = int(raw_input())
if n > 587116:
    print 0
else:
    fact = out = 1
    for i in xrange(2, n + 1):
        fact = (fact * i) % mod
        out = (out * fact) % mod
    print out
