import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, v = map(int, input().split())
visit = [0] * (n+1)
result = [0] * (n+1)
graph = [[] for _ in range(n+1)]
dfsAnswer = []
cnt = 1
def dfs(v):
    global cnt
    # print(f'v: {v}')
    visit[v] = cnt
    dfsAnswer.append(v)
    
    for i in graph[v]:
        if visit[i] == 0 and len(graph[i]) > 0:
            cnt += 1
            dfs(i)
    


for i in range(m):  
    x, y = map(int, input().split()) 
    graph[x].append(y)
    graph[y].append(x)


for i in range(1, n + 1):
        graph[i].sort()



dfs(v)
# visit[v] = v

# for i in graph[v]:
#     if visit[i] == 0:
#         visit[i] = i
#         dfs(i)

# print(f'visit: {visit}')

for i in range(1, n + 1):
    result[i] = visit[i]
for i in range(1, n + 1):  
    if visit[i] == 0:
        dfsAnswer.append(0)
    # print(visit[i])

for i in range(1, n + 1):
    print(visit[i])
# print(*dfsAnswer)