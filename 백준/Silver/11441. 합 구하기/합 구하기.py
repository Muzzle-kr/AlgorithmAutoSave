import sys
input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())
sum_arr = [0] * (n+1)

for i in range(1, n+1):
    sum_arr[i] = sum_arr[i-1] + arr[i]
    
for _ in range(m):
    s, e = map(int, input().split())
    
    print(sum_arr[e] - sum_arr[s-1])