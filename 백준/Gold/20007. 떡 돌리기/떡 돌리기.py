import heapq as hq

def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    
    while q:
        # day: 현재 날짜, cur_dist: 현재까지의 거리, checked: 왕복 여부, now: 현재 위치
        cur_dist, now = hq.heappop(q)
        
        for next_dist, next in edges[now]:
            if next_dist + cur_dist < dist[next]:
                dist[next] = next_dist + cur_dist
                hq.heappush(q, (dist[next], next))
    return dist
N, M, X, Y = map(int, input().split())
edges = [[] for i in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

result = dijkstra(Y)

# 왕복 거리가 X를 초과하면 -1 출력
for i in range(N):
    if result[i] > X // 2:
        print(-1)
        exit()

# 가까운 순으로 방문하기 위해 정렬
result.sort()
move_dist = 0 # 이동 거리
days = 1 # 방문일수

for i in range(N):
    if (move_dist + result[i]) * 2 <= X: 
        move_dist += result[i]
    else:
        days += 1
        move_dist = result[i]
print(days)