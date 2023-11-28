n, m = map(int, input().split())
number = int(input())
arr = [[0] * m for _ in range(n)]

# 우 하 좌 상
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d = 0
cur_num = 1
x, y = 0, 0
arr[x][y] = cur_num

if number > n * m:
    print(0)
    exit()
    

while cur_num <= n * m:
    if cur_num == number:
        print(x + 1, y + 1)
        break
        
    dx, dy = direction[d]
    nx, ny = x + dx, y + dy    
    
    if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
        arr[nx][ny] = cur_num
        cur_num += 1
        x, y = nx, ny
    else:
        d = (d + 1) % 4