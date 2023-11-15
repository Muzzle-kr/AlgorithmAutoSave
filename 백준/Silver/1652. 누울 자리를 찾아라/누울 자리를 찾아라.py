n = int(input())
maps = [list(input()) for _ in range(n)]
w = 0
h = 0

for i in range(n):
    cnt = 0
    
    for j in range(n):
        
        if maps[i][j] == '.':
            cnt += 1
        
        # 가로를 찾다가 짐이나 벽을 만나면
        if j == n - 1 or maps[i][j] == 'X':
            if cnt >= 2:
                w += 1
                
            cnt = 0
    
for j in range(n):
    cnt = 0         
    for i in range(n):
        if maps[i][j] == '.':
            cnt += 1
                
        # 세로를 찾다가 짐이나 벽을 만나면
        if i == n - 1 or maps[i][j] == 'X':
            if cnt >= 2:
                h += 1
                
            cnt = 0

print(w, h)
        
        