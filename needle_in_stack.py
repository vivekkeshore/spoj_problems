# Vivek Keshore
# http://www.spoj.com/problems/NHAY/

while True:
    try:
        needle_len = raw_input()
    except EOFError:
        break

    needle_len = int(needle_len)
    needle = raw_input()
    haystack = raw_input()

    if len(haystack) < needle_len:
        print ''
        continue

    index = 0
    while index < len(haystack):
        index = haystack.find(needle, index)
        if index > 0:
            print index
            index += 1
        else:
            break
    print ''
