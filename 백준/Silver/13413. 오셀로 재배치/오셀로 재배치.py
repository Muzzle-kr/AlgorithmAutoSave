for _ in range(int(input())):
    N = int(input())
    initial = list(input())
    target = list(input())
    
    b_cnt = 0
    w_cnt = 0
    
    for i in range(N):
        if initial[i] != target[i]:
            if initial[i] == 'B':
                b_cnt += 1
            else:
                w_cnt += 1
    ans = 0
    work_one = min(b_cnt, w_cnt)
    
    ans += work_one
    b_cnt -= work_one
    w_cnt -= work_one
    
    ans += b_cnt + w_cnt
    
    print(ans)