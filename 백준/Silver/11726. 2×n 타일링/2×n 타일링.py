n = int(input())
memo = [0] * (n + 2)
memo[1] = 1
memo[2] = 1

for i in range(2, n + 2):
    memo[i] = memo[i-2] + memo[i-1]

print(memo[n + 1] % 10007)