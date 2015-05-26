# Vivek Keshore
# http://www.spoj.com/problems/IITKWPCA/

inputs = int(raw_input())
for inp in xrange(inputs):
    text = raw_input()
    print len(set(text.split()))
