# Vivek Keshore
# http://www.spoj.com/problems/ARITH/

import sys

def add_subs(num1, num2, num1_len, num2_len, sol, sol_len, opr):
    m = max(num1_len, num2_len + 1, sol_len)

    print ' ' * (m - num1_len) + str(num1)
    print ' ' * (m - (num2_len + 1)) + opr + str(num2)
    print ' ' * (m - (max(sol_len, num2_len + 1))) + '-' * max(sol_len, num2_len + 1)
    print ' ' * (m - sol_len) + str(sol)


def multiply(num1, num2, num1_len, num2_len):
    sol = num1 * num2
    sol_len = len(str(sol))
    m = max(num1_len, num2_len + 1, sol_len)

    print ' ' * (m - num1_len) + str(num1)
    print ' ' * (m - (num2_len + 1)) + opr + str(num2)
    rem = num2 % 10
    num2 /= 10
    res = rem * num1
    if len(str(res)) >= (num2_len + 1):
        print ' ' * (m - (max(num2_len + 1, len(str(res))))) + '-' * max(num2_len + 1, len(str(res)))
    else:
        print ' ' * (m - (max(num2_len + 1, len(str(res))))) + '-' * (num2_len + 1)
    print ' ' * (m - len(str(res))) + str(res)

    c = 1
    while num2 > 0:
        rem = num2 % 10
        num2 /= 10
        res = rem * num1
        print ' ' * (m - c - len(str(res))) + str(res)
        c += 1
    if num2_len > 1:
        print ' ' * (m - sol_len) + '-' * (sol_len)
        print ' ' * (m - sol_len) + str(sol)

inputs = int(sys.stdin.readline())
for inp in xrange(inputs):
    expr = sys.stdin.readline().strip()

    if '+' in expr:
        expr = expr.split('+')
        opr = '+'
    elif '-' in expr:
        expr = expr.split('-')
        opr = '-'

    else:
        expr = expr.split('*')
        opr = '*'

    num1, num2 = int(expr[0]), int(expr[1])
    num1_len, num2_len = len(str(num1)), len(str(num2))
    if opr == '+':
        sol = num1 + num2
        sol_len = len(str(sol))
        add_subs(num1, num2, num1_len, num2_len, sol, sol_len, opr)

    elif opr == '-':
        sol = num1 - num2
        sol_len = len(str(sol))
        add_subs(num1, num2, num1_len, num2_len, sol, sol_len, opr)

    else:
        multiply(num1, num2, num1_len, num2_len)

    print ''
