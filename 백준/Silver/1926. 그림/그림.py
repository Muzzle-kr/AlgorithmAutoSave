n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    result = 1
    q = [(x, y)]
    while q:
        x, y = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # print(f' nx: {nx}, ny: {ny}')
            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1 and visit[nx][ny] == False:
                result += 1
                visit[nx][ny] = True
                q.append((nx, ny))

    return result


cnt, maxv = 0, 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and visit[i][j] == False:
            visit[i][j] = True
            cnt += 1
            area = bfs(i, j)
            # print(f'{i}, {j}부터 시작되는 그림 발견, 넓이: {area}')
            maxv = max(maxv, area)

print(cnt)
print(maxv)