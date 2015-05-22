# Vivek Keshore
# http://www.spoj.com/problems/SBANK/

inp = int(raw_input())
for i in xrange(inp + (inp-1)):
    accounts = raw_input()
    if len(accounts) == 0:
        continue
    accounts = int(accounts)
    acc_nums = []
    acc_details = {}
    for account in xrange(accounts):
        acc_num = raw_input()
        acc_nums.append(acc_num)
        val = acc_details.get(acc_num)
        if val:
            acc_details[acc_num] = val + 1
        else:
            acc_details[acc_num] = 1

    acc_nums.sort()
    for acc_num in acc_nums:
        val = acc_details.get(acc_num)
        if val:
            print acc_num, val
            del acc_details[acc_num]
    print ''
