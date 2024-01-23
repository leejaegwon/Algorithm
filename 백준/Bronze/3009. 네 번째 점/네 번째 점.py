import sys
lines = [i for i in sys.stdin.readlines()]
num_set_x = []
num_set_y = []
for line in lines:
    a,b = map(int,line.split())
    if a in num_set_x:
        num_set_x.remove(a)
    else:
        num_set_x.append(a)
    if b in num_set_y:
        num_set_y.remove(b)
    else:
        num_set_y.append(b)

print(num_set_x[0],num_set_y[0])