N = int(input())
s = [i for i in range(N+1)]
if N < 3:
    print(s[N])
else:
    for i in range(3,N+1):
        s[i] = s[i-1] + s[i-2]
    print(s[N]%10007)