# Vivek Keshore
# http://www.spoj.com/problems/KOIREP/


import sys

inputs = sys.stdin.readline().strip().split()
n, m = int(inputs[0]), int(inputs[1])
output = 10000000000
rows = []
for inp in xrange(n):
    data = sys.stdin.readline().split()
    data = map(int, data)
    data.sort()
    rows.append(data)

for i in xrange(m):
    nums = []
    for j in xrange(n):
        nums.append(rows[j][i])

    diff = max(nums) - min(nums)
    if diff == 0:
        print 0
        break
    else:
        if diff < output:
            output = diff

print output

# for i, mushroom in enumerate(mushrooms):
#     v = mushroom
#     for j in xrange(i):
#         v += mushrooms[j]
#
#     for k in xrange(i+1, mush_len):
#         nums.append(v + mushrooms[k])
#         nums.append(mushroom + mushrooms[k])
#
# nums.sort()
# diffs = map(lambda x: abs(100 - x), nums)
# diffs_dict = {val: i for i, val in enumerate(diffs)}
#
# print nums[diffs_dict[min(diffs)]]
