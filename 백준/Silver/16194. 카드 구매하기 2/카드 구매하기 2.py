import sys
N = int(input())
p = {}
line = map(int,input().split(' '))
for i,val in enumerate(line):
    p[i+1] = val
def get_minval(s:list, x:int):
    minval = sys.maxsize
    n = 1
    while x > 0:
        minval = min(minval,s[x-1]+p[n])
        x = x - 1
        n = n + 1
    return minval
s = [0]*(N+1)
s[1] = p[1]
for i in range(2,N+1):
    s[i] = get_minval(s,i)
print(s[N])
