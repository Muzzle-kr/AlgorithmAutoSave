import heapq as hq


for _ in range(int(input())):
    n = int(input())
    arr = []
    idx = 0
    
    while idx < n:
        arr += list(map(int, input().split()))
        idx += 10
    
    q = []
    ans = []    
    for i in range(n):
        # 숫자 넣기
        hq.heappush(q, arr[i])
        
        # 홀수 번째면 중간값 출력
        if (i+1) % 2 == 1:
            last_val = 0
            tmp = []
            for _ in range(len(q) // 2 + 1):
                last_val = hq.heappop(q)
                tmp.append(last_val) # 마지막 값 저장
            
            # 다시 넣기
            for t in tmp:
                hq.heappush(q, t) 
                
            ans.append(last_val)
            
    print(len(ans))
    
    idx = 0
    
    while idx < len(ans):
        print(*ans[idx:idx+10])
        idx += 10