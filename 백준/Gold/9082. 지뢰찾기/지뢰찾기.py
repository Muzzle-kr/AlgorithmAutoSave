import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().rstrip()))
    mine = input().strip()
    mine_cnt = 0
    
    for i in range(N):
        if i == 0:
            if arr[0] != 0 and arr[1] != 0:
                arr[0] -= 1
                arr[1] -= 1
                mine_cnt += 1
            
        elif i == N-1:
            if arr[i] != 0 and arr[i-1] != -0:
                arr[i-1] -= 1
                arr[i] -= 1
                mine_cnt += 1
        
        else:
            if arr[i] != 0 and arr[i-1] != 0 and arr[i+1] != 0:
                arr[i-1] -= 1
                arr[i+1] -= 1
                arr[i] -= 1
                mine_cnt += 1
                
    print(mine_cnt)