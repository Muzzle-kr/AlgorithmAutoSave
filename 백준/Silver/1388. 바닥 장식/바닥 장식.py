n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if maps[i][j] == '-':
                for k in range(j, m):
                    if maps[i][k] == '-':
                        visited[i][k] = True
                    else:
                        break
            else:
                for k in range(i, n):
                    if maps[k][j] == '|':
                        visited[k][j] = True
                    else:
                        break
            result += 1

print(result)