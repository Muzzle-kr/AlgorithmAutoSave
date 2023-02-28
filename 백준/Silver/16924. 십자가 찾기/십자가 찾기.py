from collections import deque
n, m = map(int, input().split())
maps = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visit = [[0] * m for _ in range(n)]
isFailed = False

for i in range(n):
    maps.append(list(input()))
    
answer = []

def checkCross(x, y):
    for i in range(4):
        dx = direction[i][0] + x
        dy = direction[i][1] + y
        
        if 0 <= dx < n and 0 <= dy < m and maps[dx][dy] == "*":
            continue
        else:
            return False
    return True

def handleVisit(x, y, distance):
            visit[x][y] = 1
            
            for idx in range(1, distance + 1):
                for i in range(4):
                    dx = direction[i][0] * idx + x
                    dy = direction[i][1] * idx + y
                    visit[dx][dy] = 1
                    
def bfs(x, y):
    distance = 0
    idx = 1

    while True:
        for i in range(4):
            dx = direction[i][0] * idx + x
            dy = direction[i][1] * idx + y
            
            if 0 <= dx < n and 0 <= dy < m and maps[dx][dy] == "*":
                continue
            else:
                return distance
            
        distance += 1
        idx += 1
        
    

for i in range(n):
    for j in range(m):
        if maps[i][j] == "*":
            distance = bfs(i, j)
            
            if distance > 0:
                handleVisit(i, j, distance)
                for k in range(1, distance + 1):
                    answer.append((i+1, j+1, k))

total = 0
total2 = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == "*":
            total += 1

        if visit[i][j] == 1:
            total2 += 1


if total == total2:
    print(len(answer))
    for a in answer:
        print(*a)
else:
    print(-1)