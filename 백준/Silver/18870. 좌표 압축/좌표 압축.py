import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
setArr = set(arr)
index = sorted(setArr)
dictArr = {}

for idx, i in enumerate(index):
    dictArr[i] = idx
    
result = []
for i in arr:
    result.append(dictArr[i])
    # print(index.index(i))
    
print(*result)
# print(arr, index)
    
