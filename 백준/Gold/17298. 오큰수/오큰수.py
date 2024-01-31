import sys
lines = [i.strip() for i in sys.stdin.readlines()]
n = int(lines[0])
nums = list(map(int,lines[1].split(' ')))

ans = [-1]* n
stack = []
stack.append(0)
for i in range(1,n):
    while stack and nums[stack[-1]] < nums[i]:
        ans[stack.pop()] = nums[i]
    stack.append(i)
print(*ans)