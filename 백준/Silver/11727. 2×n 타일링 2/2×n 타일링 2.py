N = int(input())
s = [0]*(N+1)
s[1] = 1
if N < 2:
    print(s[N])
else:
    s[2] = 3
    for i in range(3,N+1):
        s[i] = s[i-1] + 2*s[i-2]
    print(s[N]%10007)