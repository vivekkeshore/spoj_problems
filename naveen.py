numlist = [1, 2, 3, 8, 4, 7, 9, 6, 5, 10]
REQUIRED_SUM = 10

from itertools import combinations

for i in xrange(len(numlist)):
  for sumlist in combinations(numlist, i):
    if sum(sumlist) == REQUIRED_SUM:
          print list(sumlist)
