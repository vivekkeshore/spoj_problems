# Vivek Keshore
# http://www.spoj.com/problems/GLJIVE/


mushrooms = []
while True:
    try:
        n = int(raw_input())
        mushrooms.append(n)
    except EOFError:
        break

mush_len = len(mushrooms)

min_diff = 100
total = 0
final = 0
for mushroom in mushrooms:
    total += mushroom
    diff = abs(100 - total)

    if diff <= min_diff:
        min_diff = diff
        final = total

print final
