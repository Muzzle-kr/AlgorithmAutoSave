import sys
input = sys.stdin.readline
arr = [[0 for j in range(100)] for i in range(100)]

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    for j in range(a, a + 10):
        for k in range(b, b + 10):
            if arr[j][k] != 1:
                # print(f'j: {j}, k: {k}')
                arr[j][k] = 1
    # print(f'작업 후 arr : {arr}')



count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count += 1
# print(arr)
print(count)
# 색칠놀이로 풀면 됨
