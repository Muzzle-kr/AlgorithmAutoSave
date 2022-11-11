import sys
input = sys.stdin.readline

max = 0
result = [1, 1]

for i in range(9):
  arr = list(map(int, input().split()))
  for j in range(9):
    if max < arr[j]:
      max = arr[j]
      result[0] = i + 1
      result[1] = j + 1

print(max)
print(result[0], end=" ")
print(result[1])