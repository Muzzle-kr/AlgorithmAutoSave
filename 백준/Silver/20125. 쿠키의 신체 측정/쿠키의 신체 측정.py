import sys
input = sys.stdin.readline

def get_left_arm():
    global left_arm
    x, y = heart
    
    while 0 < y < N - 1:
        y -= 1
        if graph[x][y] == '*':
            left_arm += 1
        else:
            break
    
def get_right_arm():
    global right_arm

    x, y = heart

    while 0 < y < N - 1:
        y += 1
        if graph[x][y] == '*':
            right_arm += 1
        else:
            break

def get_waist():
    global waist

    x, y = heart

    while 0 < x < N - 1:
        x += 1
        if graph[x][y] == '*':
            waist += 1
        else:
            break

def get_left_leg():
    global left_leg
    x, y = heart
    x += waist
    y -= 1
    
    while 0 < x < N - 1:
        x += 1
        if graph[x][y] == '*':
            left_leg += 1
        else:
            break

def get_right_leg():
    global right_leg
    x, y = heart
    x += waist
    y += 1
    
    while 0 < x < N - 1:
        x += 1
        if graph[x][y] == '*':
            right_leg += 1
        else:
            break
        

def printAll():
    print(heart[0] + 1, heart[1] + 1)
    print(left_arm, right_arm, waist, left_leg, right_leg)

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
heart = [0, 0]
waist, left_leg, right_leg, left_arm, right_arm = 0, 0, 0, 0, 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == '*':
            
            # 머리에서 x + 1이 심장
            heart = [i+1, j]
            
            # 팔 길이 찾기
            get_left_arm()
            get_right_arm()
            
            # 허리 길이 찾기
            get_waist()
            
            # 다리 길이 찾기
            get_left_leg()
            get_right_leg()
            
            printAll()
            exit()