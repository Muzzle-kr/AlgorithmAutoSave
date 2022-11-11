arr = []
for i in range(666, 10000000):
  if str(i).count('666') >= 1:
    arr.append(i)

print(arr[int(input())-1])