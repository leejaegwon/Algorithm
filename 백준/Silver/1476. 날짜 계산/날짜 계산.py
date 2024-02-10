a,b,c = map(int,input().split())
e,s,m = 0,0,0
day = 0
while not (e==a and s ==b and m == c):
    e += 1
    s += 1
    m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
    day += 1
print(day)
