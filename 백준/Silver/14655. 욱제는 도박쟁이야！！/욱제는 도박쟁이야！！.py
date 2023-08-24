N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = [abs(arr1[i]) for i in range(N)]
arr2 = [-abs(arr2[i]) for i in range(N)]

print(sum(arr1) - sum(arr2))
