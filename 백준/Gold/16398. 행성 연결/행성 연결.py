import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

    
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)] # 부모를 자기 자신으로 초기화
edges = []
    
for a in range(n):
    for b in range(a+1, n):
        edges.append((graph[a][b], a, b))

edges.sort() # 간선을 비용 순으로 정렬

answer = 0

for cost, a, b in edges:
    
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost
        
print(answer)