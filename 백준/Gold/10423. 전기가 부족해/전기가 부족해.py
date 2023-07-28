import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
power_stations = list(map(int, input().split()))
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()
parents = [i for i in range(N+1)]

# 발전소는 부모를 0으로 만들어줌
for ps in power_stations:
    parents[ps] = 0

def find_parent(parents, x):
    if parents[x] == x:
        return x
    return find_parent(parents, parents[x])
        
def union_parents(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

ans = 0

for weight, a, b in edges:
    if find_parent(parents, a) != find_parent(parents, b):
        union_parents(parents, a, b)
        ans += weight

print(ans)