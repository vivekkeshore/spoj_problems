# Vivek Keshore
# http://www.spoj.com/problems/PHONELST/

inputs = int(raw_input())
for inp in xrange(inputs):
    nums = int(raw_input())
    numbers = []
    for num in xrange(nums):
        numbers.append(raw_input())
    numbers.sort()
    for i in xrange(1, len(numbers)):
        a = numbers[i-1]
        b = numbers[i]
        if a == b[:len(a)]:
            print 'NO'
            break
    else:
        print 'YES'
