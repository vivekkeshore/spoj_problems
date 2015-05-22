# Vivek Keshore
# http://www.spoj.com/problems/JULKA/

for i in xrange(10):
    total = int(raw_input())
    diff = int(raw_input())

    t_diff = total - diff
    if t_diff % 2 == 0:
        print (t_diff / 2) + diff
        print t_diff / 2
    else:
        print ''
