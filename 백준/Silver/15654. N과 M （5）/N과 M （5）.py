import sys
input = sys.stdin.readline
n, m = map(int, input().split())
isUsed = [False] * (n + 1)
initialArr = sorted(list(map(int, input().split())))


def func(arr):
    if len(arr) >= m:
        print(*arr)
        return

    for idx in range(n):
        if isUsed[idx]:
            continue
        arr.append(initialArr[idx])
        isUsed[idx] = True    
        func(arr)
        isUsed[idx] = False
        arr.pop()
        
new_arr = []
for idx, i in enumerate(initialArr):
    new_arr.append(i)
    isUsed[idx] = True
    func(new_arr)
    new_arr.pop()
    isUsed[idx] = False