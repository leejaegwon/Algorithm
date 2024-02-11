from collections import deque

move = [100000 for _ in range(100000+1)]
N,K = map(int,input().split())
if N == K:
    print(0)
    exit(0)
move[N] = 0
q = deque()
q.append(N)
while q:
    cx = q.popleft()
    ctrl = [-1,1,cx]
    for dest in ctrl:
        nx = cx + dest
        if nx < 0 or nx >=100001:
            continue
        if nx == K:
            move[nx] = move[cx] + 1
            q.clear()
            break
        if move[nx] >= move[cx] + 1:
            q.append(nx)
            move[nx] = move[cx] + 1
print(move[K])