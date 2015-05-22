# Vivek Keshore
# http://www.spoj.com/problems/CDGLF1/

inputs = int(raw_input())
for inp in xrange(inputs):
    l1 = raw_input().split()
    prices = raw_input().split()
    brooms, kejru = int(l1[0]), int(l1[1])
    prices = [int(price) for price in prices]
    prices.sort()
    money = 0
    for i in xrange(kejru):
        if prices[i] < 0:
            money += -1 * prices[i]
        else:
            break

    print money
