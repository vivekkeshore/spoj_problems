# Vivek Keshore
# http://www.spoj.com/problems/ARMY/

inputs = int(raw_input())
for inp in xrange(inputs):
    raw_input()  # Blank line in input
    ndata = raw_input().split()
    gdstrn = raw_input().split()
    mgdstrn = raw_input().split()

    ng, nm = int(ndata[0]), int(ndata[1])
    gdstrn = [int(i) for i in gdstrn]
    mgdstrn = [int(i) for i in mgdstrn]

    gdstrn.sort(reverse=True)
    mgdstrn.sort(reverse=True)

    mgd = mgdstrn[0]
    gd = gdstrn[0]

    if mgd <= gd:
        print 'Godzilla'
    else:
        print 'MechaGodzilla'
