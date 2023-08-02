import sys
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        temp = graph[x][y]
        # n-i ~ m-i까지
        
        for j in range(i + 1, n - i):
            x = j
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
        
        for j in range(i + 1, m - i):
            y = j
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
            
        for j in range(i + 1, n - i):
            x = n - j - 1
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
        
        for j in range(i + 1, m - i):
            y = m - j - 1
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
        
for i in range(n):
    print(*graph[i])