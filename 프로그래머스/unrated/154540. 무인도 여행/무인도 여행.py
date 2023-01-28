import sys
sys.setrecursionlimit(10**5)

def solution(maps):
    global totalSum
    answer = []
    maps = [list(map) for map in maps]
    totalSum = 0
    
    # 못가는 곳인지 체크
    def checkValid(a, b):
        return a >= 0 and a < len(maps) and b >= 0 and b < len(maps[0]) and maps[a][b] != "X"
    
    
    def dfs(a, b):
        global totalSum
        maps[a][b] = 'X'
        
        nx = [0, 0, 1, -1]
        ny = [1, -1, 0, 0]
        
        for i in range(4):
            mx = b + nx[i]
            my = a + ny[i]
            
            if checkValid(my, mx):
                totalSum += int(maps[my][mx])
                dfs(my, mx)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            
            if checkValid(i, j):
                # print(f'섬의 시작점 {i}, {j}')
                totalSum = int(maps[i][j])
                dfs(i, j)
                
                if totalSum != 0:
                    answer.append(totalSum)
                    
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)