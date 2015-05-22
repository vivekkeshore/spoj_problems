# Vivek Keshore
# Problem link - http://www.spoj.com/problems/ACPC10A/

while True:
    try:
        inp = raw_input().split()
    except EOFError:
        break

    x, y, z = int(inp[0]), int(inp[1]), int(inp[2])
    if z - y != 0:
        if z - y == y - x and z - y:
            print 'AP', z + (z-y)

        elif z % y == 0 and y % x == 0:
            if z / y == y / x:
                print 'GP', z * (z/y)
            else:
                print ''

        else:
            print ''
    else:
        print ''
