import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 


N = int(input())     
maps = []
maxHeight = 0
result = 0

def dfs(x, y):
    global copiedMaps
    cnt = 1
    nx = [0, 0, 1, -1]
    ny = [1, -1, 0, 0]
            
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        
        if 0 <= dx < N and 0 <= dy < N and copiedMaps[dx][dy] >= 0:
            copiedMaps[dx][dy] = -1
            cnt += dfs(dx, dy)
            
    return cnt
for i in range(N):
    a = list(map(int, input().split()))
    maxHeight = max(maxHeight, max(a))
    maps.append(a)

        
# for i in maps:
#     print(i)


for i in range(1, maxHeight + 1):
    global copiedMaps
    copiedMaps = [[maps[n][m] - i for m in range(N)] for n in range(N)]
    answer = 0
    # print(f'---------높이가{i}일때---------')
    # for i in copiedMaps:
    #     print(i)
        
    for i in range(N):
        for j in range(N):
            if copiedMaps[i][j] >= 0:
                copiedMaps[i][j] = -1
                answer += 1
                dfs(i, j)
            
    result = max(result, answer)  
print(result)