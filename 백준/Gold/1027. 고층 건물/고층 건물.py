def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

N = int(input())
buildings = list(map(int, input().split()))
result = 0

for idx1, y1 in enumerate(buildings):
    x1 = idx1 + 1
    
    cur_slope_right = None
    slope_right_cnt = 0
    
    # 우측 빌딩 체크
    for idx2 in range(idx1+1, N+1):
        if idx2 == N:
            break
        
        x2 = idx2 + 1
        y2 = buildings[idx2]
        slope_right = slope(x1, y1, x2, y2)
        
        if cur_slope_right is None or cur_slope_right < slope_right:
            cur_slope_right = slope_right
            slope_right_cnt += 1
    
    cur_slope_left = None
    slope_left_cnt = 0
    
    # 좌측 빌딩 체크
    for idx3 in range(idx1-1, -1, -1):
        if idx3 == -1:
            break
        
        x2 = idx3 + 1
        y2 = buildings[idx3]
        slope_left = slope(x1, y1, x2, y2)
        
        if cur_slope_left is None or cur_slope_left > slope_left:
            cur_slope_left = slope_left
            slope_left_cnt += 1
    
    if (result < slope_left_cnt + slope_right_cnt): result = slope_left_cnt + slope_right_cnt
    
print(result)