import sys
d = [[]]*(100000+1)
d[1] = [1,0,0]
d[2] = [0,1,0]
d[3] = [1,1,1]
for i in range(4,100000+1):
    d[i] = [(d[i-1][1]+d[i-1][2])%1000000009,
            (d[i-2][0]+d[i-2][2])%1000000009,
            (d[i-3][0]+d[i-3][1])%1000000009]

lines = [int(i) for i in sys.stdin.readlines()]
for line in lines[1:]:
    ans = d[line][0] + d[line][1] + d[line][2]
    print(ans%1000000009)