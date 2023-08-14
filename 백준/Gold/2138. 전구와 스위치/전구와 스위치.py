import sys
input = sys.stdin.readline

def switch(bulbs, cnt):
    # 첫번째 스위치를 누른 경우
    if cnt == 1:
        bulbs[0] = 1 - bulbs[0]
        bulbs[1] = 1 - bulbs[1]
    
    # 전구 상태 확인
    for i in range(1, N):
        if bulbs[i-1] != after[i-1]:
            bulbs[i-1] = 1 - bulbs[i-1]
            bulbs[i] = 1 - bulbs[i]
            
            if i != N-1:
                bulbs[i+1] = 1 - bulbs[i+1]
                
            cnt += 1
    
    if bulbs == after:
        return cnt
    
    return -1
        

N = int(input())
now = list(map(int, input().rstrip()))
after = list(map(int, input().rstrip()))

res1 = switch(now[:], 0) # 첫번 째 스위치 안누른 경우
res2 = switch(now[:], 1) # 첫번 째 스위치 누른 경우

if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0:
    print(res1)
elif res2 >= 0:
    print(res2)
else:
    print(-1)