# Vivek Keshore
# Problem link - http://www.spoj.com/problems/ADDREV/

inp = int(raw_input())
for i in xrange(inp):
    x = (raw_input().split())
    a, b = (x[0][::-1]), (x[1][::-1])
    addition = int(a) + int(b)
    print int(str(addition)[::-1])
