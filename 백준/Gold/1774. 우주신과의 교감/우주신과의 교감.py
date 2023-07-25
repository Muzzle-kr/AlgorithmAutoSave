import sys
input = sys.stdin.readline

def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_parent(parent, x):
    if parent[x] == x:
        return x
    return get_parent(parent, parent[x])

def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    else:
        return False

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
edges = []
distance = []

for _ in range(N):
    edges.append(list(map(int, input().split())))
    
for _ in range(M):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = edges[i]
        x2, y2 = edges[j]        
        distance.append((get_distance(x1, y1, x2, y2), i+1, j+1))

distance.sort()
result = 0

for d in distance:
    cost, a, b = d
    
    if not find_parent(parent, a, b):
        union_parent(parent, a, b)
        result += cost

print('%.2f' % result)