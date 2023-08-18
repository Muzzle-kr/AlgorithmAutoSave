N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
# 짝수 일 때
if N % 2 == 0:
    for i in range(N//2):
        ans = max(ans, arr[i] + arr[N-1-i])
    
else:
    for i in range(N//2):
        ans = max(ans, arr[i] + arr[N-2-i])
    ans = max(ans, arr[N-1])

print(ans)