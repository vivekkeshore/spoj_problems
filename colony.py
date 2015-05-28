# Vivek Keshore
# http://www.spoj.com/problems/COLONY/

year = int(raw_input())
position = int(raw_input())
n = 0
color = None

if position == 0:
    color = 'red'
elif position == 1:
    color = 'blue'
else:
    while position > 1:
        if position % 2 != 0:
            n += 1
        position = int(position / 2)

    if n % 2 == 0:
        color = 'blue'
    else:
        color = 'red'

if year % 2 == 0:
    print color
else:
    if color == 'red':
        print 'blue'
    else:
        print 'red'
