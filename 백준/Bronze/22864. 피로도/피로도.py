pirodo, work, downPirodo, limit = map(int, input().split())

hour = 24
currentState = 0
totalWork = 0
for i in range(hour):
    # 현재 피로도 (음수) 초기화
    if currentState < 0:
        currentState = 0
        
    if currentState + pirodo > limit:
        currentState -= downPirodo
    else: 
        currentState += pirodo 
        totalWork += work
    # 한 시간 지남
    hour += 1
    
print(totalWork)
