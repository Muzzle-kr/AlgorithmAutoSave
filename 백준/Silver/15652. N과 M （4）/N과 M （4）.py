import sys
input = sys.stdin.readline
n, m = map(int, input().split())

isUsed = [False] * (n + 1)

def func(arr):
    if len(arr) >= m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if isUsed[i] or i < arr[-1]:
            continue
        arr.append(i)
        func(arr)
        arr.pop()
        
for i in range(1, n + 1):
    arr = []
    arr.append(i)
    func(arr)