N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

arr_diff = [arr[i+1] - arr[i] for i in range(N-1)]
arr_diff.sort(reverse=True)
print(sum(arr_diff[K-1:]))