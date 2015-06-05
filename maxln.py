# Vivek Keshore
# http://www.spoj.com/problems/MAXLN/

inputs = int(raw_input())
for inp in xrange(inputs):
    r = float(raw_input())
    x = (4.0 * r * r) + 0.25
    print 'Case {}: {:.2f}'.format(inp+1, x)
