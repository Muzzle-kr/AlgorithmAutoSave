import math

a, board = map(int, input().split())
answer = 0
puddles = []
for _ in range(a):
    puddles.append(list(map(int, input().split())))
    

puddles.sort()

lastIdx = 0

for start, end in puddles:
    
    if lastIdx >= start:
        start = lastIdx + 1
        
    need = math.ceil((end - start) / board)
    # print(f'need: {need}, start: {start}, end: {end}, lastIdx: {lastIdx}')
    answer += need
    remainder = (need * board) - (end - start)
    if remainder > 0:
        lastIdx = end - 1 + remainder
    else:
        lastIdx = end - 1

print(answer)