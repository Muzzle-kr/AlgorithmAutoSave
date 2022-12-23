arr = list(map(int, input().split()))

# print(f'  arr: {arr} ')


while True:
  if arr == [1, 2, 3, 4, 5]:
    break
  
  for i in range(len(arr)-1):
    tmp = 0
    if arr[i] > arr[i+1]:
      tmp = arr[i]
      arr[i] = arr[i+1]
      arr[i+1] = tmp
      
      print(*arr)
    