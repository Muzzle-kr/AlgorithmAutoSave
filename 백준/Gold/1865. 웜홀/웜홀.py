def bellman_ford(start):
    INF = int(1e9)
    dist = [INF] * (n + 1)
    dist[start] = 0
    
    for i in range(n):
        for j in range(len(edges)):
            cur, next_node, cost = edges[j]
            
            if dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                
                if i == n-1:
                    return True
    return False

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    if bellman_ford(1):
        print("YES")
    else:
        print("NO")