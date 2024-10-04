N = int(input())
network = [[] for _ in range(N+1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)

visited = [False] * (N + 1)
count = 0

def dfs(idx):
    global count
    visited[idx] = True
    count += 1
    
    for next in network[idx]:
        if not visited[next]:
            dfs(next)
            
dfs(1)
print(count-1)