# Vivek Keshore
# http://www.spoj.com/problems/GIRLSNBS/
while True:
    gb = raw_input().split()
    g, b = int(gb[0]), int(gb[1])
    if g > b:
        print (g + b) / (b + 1)
    elif b > g:
        print (b + g) / (g + 1)
    elif g == b == 0:
        print 0
    elif g == b == -1:
        break
    else:
        print 1
