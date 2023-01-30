import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
cities = [INF] * (n + 1)
edges = []


def bf(start):
    cities[start] = 0
    
    for i in range(n):
        for j in range(m):
            cur, next, cost = edges[j]
            

            if cities[cur] != INF and cities[next] > cities[cur] + cost:
                cities[next] = cities[cur] + cost
                
                if i == n - 1:
                    return True
    return False


for i in range(m):
    a, b, c = map(int, input().split())
    
    edges.append((a, b, c))
    
    # 벨만 포드 알고리즘 수행
negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    for i in range(2, n + 1):
        if cities[i] == INF:
            print('-1')
        else:    
            print(cities[i])