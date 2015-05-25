# Vivek Keshore
# http://www.spoj.com/problems/TOANDFRO/

while True:
    inp = int(raw_input())
    if inp == 0:
        break

    text = raw_input()
    output = ''
    for i in xrange(inp):
        x = i
        y = ((((inp - 1) - i) * 2) + 1) + x
        for k in xrange(len(text)/inp):
            if k % 2 == 0:
                output += text[x]
                x += inp * 2
            else:
                output += text[y]
                y += inp * 2

    print output
