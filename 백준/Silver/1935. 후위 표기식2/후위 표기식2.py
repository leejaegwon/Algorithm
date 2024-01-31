import sys
import queue
lines = [i.strip() for i in sys.stdin.readlines()]
vals = {}
N = int(lines[0])
for i in range(N):
    vals[chr(65+i)] = float(lines[2+i])
stack = []
for word in lines[1]:
    if word in vals:
        stack.append(vals[word])
    else:
        stack.append(word)
oper = []
for word in stack:
    if type(word) == float:
        oper.append(word)
    else:
        if word == '*':
            a = oper.pop()
            b = oper.pop()
            oper.append(b*a)
        elif word == '/':
            a = oper.pop()
            b = oper.pop()
            oper.append(b/a)
        elif word == '-':
            a = oper.pop()
            b = oper.pop()
            oper.append(b-a)
        elif word == '+':
            a = oper.pop()
            b = oper.pop()
            oper.append(b+a)
print(f'{oper.pop():.2f}')