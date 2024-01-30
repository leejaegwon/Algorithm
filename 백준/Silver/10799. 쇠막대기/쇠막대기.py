import sys
input = sys.stdin.readline().strip()
laser = input.replace('()','X')
bar = []
total = []
for mark in laser:
    if mark == "(":
        bar.append(0)
    elif mark == ")":
        popx = bar.pop()
        total.append(popx)
        if bar:
            bar[-1] += popx
    elif mark == "X":
        if len(bar) == 0:
            continue
        bar[-1] += 1
print(sum(total)+len(total))
    