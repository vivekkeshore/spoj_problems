# Vivek Keshore
# http://www.spoj.com/problems/PALIN/


def make_palindrome(num):
    palin_num = ''
    num_len = len(num)
    palin_num += num[:(num_len/2)]
    palin_num = palin_num[::-1]
    if num_len % 2 != 0:
        palin_num = num[:(num_len/2)+1] + palin_num
    else:
        palin_num = num[:num_len/2] + palin_num

    return palin_num


inp = int(raw_input())
for ini in xrange(inp):
    num = (raw_input())
    if len(num) > 1:
        palin_num = make_palindrome(num)
        if palin_num and palin_num > num:
            print palin_num
            continue

    if len(num) == 1:
        print '11'
        continue

    palin_num = ''
    i = len(num) / 2
    if len(num) % 2 != 0:
        i += 1

    while i >= 0:
        digit = int(num[i-1])
        digit += 1

        if digit > 9:
            if i == 1:
                palin_num += '01'
                break
            palin_num += '0'
            i -= 1
        else:
            palin_num += str(digit)
            break

    for i in xrange(i-2, -1, -1):
        palin_num += num[i]

    palin_num = palin_num[::-1]
    if len(num) % 2 != 0:
        palin_num += palin_num[-2::-1]
    else:
        if len(palin_num) > len(num)/2:
            palin_num += palin_num[-2::-1]
        else:
            palin_num += palin_num[::-1]

    print palin_num
