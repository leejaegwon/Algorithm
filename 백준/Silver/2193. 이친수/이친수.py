N = int(input())
d = [[]]*(N+1)
d[1] = [0,1]

for i in range(2,N+1):
    d[i] = [0,0]
    d[i][0] = d[i-1][0]+d[i-1][1]
    d[i][1] = d[i-1][0]
print(sum(d[N]))    