K, N = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(K+1)]

for i in range(K):
    prefix[i+1] = prefix[i] + arr[i]

answer = []

for i in range(N, K+1):
    answer.append(prefix[i] - prefix[i-N])

print(max(answer))