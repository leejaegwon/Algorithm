N = input().strip()
M = int(input())
if M == 0:
    broken = []
else:
    broken = list(map(int,input().split()))
enable = [i for i in range(10) if i not in broken]

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr,r-1):
                yield [arr[i]]+next
combi_nums = []
for combi in combinations(enable,len(N)):
    combi_nums.append(int(''.join(map(str,combi))))

if len(N) < 6:
    for combi in combinations(enable,len(N)+1):
        combi_nums.append(int(''.join(map(str,combi))))

if len(N) > 1:
    for combi in combinations(enable,len(N)-1):
        combi_nums.append(int(''.join(map(str,combi)))) 

from_cur = abs(100-int(N))
if combi_nums:
    find_min = min([abs(int(N)-i)+len(str(i)) for i in combi_nums])
    print(min(from_cur,find_min))
else:
    print(from_cur)