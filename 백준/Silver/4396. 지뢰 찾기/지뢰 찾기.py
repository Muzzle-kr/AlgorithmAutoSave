n = int(input())

mine_map = [list(input().strip()) for _ in range(n)]
result_map = [list(input().strip()) for _ in range(n)]
final_map = [['.'] * n for _ in range(n)]
mine_arr = []
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, -1, 1, 0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if mine_map[i][j] == "*":
            mine_arr.append((i,j))
            
def count_mine(x, y):
    count = 0
    
    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if (nx, ny) in mine_arr:
            count += 1
            
    return count
            
isFind = False

for i in range(n):
    for j in range(n):
        # 이미 건너간
        if result_map[i][j] == "x":
            if mine_map[i][j] != "*":
                final_map[i][j] = count_mine(i,j)
            else:
                isFind = True

if isFind:
    for mx, my in mine_arr:
        final_map[mx][my] = "*"

for i in range(n):
    for j in range(n):
        print(final_map[i][j], end="")
    print()