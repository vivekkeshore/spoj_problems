# Vivek Keshore
# http://www.spoj.com/problems/DCEPC504/
# Run with Python3.x

inputs = int(input())
for inp in range(inputs):
    data = input().split()
    k = int(data[1])
    n = 0

    if k == 1:
        print('Male')
    elif k == 2:
        print('Female')
    else:
        k -= 1
        while k > 1:
            if k % 2 != 0:
                n += 1
            k = int(k / 2)

        if n % 2 == 0:
            print('Female')
        else:
            print('Male')
