from collections import deque

N = int(input())
aquarium = [list(map(int, input().split())) for _ in range(N)]

def find_shark():
    for i in range(N):
        for j in range(N):
            if aquarium[i][j] == 9:
                return i, j

sx, sy = find_shark()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(sx, sy, init_level, init_feed, init_time):
    q = deque()
    q.append((sx, sy, init_level, init_feed, init_time))
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    
    feeds = []
    min_distance = int(1e9)
    
    while q:
        x, y, level, feed, time = q.popleft()
        
        if min_distance < time:
            break
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and aquarium[nx][ny] <= level:
                visited[nx][ny] = True
                
                # 먹이를 찾은 경우
                if aquarium[nx][ny] < level and aquarium[nx][ny] != 0:
                    
                    if min_distance > time + 1:
                        feeds = [(nx, ny)]
                        min_distance = time + 1
                    elif min_distance == time + 1:
                        feeds.append((nx, ny))
                
                elif aquarium[nx][ny] == level or aquarium[nx][ny] == 0:
                    q.append((nx, ny, level, feed, time + 1))
                
    if feeds:
        
        # 먹이가 여러개라면 정렬해서 먹음
        if len(feeds) > 1:
            feeds.sort(key=lambda x : (x[0], x[1]))
        
        fx, fy = feeds[0]
        aquarium[fx][fy] = 9
        aquarium[sx][sy] = 0
        
        if feed + 1 == level:
            return bfs(fx, fy, level + 1, 0, min_distance)
        else:
            return bfs(fx, fy, level, feed + 1, min_distance)
    else:
        return init_time
            
print(bfs(sx, sy, 2, 0, 0))