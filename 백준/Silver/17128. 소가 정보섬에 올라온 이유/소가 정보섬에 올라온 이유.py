import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
q_arr = list(map(int, input().split()))
arr_arr = arr + arr
dp = [0] * n

for i in range(n):
    dp[i] = arr_arr[i] * arr_arr[i+1] * arr_arr[i+2] * arr_arr[i+3]

# 그 결과가 미리 구해놓기
result = sum(dp)
for q in q_arr:
    for i in range(4):
        # 해당 숫자를 포함하는 idx-3부터 ~ 0까지
        n_idx = (q-1-i) % n
        # 숫자 - 붙여서 바꿔놓기
        dp[n_idx] = -dp[n_idx]
        # 기존 값에 부호바꿔서 2번 더하면 정답
        result += 2 * dp[n_idx]
    print(result)