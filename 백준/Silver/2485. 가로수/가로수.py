import math

N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))

tmpArr = []

for idx, i in enumerate(arr):
    if idx != 0:
        # 앞의 가로수와의 거리 차이를 배열에 append
        # print(f'i = {idx}')
        tmpArr.append(arr[idx] - arr[idx-1])

gcd = math.gcd(*tmpArr)
result = []

for i in tmpArr:
    result.append(round(i / gcd)-1)
# print(gcd, tmpArr, result)
print(sum(result))

