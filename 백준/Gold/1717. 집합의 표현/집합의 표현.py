import sys
sys.setrecursionlimit(10**9)

order = []
N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(M):
    opr, a, b = map(int, input().split())
    
    if opr == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')