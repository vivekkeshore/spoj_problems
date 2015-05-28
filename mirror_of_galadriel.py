# Vivek Keshore
# http://www.spoj.com/problems/AMR12D/

inputs = int(raw_input())
for inp in xrange(inputs):
    text = raw_input()
    t_len = len(text)

    i = 0
    flag = True
    while i < (t_len / 2):
        if text[i] != text[t_len - i - 1]:
            print 'NO'
            flag = False
            break

        i += 1

    if flag:
        print 'YES'
