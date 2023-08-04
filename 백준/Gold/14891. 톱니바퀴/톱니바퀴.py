import sys
from collections import deque
input = sys.stdin.readline
saw_tooth = [deque(list(input().rstrip())) for _ in range(4)]
    
K = int(input())
rotate = []

for _ in range(K):
    n, d = map(int, input().split())
    n -= 1
    
    tmp_saw_tooth = []
    
    for i in range(4):
        tmp_saw_tooth.append((saw_tooth[i][2], saw_tooth[i][6]))
    
    # 시계 방향
    if d == 1:
        # 방향
        cd = -1
        
        # 우측 전파
        for i in range(n+1, 4):
            # 2번과 6번 비교
            if tmp_saw_tooth[i-1][0] != tmp_saw_tooth[i][1]:
                saw_tooth[i].rotate(cd)
                cd *= -1
            else:
                break
        
        cd = -1
        # 좌측 방향
        for i in range(n-1, -1, -1):
            # 2번과 6번 비교
            if tmp_saw_tooth[i+1][1] != tmp_saw_tooth[i][0]:
                saw_tooth[i].rotate(cd)
                cd *= -1
            else:
                break
        
        saw_tooth[n].rotate(d)
    
    # 반시계 방향
    else:
        cd = 1
        
        # 우측 전파
        for i in range(n+1, 4):
            # 2번과 6번 비교
            if tmp_saw_tooth[i-1][0] != tmp_saw_tooth[i][1]:
                saw_tooth[i].rotate(cd)
                cd *= -1
            else:
                break
        
        cd = 1
        # 좌측 전파
        for i in range(n-1, -1, -1):
            # 2번과 6번 비교
            if tmp_saw_tooth[i+1][1] != tmp_saw_tooth[i][0]:
                saw_tooth[i].rotate(cd)
                cd *= -1
            else:
                break
        
        saw_tooth[n].rotate(d)
    
ans = 0

for i in range(4):
    ans += 2 ** i if saw_tooth[i][0] == '1' else 0

print(ans)