import sys
lines = [list(map(int,data.split())) for data in sys.stdin.readlines()]
N,M = lines[0]
numbers = []
card = lines[1]
for i,vali in enumerate(card):
    second = (card[i+1:])
    for j,valj in enumerate(second):
        thrid = (second[j+1:])
        for k in thrid:
            if len(thrid)>0:
                numbers.append(vali+valj+k)
subtracts = list(map(lambda x:M-x if x-M <= 0 else x,numbers))
print(numbers[subtracts.index(min(subtracts))])