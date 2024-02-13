N = int(input())

# % 나머지
# // 몫
comlist = []
count5 = 1
count3 = 1
while N > 5 * count5:
    if (N - 5 * count5) % 3  == 0:
        comlist.append(count5 + ((N - 5 * count5) // 3))
    else:
        pass
    count5 += 1
if N % 3 == 0:
    comlist.append(N // 3) 
if N % 5 == 0:
    comlist.append(N //5 )    
print( -1 if len(comlist)==0 else min(comlist)) 