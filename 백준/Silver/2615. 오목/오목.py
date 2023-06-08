omok = [list(map(int, input().split())) for i in range(19)]

# 제일 왼쪽의 바둑돌을 찾기 위해 ➡️ ↗️ ⬇️ ↘️ 방향으로만 감
dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]

def find_omok(start, x, y):
    
    for i in range(4):
        cnt = 1
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        while 0 <= nx < 19 and 0 <= ny < 19 and start == omok[nx][ny]:
            cnt += 1
            # 6목 체크    
            if cnt == 5:
                if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and omok[nx+dx[i]][ny+dy[i]] == start:
                    break
                if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and omok[x-dx[i]][y-dy[i]] == start:
                    break
                
                print(start)
                print(x+1, y+1)
                exit()
                
            nx += dx[i]
            ny += dy[i]
            
        
        
                
for i in range(19):
    for j in range(19):
        if omok[i][j] != 0:
            find_omok(omok[i][j], i, j)
else:
    print(0)