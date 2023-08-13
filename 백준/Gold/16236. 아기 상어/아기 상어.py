from collections import deque

def bfs(sx, sy, initial_level, initial_feed, initial_time):       
    q = deque()
    q.append((sx, sy, initial_level, initial_feed, initial_time))
    visit = [[0] * N for _ in range(N)]
    visit[sx][sy] = 1
    
    feeds = []
    min_distance = int(1e9)
    
    while q:
        x, y, level, feed, time = q.popleft()
        
        if min_distance < time:
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and graph[nx][ny] <= level:
                visit[nx][ny] = 1
                
                # 먹이를 찾은 경우
                if graph[nx][ny] < level and graph[nx][ny] != 0:
                    if min_distance > time + 1:
                        feeds = [(nx, ny)]
                        min_distance = time + 1
                    elif min_distance == time + 1:
                        feeds.append((nx, ny))
                        
                elif graph[nx][ny] == level or graph[nx][ny] == 0:
                    q.append((nx, ny, level, feed, time + 1))
    
    if feeds:
        # 먹이가 여러개인 경우 가장 위쪽, 가장 왼쪽에 있는 먹이를 먹는다.
        if len(feeds) > 1:
            feeds.sort(key=lambda x: (x[0], x[1]))
        
        fx, fy = feeds[0]
        graph[fx][fy] = 9
        graph[sx][sy] = 0
        if feed + 1 == level:
            return bfs(fx, fy, level+1, 0, min_distance)
        else:
            return bfs(fx, fy, level, feed + 1, min_distance)
    else:
        if level == 2 and feed == 0:
            return 0
        else:
            return initial_time
            
        

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
sx, sy = 0, 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
    
for i in range(N):
    try:
        if graph[i].index(9) != -1:
            sx, sy = i, graph[i].index(9)
            break
    except:
        continue
    

print(bfs(sx, sy, 2, 0, 0))