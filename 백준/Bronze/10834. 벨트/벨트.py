M = int(input())

direction = 0
speed_ratio = 1

for _ in range(M):
    # c == 1: 꼬인형태, c == 0: 안 꼬인 형태
    a, b, c = map(int, input().split()) 
    
    speed_ratio *= b/a
    
    if c == 1:
        direction = 1 - direction

print(direction, int(speed_ratio))