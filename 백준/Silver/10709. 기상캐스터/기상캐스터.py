n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
result = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if maps[i][j] == "c":
                cnt = 0
                result[i][j] = cnt
                visited[i][j] = True
                
                for k in range(j+1, m):
                    if maps[i][k] == ".":
                        cnt += 1
                        result[i][k] = cnt
                        visited[i][k] = True
                    else:
                        break
for r in result:
    print(*r)