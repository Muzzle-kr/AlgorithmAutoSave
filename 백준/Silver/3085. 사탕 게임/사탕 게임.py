def check(arr):
    max_cnt = 1
    
    # 행 방향 연속한 동일한 원소의 개수 확인
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j-1] == arr[i][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    # 열 방향 연속한 동일한 원소의 개수 확인
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if arr[i-1][j] == arr[i][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt

n = int(input())
arr = [list(input()) for _ in range(n)]
result = 0

# 모든 가능한 인접한 두 원소 교환 시도
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            result = max(result, check(arr))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if i + 1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            result = max(result, check(arr))
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(result)
