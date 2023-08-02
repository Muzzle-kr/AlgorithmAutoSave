import sys
input = sys.stdin.readline

def counter_clock_wise():
    global graph
    for i in range(min(N, M) // 2):
        x, y = i, i
        temp = graph[x][y]
        
        # 좌
        for j in range(i + 1, N - i):
            x = j
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
            
        # 하
        for j in range(i + 1, M - i):
            y = j
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
        # 우
        for j in range(i + 1, N - i):
            x = N - j - 1
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
    
        # 상
        for j in range(i + 1, M - i):
            y = M - j - 1
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
        
N, M, R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

arr = [[] for _ in range(min(N, M)//2)]

for i in range(min(N, M)//2):
    x, y = i, i
    
    # 상단
    for j in range(i, M-i):
        y = j
        
        arr[i].append(graph[x][y])
    
    # 우측
    for j in range(i+1, N-i):
        x = j
        arr[i].append(graph[x][y])
    
    # 하단
    for j in range(i+1, M-i):
        y = M-j-1
        arr[i].append(graph[x][y])        
    # 좌측
    for j in range(i+1, N-i-1):
        x = N-j-1
        arr[i].append(graph[x][y])


for i in range(len(arr)):
    r = R % len(arr[i])
    arr[i] = arr[i][r:] + arr[i][:r]

for i in range(min(N, M)//2):
    x, y = i, i
    
    # 상단
    for j in range(i, M-i):
        y = j
        graph[x][y] = arr[i].pop(0)
    
    # 우측
    for j in range(i+1, N-i):
        x = j
        graph[x][y] = arr[i].pop(0)
    
    # 하단
    for j in range(i+1, M-i):
        y = M-j-1
        arr[i].append(graph[x][y])        
        graph[x][y] = arr[i].pop(0)
    # 좌측
    for j in range(i+1, N-i-1):
        x = N-j-1
        arr[i].append(graph[x][y])
        graph[x][y] = arr[i].pop(0)

for g in graph:
    print(*g)