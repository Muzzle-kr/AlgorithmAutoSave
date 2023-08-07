r1, c1, r2, c2 = map(int, input().split())
graph = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
total = (r2-r1+1) * (c2-c1+1)

# 우상좌하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

idx = 1
x, y = 0, 0

cnt = 1
d = 0
    
while total > 0:
    for _ in range(2):
        for _ in range(idx):
            if r1 <= x <= r2 and c1 <= y <= c2:
                graph[x-r1][y-c1] = cnt
                total -= 1
                m = cnt    
            
            x += dx[d]
            y += dy[d] 
            cnt += 1
            
        d = (d + 1) % 4
    idx += 1

max_len = len(str(m))

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(graph[i][j]).rjust(max_len), end=' ')
    print()