import sys
lines = [line for line in sys.stdin.readlines()]
N,M,V = map(int,lines[0].split())
graph = {}

for i in range(1,N+1):
    graph.setdefault(i,[])

for line in lines[1:]:
    n1,n2 = map(int,line.split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
for key,values in graph.items():
    values.sort()

def dfs_stack(graph, node, visited):
    lines = []
    #print(node)
    lines.append(node)
    stack = [node]
    visited[node] = True
    while len(stack) > 0:
        current = stack[-1]
        for nxt in graph[current]:
            if not visited[nxt]:
                stack.append(nxt)
                visited[nxt] = True
                # print(nxt)
                lines.append(nxt)
                break
        else:
            (stack.pop())

    return lines

def bfs(graph, node, visited):
    lines = []
    #print(node)
    lines.append(node)
    queue = [node]
    visited[node] = True
    while len(queue) > 0:
        current = queue.pop(0)
        for nxt in graph[current]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True
                # print(nxt)
                lines.append(nxt)
    return lines

lines = dfs_stack(graph, V, visited={i:False for i in graph.keys()})
print(*lines,sep=' ')
lines = bfs(graph, V, visited={i:False for i in graph.keys()})
print(*lines,sep=' ')