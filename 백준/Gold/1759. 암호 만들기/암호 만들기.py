import sys
input = sys.stdin.readline
n, m = map(int, input().split())
isUsed = [False] * (m + 1)
initialArr = sorted(list(input().split()))
vowel = ["a", "e", "i", "o", "u"]

def func(arr):
    if len(arr) == n:
        answer = "".join(sorted(arr))
        
        isFind = False
        
        count = 0
        for i in answer:
            if i in vowel:
                isFind = True
            else:
                count += 1
            
            if count >= 2 and isFind:
                print(answer)
                break
            
    for new_idx in range(m):
        if isUsed[new_idx] or arr[-1] > initialArr[new_idx]:
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