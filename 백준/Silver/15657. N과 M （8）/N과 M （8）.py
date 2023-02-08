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
        
        # print(f'arr: {arr}, new_idx: {new_idx}, initialArr[new_idx]: {initialArr[new_idx]}')
        if arr[-1] > initialArr[new_idx]:
            continue
        
        arr.append(initialArr[new_idx])
        func(arr)
        arr.pop()
        
new_arr = []
for idx in range(len(initialArr)):
    new_arr.append(initialArr[idx])
    func(new_arr)
    new_arr.pop()