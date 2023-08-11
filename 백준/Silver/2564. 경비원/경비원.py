W, H = map(int, input().split())
N = int(input())
stores_address = [list(map(int, input().split())) for _ in range(N)]
ex, ey = map(int, input().split())

# 북서쪽, 남서쪽, 북동쪽, 남동쪽
nl, sl, nr, sr = 0, 0, 0, 0
    
if ex == 1:
    nl = ey
    sl = ey + H
    nr = W - ey
    sr = W - ey + H
elif ex == 2:
    nl = ey + H
    sl = ey
    nr = W - ey + H
    sr = W - ey
elif ex == 3:
    nl = ey
    sl = H - ey
    nr = ey + W
    sr = H - ey + W
else:
    nl = ey + W
    sl = H - ey + W
    nr = ey
    sr = H - ey

total = 0

for sx, sy in stores_address:
    min_distance = int(1e9)    
    
    # 같을 땐 거리만 체크
    if sx == ex:
        min_distance = abs(sy - ey)
    # 1번 (북쪽)
    elif sx == 1:
        min_distance = min(min_distance, nl + sy, nr + W - sy)
    
    # 2번 (남쪽)
    elif sx == 2:
        min_distance = min(min_distance, sl + sy, sr + W - sy)
        
    # 3번 (서쪽)
    elif sx == 3:
        min_distance = min(min_distance, nl + sy, sl + H - sy)
        
    # 4번 (동쪽)
    else:
        min_distance = min(min_distance, nr + sy, sr + H - sy)
    
    total += min_distance
    
print(total)