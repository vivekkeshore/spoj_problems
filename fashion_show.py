# Vivek Keshore
# http://www.spoj.com/problems/FASHION/

inputs = int(raw_input())
for inp in xrange(inputs):
    models = int(raw_input())
    men = raw_input().split()
    women = raw_input().split()
    men = [int(i) for i in men]
    women = [int(i) for i in women]
    men.sort()
    women.sort()
    value = 0
    for i in xrange(models):
        value += int(men[i]) * int(women[i])

    print value
