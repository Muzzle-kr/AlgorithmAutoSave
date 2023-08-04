from collections import deque

def get_score(x, y):
    likes = likes_dict[graph[x][y]]
    cnt = 0
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] in likes:
                cnt += 1
                
    return cnt

def find_like_spaces(f, likes):
    max_total = -1
    arr = []
    
    for x, y in empty:
        cnt = 0
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] in likes:
                    cnt += 1
        
        if cnt > max_total:
            arr = [(x, y)]
            max_total = cnt
        elif cnt == max_total:
            arr.append((x, y))
    return arr

def find_empty_spaces(spaces):
    max_total = -1
    arr = []
    
    for x, y in spaces:
        cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    cnt += 1
        if cnt > max_total:
            arr = [(x, y)]
            max_total = cnt
        elif cnt == max_total:
            arr.append((x, y))
            
    return arr
            
N = int(input())

likes_dict = {}
graph = [[0] * N for _ in range(N)]
friends = [list(map(int, input().split())) for _ in range(N**2)]
empty = []

# 좋아하는 친구 dict 생성
for i in range(N**2):
    likes_dict[friends[i][0]] = friends[i][1:]

# 빈 자리 만들어놓기
for i in range(N):
    for j in range(N):
        empty.append((i, j))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N**2):
    f = friends[i][0]
    
    # 1. 좋아하는 학생이 인접한 칸에 가장 많은 칸
    like_spaces = find_like_spaces(f, friends[i][1:])
    
    if len(like_spaces) == 1:
        graph[like_spaces[0][0]][like_spaces[0][1]] = f
        
        # 빈 자리에서 삭제
        empty.remove(like_spaces[0])
        continue
    
    # 2. 빈 자리 찾기
    empty_spaces = find_empty_spaces(like_spaces)
    
    # 빈 자리가 유일하면 자리 앉히기
    if len(empty_spaces) == 1:
        graph[empty_spaces[0][0]][empty_spaces[0][1]] = f
        
        # 빈 자리에서 삭제
        empty.remove(empty_spaces[0])
        continue
    
    # 3. 행 또는 열의 번호가 가장 작은 칸
    space = sorted(empty_spaces, key=lambda x: (x[0], x[1]))[0]
    graph[space[0]][space[1]] = f
    empty.remove(space)

score = [0, 1, 10, 100, 1000]
ans = 0

for i in range(N):
    for j in range(N):
        ans += score[get_score(i, j)]
print(ans)