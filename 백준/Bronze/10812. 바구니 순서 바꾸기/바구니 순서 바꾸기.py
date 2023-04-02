n, m = map(int, input().split())
arr = [i+1 for i in range(n)]

for _ in range(m):
    start, end, mid = map(int, input().split())
    start -= 1
    end -= 1
    mid -= 1
    arr = arr[:start] + arr[mid:end+1] + arr[start:mid] + arr[end+1:]

print(*arr)