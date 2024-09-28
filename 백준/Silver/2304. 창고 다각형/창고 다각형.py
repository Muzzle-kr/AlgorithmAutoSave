N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

max_y = 0
max_idx = 0

for i in range(N):
    x, y = arr[i][0], arr[i][1]
    
    if y > max_y:
        max_y = y
        max_idx = i
    
answer = 0

# 왼쪽에서 시작
prev_x, prev_y = arr[0][0], arr[0][1]

for i in range(1, max_idx + 1):
    x, y = arr[i]

    # 높은 기둥을 찾으면 계산하고 이전 좌표를 업데이트한다.
    if y >= prev_y:
        answer += prev_y * abs(x - prev_x)
        prev_x, prev_y = x, y

# 오른쪽에서 시작
prev_x, prev_y = arr[-1][0], arr[-1][1]

for i in range(N-2, max_idx-1, -1):
    x, y = arr[i]

    # 높은 기둥을 찾으면 계산하고 이전 좌표를 업데이트한다.
    if y >= prev_y:
        answer += prev_y * abs(x - prev_x)
        prev_x, prev_y = x, y
    
print(answer + max_y)