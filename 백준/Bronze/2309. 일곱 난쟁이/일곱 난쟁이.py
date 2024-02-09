import sys
lines = [int(i.strip()) for i in sys.stdin.readlines()]

def combinations(array,r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:],r-1):
                yield [array[i]] + next

for i in combinations(lines,7):
   
    if sum(i) == 100:
        for val in sorted(i):
            print(val)
        break