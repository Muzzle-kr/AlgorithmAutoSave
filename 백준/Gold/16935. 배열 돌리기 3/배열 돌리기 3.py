import sys

def reversal_top_bottom():
    global graph
    graph = graph[::-1]

def reversal_left_right():
    global graph
    graph = [i[::-1] for i in graph]

def rotation_left():
    global graph
    graph = list(zip(*graph))[::-1]

def rotation_right():
    global graph
    graph = list(zip(*graph[::-1]))

def move_group():
    # 1 -> 2 -> 3 -> 4 -> 1로 이동
    new_graph = [[0]*M for _ in range(N)]
    
    # 1 -> 2번 그룹 옮기기
    for i in range(N//2):
        for j in range(M//2):
            new_graph[i][j+M//2] = graph[i][j]
    
    # 2 -> 3번 그룹 옮기기
    for i in range(N//2):
        for j in range(M//2,M):
            new_graph[i+N//2][j] = graph[i][j]
            
    # 3 -> 4번 그룹 옮기기
    for i in range(N//2, N):
        for j in range(M//2, M):
            new_graph[i][j-M//2] = graph[i][j]
            
    # 4 -> 1번 그룹 옮기기
    for i in range(N//2, N):
        for j in range(M//2):
            new_graph[i-N//2][j] = graph[i][j]
    
    return new_graph
            
    

def move_group2():
    # 1 -> 4, 4 -> 3, 3 -> 2, 2 -> 1로 이동
    
    new_graph = [[0]*M for _ in range(N)]
    
    # 1 -> 4번 그룹 옮기기
    for i in range(N//2):
        for j in range(M//2):
            new_graph[i+N//2][j] = graph[i][j]
    
    # 4 -> 3번 그룹 옮기기
    for i in range(N//2, N):
        for j in range(M//2):
            new_graph[i][j+M//2] = graph[i][j]
            
    # 3 -> 2번 그룹 옮기기
    for i in range(N//2, N):
        for j in range(M//2, M):
            new_graph[i-N//2][j] = graph[i][j]
            
    # 2 -> 1번 그룹 옮기기
    for i in range(N//2):
        for j in range(M//2, M):
            new_graph[i][j-M//2] = graph[i][j]
    
    return new_graph

input = sys.stdin.readline

N, M, R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
A = list(map(int, input().split()))

for a in A:
    N, M = len(graph), len(graph[0])
    if a == 1:
        reversal_top_bottom()
    elif a == 2:
        reversal_left_right()
    elif a == 3:
        rotation_right()
    elif a == 4:
        rotation_left()
    elif a == 5:
        graph = move_group()
    elif a == 6:
        graph = move_group2()
    
for i in graph:
    print(*i)