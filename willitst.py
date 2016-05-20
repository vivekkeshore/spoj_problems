# Vivek Keshore
# http://www.spoj.com/problems/WILLITST/

while True:
    try:
        n = int(raw_input())
    except EOFError:
        break

    while n % 2 == 0:
        n /= 2

    if n == 1:
        print 'TAK'
    else:
        print 'NIE'
