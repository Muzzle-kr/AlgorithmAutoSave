import sys
input = sys.stdin.readline

T = int(input())

def clockwise():
    for i in range(n // 2):
        x, y = i, i
        temp = graph[x][y]
        
        # 상단
        for j in range(i + n//2-i, n - i, n//2-i):
            y = j
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev  
            
        # 우측    
        for j in range(i + n//2-i, n - i, n//2-i):
            x = j
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
            
        # 하단
        for j in range(i + n//2-i, n - i, n//2-i):
            y = n - j - 1
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
            
        # 좌측
        for j in range(i + n//2-i, n - i, n//2-i):
            x = n - j - 1
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev



        
def counterclockwise():
    for i in range(n // 2):
        x, y = i, i
        temp = graph[x][y]
        # n-i ~ m-i까지
        
        # 좌측
        for j in range(i + n//2-i, n - i, n//2-i):
            x = j
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
        
        # 하단
        for j in range(i + n//2-i, n - i, n//2-i):
            y = j
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
        
        # 우측    
        for j in range(i + n//2-i, n - i, n//2-i):
            x = n - j - 1
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev
        
        # 상단
        for j in range(i + n//2-i, n - i, n//2-i):
            y = n - j - 1
            prev = graph[x][y]
            graph[x][y] = temp
            temp = prev 
for _ in range(T):
    n, d = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    r = abs(d // 45)
    rotation = 1 if d > 0 else -1
    
    for _ in range(r):
        # 시계 방향
        
        if rotation == 1:
            clockwise()
        # 반시계 방향
        else:
            counterclockwise()
    
    for i in range(n):
        print(*graph[i])
        
            
