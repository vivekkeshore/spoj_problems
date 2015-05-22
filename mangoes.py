# Vivek Keshore
# http://www.spoj.com/problems/MANGOES/

inputs = int(raw_input())
for inp in xrange(inputs):
    n = int(raw_input())
    print (((n-1)/2) * ((n-1)/2) % n)
