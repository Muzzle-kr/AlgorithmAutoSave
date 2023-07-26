import sys
input = sys.stdin.readline

def get_parent(parents, x):
    if parents[x] == x:
        return x
    return get_parent(parents, parents[x])

def find_parent(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    
    return a == b

def union_parent(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    
    if a > b:
        parents[a] = b
    else:
        parents[b] = a
        
n = int(input())
edges = []
for i in range(n):
    edges.append((int(input()), 0, i+1))

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        edges.append((arr[i][j], i+1, j+1))

parents = [i for i in range(n+1)]
edges.sort()

cnt = 0
result = 0

for edge in edges:
    cost, a, b = edge
    
    if not find_parent(parents, a, b):
        union_parent(parents, a, b)
        result += cost
        cnt += 1
    
    if cnt == n:
        break

print(result)