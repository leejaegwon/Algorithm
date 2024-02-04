N = int(input())
def get_case(x:int):
    if x < 4:
        return 2**(x-1)
    else:
        s = [0] * (x+1)
        s[1] = 1
        s[2] = 2
        s[3] = 4
        for i in range(4,x+1):
            s[i] = s[i-3] + s[i-2] + s[i-1]
        return s[x]
for _ in range(N):
    case = get_case(int(input()))
    print(case)