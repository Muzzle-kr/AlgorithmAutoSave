N = int(input())
comparison = [i for i in range(1, N+1)]
arr = [int(input()) for _ in range(N)]
arr.sort()


ans = 0
for i in range(N):
    if arr[i] != comparison[i]:
        ans += abs(arr[i] - comparison[i])

print(ans)