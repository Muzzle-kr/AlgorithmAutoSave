
def bellman_fod(start):
    distance[start] = 0
    
    # 모든 간선 확인
    for i in range(1, n+1):
        for j in range(m):
            now, next, dist = edges[j]
            
            if distance[now] != INF and distance[next] > distance[now] + dist:
                distance[next] = distance[now] + dist
                
                if i == n:
                    return True
    return False

    
n, m = map(int, input().split())
edges = []
INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    
result = bellman_fod(1)

# 무한대 값이면 -1로 바꿔줌
distance = [-1 if d == INF else d for d in distance]

# 음수 순환 발생 시
if result:
    print(-1) 
else:
    for d in distance[2:]:
        print(d)