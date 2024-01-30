line = input()
line = line.strip()
strings = []
tag = False
stack = []
for word in line:
    if word == "<":
        if len(stack) > 0:
            strings.append(stack)
        strings.append('<')
        tag = True
        continue
    elif word == ">":
        strings.append('>')
        stack = []
        tag = False
        continue
    if tag:
        strings.append(word)
    else:
        if word == ' ':
            strings.append(stack)
            strings.append(' ')
            stack = []
        else:
            stack.append(word)
if len(stack) > 0:
    strings.append(stack)

for i in strings:
    if type(i) == list:
        while len(i) >0:
            print(i.pop(),end='')
    else:
        print(i,end='')
