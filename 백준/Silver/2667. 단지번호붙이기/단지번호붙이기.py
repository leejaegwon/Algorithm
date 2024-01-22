import sys
from collections import deque 
input = sys.stdin.readline

N = int(input().rstrip())
given_map = []
for _ in range(N):
    given_map.append(list(map(int,input().rstrip())))
#print(given_map)
visited = [[False] * N for _ in range(N)]
#print(visited)

apts = []
for i in range(N):
    for j in range(N):
        if given_map[i][j] == 0 or visited[i][j] == True:
            continue
        apt = 1
        queue = deque()
        queue.append((i,j))
        visited[i][j] = True
        while queue:
            x,y = queue.popleft()
            # u d r l
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >=N or ny < 0 or ny >=N or visited[nx][ny] == True:
                    continue
                if given_map[nx][ny] == 0:
                    visited[nx][ny] = False
                    continue
                if given_map[nx][ny] == 1:
                    #given_map[nx][ny] = given_map[x][y] + 1
                    apt += 1
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    
                    
        apts.append(apt)
apts.sort()
print(len(apts))
print(*apts, sep='\n')