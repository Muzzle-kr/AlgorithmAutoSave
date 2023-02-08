import sys
input = sys.stdin.readline
n, m = map(int, input().split())
isUsed = [False] * (100001)
initialArr = sorted(list(map(int, input().split())))
checkDuplicated = {}

def func(arr):
    global checkDuplicated
    if len(arr) == m:
        if str(arr) in checkDuplicated:
            return
        
        checkDuplicated[str(arr)] = True
        print(*arr)
        return

    for new_idx in range(n):
        if isUsed[new_idx]:
            continue
        
        arr.append(initialArr[new_idx])
        func(arr)
        arr.pop()
        
new_arr = []
for idx in range(len(initialArr)):
    new_arr.append(initialArr[idx])
    func(new_arr)
    new_arr.pop()