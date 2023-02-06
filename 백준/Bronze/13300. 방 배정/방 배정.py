import math

N, M = map(int, input().split())
arr = [[0] * 2 for i in range(6)]

count = 0

for i in range(N):
    s, y = map(int, input().split())
    
    # 1이 남자, 0이 여자
    
    if s == 1:
        arr[y-1][1] += 1
    else:
        arr[y-1][0] += 1
        

for i in range(6):
    for j in range(2):
        if arr[i][j] != 0:
            count += math.ceil(arr[i][j] / 2)
            
print(count)