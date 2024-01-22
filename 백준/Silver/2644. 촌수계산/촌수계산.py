import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
graph = {}
for i in range(N):
    graph.setdefault(i+1,[])

a,b = map(int,input().split())

M = int(input().rstrip())
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = {i:False for i in graph.keys()}
distance = {i:0 for i in graph.keys()}
queue = deque()
queue.append(a)
visited[a] = True
distance[a] = 0

while queue:
    current = queue.popleft()
    cur_dist = distance[current]
    for nxt in graph[current]:
        if visited[nxt] == False:
            queue.append(nxt)
            visited[nxt] = True
            distance[nxt] += cur_dist + 1

print(distance[b] if distance[b] != 0 else -1)