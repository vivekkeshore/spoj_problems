# Vivek Keshore
# http://www.spoj.com/problems/SCPC11D/

while True:
    try:
        inp = raw_input().split()
    except EOFError:
        break

    inp = [int(i) for i in inp]
    inp.sort()
    a, b, c = inp

    if a > 0 and b > 0 and c > 0:
        if (a * a) + (b * b) == (c * c):
            print 'right'
        else:
            print 'wrong'
