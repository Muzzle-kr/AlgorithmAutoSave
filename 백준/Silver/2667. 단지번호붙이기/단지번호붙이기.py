import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) 


def dfs(x, y):
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < size and 0 <= ny < size:
            if check[nx][ny] == 0 and apartments[nx][ny] == 1:
                check[nx][ny] = numberOfComplex
                cnt += dfs(nx, ny)
    return cnt


apartments = []
size = int(input())
check = [[0]* size for _ in range(size)]
numberOfComplex = 0
answer = []
for i in range(size):
    apartments.append(list(map(int, list(input()[:-1]))))


for i in range(size):
    for j in range(size):
        if check[i][j] == 0 and apartments[i][j] == 1:
            # 단지 수 증가
            numberOfComplex += 1
            
            count = dfs(i, j)
            if count == 1:
                answer.append(count)    
            else:
                answer.append(count-1)
            
          
answer.sort()  

print(numberOfComplex)
# print(answer)
for i in answer:
    print(i)