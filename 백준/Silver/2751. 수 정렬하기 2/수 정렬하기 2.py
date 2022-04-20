N = int(input())

li = [int(input()) for i in range(N)]

li.sort()

for i in range(N):
  print(li[i])