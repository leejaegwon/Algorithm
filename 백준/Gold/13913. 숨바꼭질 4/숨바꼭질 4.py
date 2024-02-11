from collections import deque

move = [100000 for _ in range(100000+1)]

N,K = map(int,input().split())
if N == K:
    print(0)
    print(N)
    exit(0)
if N > K:
    print(N-K)
    print(*[N-i for i in range(N-K+1)])
    exit(0)
move[N] = 0
q = deque()
q.append((N,str(N)))
while q:
    cx,move_str = q.popleft()
    ctrl = [-1,1,cx]
    if cx == K:
        nxt_str = move_str
        q = 0
        break
    for dest in ctrl:
        nx = cx + dest
        if nx < 0 or nx >=100001:
            continue
        if move[nx] >= move[cx] + 1:
            move[nx] = move[cx] + 1
            nxt_str = str(move_str) +' '+ str(nx)
            q.append((nx,nxt_str))

print(move[K])
print(nxt_str)