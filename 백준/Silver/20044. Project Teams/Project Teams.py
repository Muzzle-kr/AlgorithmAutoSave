N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = []

for i in range(N):
    ans.append(arr[i] + arr[N*2-i-1])

print(min(ans))