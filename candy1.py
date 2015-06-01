# Vivek Keshore
# http://www.spoj.com/problems/CANDY/

while True:
    inputs = int(raw_input())
    if inputs == -1:
        break

    total = 0
    items = []

    for inp in xrange(inputs):
        item = int(raw_input())
        total += item
        items.append(item)

    if total % inputs != 0:
        print -1

    else:
        mean = total / inputs
        n = 0
        nsum = 0
        for item in items:
            if item > mean:
                n += 1
                nsum += item

        print nsum - (mean * n)

