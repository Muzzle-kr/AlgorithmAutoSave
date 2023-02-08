import sys
input = sys.stdin.readline
n, m = map(int, input().split())
isUsed = [False] * (n + 1)
initialArr = sorted(list(map(int, input().split())))


def func(arr):
    if len(arr) >= m:
        print(*arr)
        return

    for new_idx in range(n):
        if isUsed[new_idx]:
            continue
        
        arr.append(initialArr[new_idx])
        # isUsed[new_idx] = True    
        func(arr)
        # isUsed[new_idx] = False
        arr.pop()
        
new_arr = []
for idx, i in enumerate(initialArr):
    new_arr.append(i)
    func(new_arr)
    new_arr.pop()