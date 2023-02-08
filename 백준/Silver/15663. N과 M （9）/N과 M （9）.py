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
            # print(f'arr: {arr} is duplicated')
            return
        
        checkDuplicated[str(arr)] = True
        print(*arr)
        return

    for new_idx in range(n):
        if isUsed[new_idx]:
            continue
        
        arr.append(initialArr[new_idx])
        isUsed[new_idx] = True
        func(arr)
        isUsed[new_idx] = False
        arr.pop()
        
new_arr = []
for idx in range(len(initialArr)):
    new_arr.append(initialArr[idx])
    isUsed[idx] = True
    func(new_arr)
    isUsed[idx] = False
    new_arr.pop()