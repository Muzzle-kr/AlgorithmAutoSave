import sys
from collections import deque

INF = int(10e9)
input = sys.stdin.readline
minimum = INF
leastPerson = 0
friends, relations = map(int, input().split())
relationList = [[] for _ in range(friends + 1)]

for i in range(1, relations+1):
    a, b = map(int, input().split())

    relationList[a].append(b)
    relationList[b].append(a)

def bfs(graph, start):
    num = [0] * (friends + 1)
    chk[start] = 1
    
    q = deque()
    q.append(start)
    
    while (q):
        a = q.popleft()
        for i in graph[a]:
            if chk[i] == 0:
                num[i] = num[a] + 1
                q.append(i)
                chk[i] = 1
    return sum(num)

result = []

# 자기가 아닌 다른 숫자로 가는 최소 숫자 (BFS 이용)
for personToStart in range(1, friends + 1):
    chk = [0 for i in range(friends + 1)]   
    result.append(bfs(relationList, personToStart))
    

print(result.index(min(result)) + 1)