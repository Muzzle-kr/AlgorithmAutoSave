import sys
from collections import deque
input = sys.stdin.readline
n = int(input()) # 간선의 개수
tree = [[] for _ in range(n + 1)]
# visit = [0] * (n+1)
farthest = [0, 0] # 가장 먼 노드값, 가중치
diameter = 0

# 리프노드에서 루프노드로 갔을 때 max값보다 낮은 노드는 통과 X 시키기
for i in range(n-1):
    a, b, weight = map(int, input().split()) 
    tree[a].append((b, weight))
    tree[b].append((a, weight))


def bfs(i):
    q = deque()
    q.append((i, 0, [i]))
    
    while q:
        node, total, visit = q.popleft()
        
        # print(f'node: {node}, total: {total}, visit: {visit}')
        # print(node, total)
        if total > farthest[1]:
            farthest[0] = node
            farthest[1] = total
        
            # print("여기 들옴")
        for (j, weight) in tree[node]:
            if j not in visit:
                visit.append(j)
                q.append((j, total + weight, visit))
                

# def secondBfs(i):
#     q = deque()
#     q.append((i, 0))
#     maxDistance = 0
    
#     while q:
#         node, total, visit = q.popleft()
        
#         for (j, weight) in tree[node]:
#             if j not in visit:
#                 visit.append(j)
#                 q.append((j, total + weight, visit))
    
bfs(1)
bfs(farthest[0])
# result = secondBfs(farthestNode)
print(farthest[1])
    

            
    