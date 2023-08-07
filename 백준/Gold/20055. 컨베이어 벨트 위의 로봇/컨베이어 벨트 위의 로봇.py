from collections import deque

N, K = map(int, input().split())
conveyor = deque(list(map(int, input().split())))
robot = deque([0] * N)
ans = 0
    
    

while True:
    # 1단계
    conveyor.rotate(1)
    robot.rotate(1)
    
    # 끝에 도달한 로봇 내려주기
    robot[N-1] = 0
    
    # 2단계 로봇 이동
    for i in range(N-2, -1, -1):
        if robot[i+1] == 0 and robot[i] == 1 and conveyor[i+1] > 0:
            robot[i+1], robot[i] = robot[i], robot[i+1]
            conveyor[i+1] -= 1
            
        # 로봇이 내려가는 위치에 도달하면 로봇 내려주기
        robot[N-1] = 0

    # 3단계 로봇 올리기
    if conveyor[0] > 0 and robot[0] == 0:
        robot[0] = 1
        conveyor[0] -= 1
    
    ans += 1
    
    if conveyor.count(0) >= K:
        break
print(ans)