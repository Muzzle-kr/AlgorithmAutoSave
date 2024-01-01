import heapq as hq
N, M = map(int, input().split())
level = list(map(int, input().split()))
P = int(input())
tips = [[] for _ in range(N)]

for _ in range(P):
    a, b, t = map(int, input().split())
    # Tip에 저장해두기
    tips[a-1].append((b-1, t))
    # 난이도 올리기
    level[b-1] += t
    
monster = []

for i in range(N):
    hq.heappush(monster, (level[i], i))

cnt = 0
ans = 0
die_monster = [False] * N

while cnt < M:
    lev, idx = hq.heappop(monster)
    
    # 이미 잡은 몬스터면 건너뛰기
    if die_monster[idx]:
        continue
    
    # 몬스터 잡기
    die_monster[idx] = True
    
    # 레벨 최신화
    if ans < lev:
        ans = lev
    
    # 레벨 낮추기
    for b, t in tips[idx]:
        # 죽지 않은 몬스터만 하향시키기
        if not die_monster[b]:
            level[b] -= t
            hq.heappush(monster, (level[b], b))
            
    cnt += 1

print(ans)