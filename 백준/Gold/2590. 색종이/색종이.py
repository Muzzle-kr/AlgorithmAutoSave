arr = [int(input()) for _ in range(6)]
ans = []
cnt = 0

for i in range(5, -1, -1):
    if i == 5:
        cnt += arr[i]
    elif i == 4:
        # 5개짜리에는 1을 11개 저장 가능
        for _ in range(arr[i]):
            arr[0] -= min(11, arr[0])
            cnt += 1
    elif i == 3:
        # 4개짜리에는 2를 최대 5개 혹은 1칸 20개 저장
        for _ in range(arr[i]):
            two_cnt = min(5, arr[1])
            arr[1] -= two_cnt
            arr[0] -= min(20 - (two_cnt * 4), arr[0])
            cnt += 1
    elif i == 2:
        # 3개 짜리는 4개씩 저장 가능
        cnt += arr[i] // 4
        arr[i] %= 4
        
        # 3개 짜리 1개일 때, 2칸 5개, 1칸 27칸 저장 가능
        if arr[i] == 1:
            two_cnt = min(5, arr[1])
            arr[1] -= two_cnt
            arr[0] -= min(27 - (two_cnt * 4), arr[0])
            cnt += 1
        # 3개 짜리 2개일 때, 2칸 3개, 1칸 18개 저장 가능
        elif arr[i] == 2:
            two_cnt = min(3, arr[1])
            arr[1] -= two_cnt
            arr[0] -= min(18 - (two_cnt * 4), arr[0])
            cnt += 1
        # 3개 짜리 3개일 때, 2칸 1개, 1칸 9개 저장 가능
        elif arr[i] == 3:
            two_cnt = min(1, arr[1])
            arr[1] -= two_cnt
            arr[0] -= min(9 - (two_cnt * 4), arr[0])
            cnt += 1
            
    elif i == 1:
        # 2칸 짜리 최대 9개 저장 가능
        cnt += arr[i] // 9
        arr[i] %= 9
        
        # 2칸짜리 1개 이상 일 때, 
        if arr[i] > 0:
            arr[0] -= min(36 - (arr[i] * 4), arr[0])
            cnt += 1
    else:
        while arr[0] > 0:
            arr[0] -= min(36, arr[0])
            cnt += 1
print(cnt)
