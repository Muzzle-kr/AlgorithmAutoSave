import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, v = map(int, input().split())
visit = [-1] * (n+1)
result = [0] * (n+1)
graph = [[] for _ in range(n+1)]
dfsAnswer = []
depth = 0
order = 1
answer = 0
def dfs(v):
    global depth
    global order
    global answer
    visit[v] = depth
    answer += (order * depth)
    dfsAnswer.append(v)
    
    for i in graph[v]:
        if visit[i] == -1 and len(graph[i]) > 0:
            depth += 1
            order += 1
            dfs(i)
            depth -= 1

for i in range(m):  
    x, y = map(int, input().split()) 
    graph[x].append(y)
    graph[y].append(x)


for i in range(1, n + 1):
        graph[i].sort(reverse=True)

dfs(v)
    
for i in range(1, n + 1):  
    if visit[i] == -1:
        dfsAnswer.append(-1)

print(answer)
