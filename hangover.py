# Vivek Keshore
# http://www.spoj.com/problems/HANGOVER/

while True:
    inp = float(raw_input())
    if inp == 0.00:
        break

    i = 1
    frac_sum = 0.00
    while True and inp > 0.5:
        frac_sum += 1.0/(i+1.0)
        if frac_sum+1.0/(i+1.0) <= inp:
            i += 1
        else:
            i += 1
            break
    print i, 'card(s)'
