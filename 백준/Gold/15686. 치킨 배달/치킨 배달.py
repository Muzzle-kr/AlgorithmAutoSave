from itertools import combinations 
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            chickens.append([i, j])
            
        if maps[i][j] == 1:
            houses.append([i, j])
            
chicken_combinations = list(combinations(chickens, M))
answer = float('inf')

for combination in chicken_combinations:    
    total = 0
    
    for x, y in houses:
        min_chicken_distance = 99999999
        
        for cx, cy in combination:
            chicken_distance = abs(cx-x) + abs(cy-y)
            min_chicken_distance = min(min_chicken_distance, chicken_distance)
        total += min_chicken_distance
    answer = min(answer, total)

print(answer)