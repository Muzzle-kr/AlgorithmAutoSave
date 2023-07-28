N, M = map(int, input().split())
big = [[] for _ in range(N+1)]
small = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    big[a].append(b)
    small[b].append(a)
    
# 자신보다 큰  아이보다 큰 아이를 다 찾아서 넣기
for i in range(1, N+1):
    for b in big[i]:
        for bb in big[b]:
            if bb not in big[i]:
                big[i].append(bb)
    
# 자신보다 작은 아이보다 작은 아이를 다 찾아서 넣기
for i in range(1, N+1):
    for s in small[i]:
        for ss in small[s]:
            if ss not in small[i]:
                small[i].append(ss)

ans = 0
for i in range(1, N+1):
    cnt = 0
    cnt += len(big[i])
    cnt += len(small[i])
    
    if cnt == N-1:
        ans += 1
print(ans)

        