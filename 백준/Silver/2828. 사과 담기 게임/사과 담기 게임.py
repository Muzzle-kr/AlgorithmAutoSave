n, m = map(int, input().split())
j = int(input())
cur_position = 1
arr = [int(input()) for _ in range(j)]
ans = 0
m -= 1 # 바구니 길이 보정

for i in arr:
    # print(f'사과의 위치: {i}, 현재위치: {cur_position}')
    # 현재위치 + 바구니 크기가 사과의 위치보다 작으면
    if cur_position + m < i:
        move_distance = (i - m) - cur_position
        # print(f'이동해야할 거리 : {move_distance}')
        ans += move_distance
        # 현재위치를 사과위치 - 바구니 크기로 변경
        cur_position += move_distance
        # print(f'변경된 현재 위치: {cur_position}')
    elif cur_position > i:
        move_distance = cur_position - i 
        # print(f'이동해야할 거리 : {move_distance}')
        ans += move_distance
        # 현재위치를 사과위치 - 바구니 크기로 변경
        cur_position -= move_distance
        # print(f'변경된 현재 위치: {cur_position}')
print(ans)