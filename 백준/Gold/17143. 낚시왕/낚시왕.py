R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
seas = [[0] * (C) for _ in range(R)]
ans = 0
# 상어 바다에 배치
for r, c, s, d, z in sharks:
    r -= 1
    c -= 1
    seas[r][c] = [s, d, z]

# 상어 낚시
def fishing(j):
    for i in range(R):
        if seas[i][j]:
            size = seas[i][j][2]
            seas[i][j] = 0
            return size
    return 0

def get_new_location(i, j, speed, dir):
    
    if dir == 1 or dir == 2:
        cycle = R * 2 - 2
        if dir == 1:
            speed += 2 * (R - 1) - i
        else:
            speed += i

        speed %= cycle
        
        if speed >= R:
            return (cycle - speed, j, 1)
        return (speed, j, 2)

    else:  # j
        cycle = C * 2 - 2
        if dir == 4:
            speed += 2 * (C - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= C:
            return (i, cycle - speed, 4)
        return (i, speed, 3)
        
# 상어 이동
def move_shark():
    global seas
    new_seas = [[0] * (C) for _ in range(R)]
    
    for x in range(R):
        for y in range(C):
            if seas[x][y]:
                s, d, z = seas[x][y]
                nx, ny, nd = get_new_location(x, y, s, d)
                
                if new_seas[nx][ny]:
                    if new_seas[nx][ny][2] < z:
                        new_seas[nx][ny] = [s, nd, z]
                else:
                    new_seas[nx][ny] = [s, nd, z]    
    seas = new_seas
    
for j in range(C):
    # 낚시왕 이동 후 낚시
    ans += fishing(j)
    move_shark()

print(ans)