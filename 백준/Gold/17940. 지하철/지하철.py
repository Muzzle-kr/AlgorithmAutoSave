import sys, collections, heapq as hq

# bfs : 시작점 0에서 출발하여 끝점 m까지 도달하는데 필요한 최소 환승 수를 리턴하는 함수
def bfs():
    q = collections.deque()
    visit = [-1] * n
    q.append(0)
    visit[0] = 0
    while q:
        now  = q.popleft()
        
        for (next, next_dist) in adj1[now]:
            if visit[next] == -1:
                # 만약 회사가 달라 환승이 필요하면 맨 마지막에 넣는다
                if arr[next] != arr[now]:
                    visit[next] = visit[now] + 1
                    q.append(next)
                # 만약 회사가 같아서 환승이 필요없다면 맨 처음에 넣는다
                else:
                    visit[next] = visit[now]
                    q.appendleft(next)
    return visit[m]

# dijkstra : 특정 환승 횟수인 num이하인 경로 중 끝점 m에 대한 최단거리를 리턴하는 함수
def dijkstra(num):
    INF = int(1e9)
    
    # d : 현재 idx번째 정점이고 현재까지 환승 수가 cnt일 때 최단거리를 저장하는 2차원 상태 배열
    d = [[INF] * (num + 1) for _ in range(n)]
    d[0][0] = 0
    q = []
    
    # (현재 거리, 현재 환승 수, 현재 정점)
    hq.heappush(q, (0, 0, 0))
    
    while q:
        cur_dist, cur_cnt, cur = hq.heappop(q)
        
        if d[cur][cur_cnt] < cur_dist:
            continue
        
        for next, next_dist in adj2[cur]:
            
            if arr[next] != arr[cur]:
                if cur_cnt + 1 <= num:
                    if d[next][cur_cnt + 1] > cur_dist + next_dist:
                        d[next][cur_cnt + 1] = cur_dist + next_dist
                        hq.heappush(q, (cur_dist + next_dist, cur_cnt + 1, next))
            else:
                if d[next][cur_cnt] > cur_dist + next_dist:
                    d[next][cur_cnt] = cur_dist + next_dist
                    hq.heappush(q, (cur_dist + next_dist, cur_cnt, next))
    return d[m][num]

# 입력부
n, m = map(int, sys.stdin.readline().split())
arr = [0] * n
for i in range(n):
    arr[i] = int(sys.stdin.readline())
temp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# adj1 : 0-1 BFS 인접리스트
adj1 = [[] for _ in range(n)]
# adj2 : 다익스트라 인접리스트
adj2 = [[] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if temp[i][j]:
            adj2[i].append((j, temp[i][j]))
            adj2[j].append((i, temp[i][j]))
            
            if arr[i] != arr[j]:
                adj1[i].append((j, 1))
                adj1[j].append((i, 1))
            else:
                adj1[i].append((j, 0))
                adj1[j].append((i, 0))
                
# 정답 출력
val = bfs()
res = dijkstra(val)
print(val, res)