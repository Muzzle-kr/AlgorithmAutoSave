from collections import deque
r, c = 12, 6
graph = [list(input().rstrip()) for i in range(r)]
chain_cnt = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def downPuyo():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                # 윗블록은 색깔, 아래 블록은 빈칸일 경우
                if graph[j][i] != '.' and graph[k][i] == '.':
                    graph[k][i] = graph[j][i]
                    graph[j][i] = '.'
                    break
                    
def delete_chain(arr):
    for x, y in arr:
        graph[x][y] = '.'
        
def bfs(i, j):
    q = deque()
    q.append((i, j))
    tmp.add((i, j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                q.append((nx, ny))
                tmp.add((nx, ny))
                visited[nx][ny] = 1
    
while True:
    is_chain = False
    visited = [[0] * 6 for _ in range(12)]
    
    for i in range(12):
        for j in range(6):
            # 색깔 필드를 찾을 경우 dfs를 통해 연쇄 대상을 찾는다.
            if graph[i][j] != '.':
                tmp = set()
                bfs(i, j)
                if len(tmp) >= 4:
                    is_chain = True
                    delete_chain(tmp)
    
    if not is_chain:
        break
    
    downPuyo()
    chain_cnt += 1

print(chain_cnt)