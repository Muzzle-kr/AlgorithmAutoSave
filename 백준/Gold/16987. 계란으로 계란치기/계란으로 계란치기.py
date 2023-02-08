import sys
input = sys.stdin.readline
n = int(input())
eggs = []
answer = 0
S, W = 0, 1

for i in range(n):
    eggs.append(list(map(int, input().split())))
    
# 2번째부터 내구도 순 정렬
# eggs = [eggs[0]] + sorted(eggs[1:], key=lambda x: x[S])

def crash(nowIndex):
    global answer
    if nowIndex == n:
        
        # print(f'종료 조건 시 계란 상황::: {eggs}')
        breakEggs = 0
        
        for i in range(n):
            if eggs[i][S] <= 0:
                breakEggs += 1                   
        answer = max(answer, breakEggs)
        return
    
    
    # 자기가 깨져있는 경우
    if eggs[nowIndex][S] <= 0:
        crash(nowIndex + 1)
        return
    
    # 자기말고 다 깨져있는 상황인 경우
    isAllBroken = True
    
    for targetIndex in range(n):
        if targetIndex == nowIndex: continue
        if eggs[targetIndex][S] > 0:
            isAllBroken = False
            break
        
    if isAllBroken:
        # print(f'자기말고 다 깨진 상황: {eggs}')
        answer = max(answer, n - 1)
        return
    
    
    for targetIndex in range(n):
        if targetIndex == nowIndex: continue
        if eggs[targetIndex][S] <= 0: continue
        
        # 내구도 - 무게로 때리기
        eggs[nowIndex][S] -= eggs[targetIndex][W]
        eggs[targetIndex][S] -= eggs[nowIndex][W]
        
        crash(nowIndex + 1)
        
        # 내구도 원상복구
        eggs[nowIndex][S] += eggs[targetIndex][W]
        eggs[targetIndex][S] += eggs[nowIndex][W]
        
# 무조건 0번 계란부터 시작
crash(0)
print(answer)