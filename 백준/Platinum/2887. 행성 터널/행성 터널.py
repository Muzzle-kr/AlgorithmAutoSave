def get_cost(a, b):
    return min([abs(a[i]-b[i]) for i in range(3)])

def get_parent(parents, x):
    if parents[x] == x:
        return x
    return get_parent(parents, parents[x])

def find_parent(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    if a == b:
        return True
    else:
        return False

def union_parent(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
        
n = int(input())
costs = [[] for _ in range(n)]
x_list, y_list, z_list = [], [], []
edges = []

for i in range(n):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))

x_list.sort(); y_list.sort(); z_list.sort()

for cur_list in (x_list, y_list, z_list):
    for i in range(1, n):
        w1, a = cur_list[i-1]
        w2, b = cur_list[i]
        
        edges.append((abs(w1-w2), a, b))
        
edges.sort(reverse=True)
parents = [i for i in range(n)]
cnt = n-1
ans = 0

while cnt:
    w, a, b = edges.pop()
    
    if not find_parent(parents, a, b):
        union_parent(parents, a, b)
        ans += w
        cnt -= 1

print(ans)