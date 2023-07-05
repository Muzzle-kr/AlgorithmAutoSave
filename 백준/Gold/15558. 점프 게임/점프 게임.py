from collections import deque

n, k = map(int, input().split())
graph = [list(input().strip()) for _ in range(2)]
visited = [[0] * n for _ in range(2)]
    
def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = 1
    while q:
        map, order, cnt = q.popleft()
        
        if order + 1 >= n:
            return 1
        
        if order + k >= n:
            return 1
        
        # 한 칸 앞으로 가는 경우
        if order + 1 <= n and graph[map][order + 1] == '1':
            if order+1 > cnt and not visited[map][order+1]:
                visited[map][order + 1] = 1
                q.append((map, order + 1, cnt + 1))
        
        # 한 칸 뒤로 가는 경우
        if 0 <= order -1 <= n and graph[map][order - 1]  == '1' and order - 1 > cnt:
            if order-1 > cnt and not visited[map][order-1]:
                visited[map][order - 1] = 1
                q.append((map, order - 1, cnt + 1))
        
        # 맵을 옮기는 경우
        if order + k <= n and graph[not map][order + k] == '1':
            if order + k > cnt and not visited[not map][order + k]:
                visited[not map][order + k] = 1
                q.append((not map, order + k, cnt + 1))    
    return 0
print(bfs())