# Vivek Keshore
# http://www.spoj.com/problems/SHAKTI/

inputs = int(raw_input())
for inp in xrange(inputs):
    n = int(raw_input())

    if n % 2 == 0:
        print 'Thankyou Shaktiman'
    else:
        print 'Sorry Shaktiman'
