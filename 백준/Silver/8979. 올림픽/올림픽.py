N, K = map(int, input().split())
medals = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (-x[1], -x[2], -x[3]))

grade = 0
duplicated = 0
pre_gold, pre_silver, pre_bronze = medals[0][1:]

for i in range(1, N):
    idx, gold, silver, bronze = medals[i]
    
    if pre_gold == gold and pre_silver == silver and pre_bronze == bronze:
        duplicated += 1
    else:
        grade += 1
        
    if idx == K:
        print(grade - duplicated)
        break