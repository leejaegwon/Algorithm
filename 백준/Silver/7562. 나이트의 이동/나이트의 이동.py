from collections import deque
N = int(input())
case = []
for _ in range(N):
    chs_len = int(input())
    box = [[0] * chs_len for _ in range(chs_len)]
    visited = [[False] * chs_len for _ in range(chs_len)]

    sy, sx = map(int, input().split())
    dest_y, dest_x = map(int, input().split())

    if (sy, sx) == (dest_y, dest_x):
        case.append(0)
        continue

    q = deque([(sy, sx)])
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    while q:
        cy, cx = q.popleft()

        for i in range(8):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if nx < 0 or ny < 0 or nx >= chs_len or ny >= chs_len or visited[ny][nx]:
                continue

            q.append((ny, nx))
            box[ny][nx] = box[cy][cx] + 1
            visited[ny][nx] = True

            if (ny, nx) == (dest_y, dest_x):
                case.append(box[ny][nx])
                q.clear()
                break

print(*case, sep='\n')