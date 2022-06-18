# 2 * (N - 1) 만큼의 칸이 존재해야함
repeat = int(input())


for i in range(repeat, 0, -1):
  max = (2 * repeat - 1);
  num = (2 * i - 1);
  gap = int(((max - num) / 2))
  # print("max = ", max, "num = ", num, "gap = ", gap);
  print(" " * int((max - num)/2) + "*" * num)