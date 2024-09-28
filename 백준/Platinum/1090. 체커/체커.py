N = int(input())
positions = [list(map(int, input().split())) for _ in range(N)]
set_x = {x for x, _ in positions}
set_y = {y for _, y in positions}

# 최소 거리를 저장할 리스트 초기화
min_distances = [float('inf')] * N

# 좌표 값 x, y set에 넣어주기
for p in positions:
    x, y = p
    set_x.add(x)
    set_y.add(y)
    
for x in set_x:
    for y in set_y:
        distance = []
        
        for px, py in positions:
            distance.append(abs(px - x) + abs(py - y))

        distance.sort()
        
        cumulative_sum = 0  # 각 거리마다 최소 거리를 저장
        
        for dist in range(N):
            cumulative_sum += distance[dist]  # 각 좌표개수마다 거리를 더해준다.
            min_distances[dist] = min(min_distances[dist], cumulative_sum)  # 그값을 저장

print(*min_distances)