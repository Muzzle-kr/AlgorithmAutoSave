repeat = int(input())

for i in range(repeat):
  priceOfCar = int(input())
  numOfOptions = int(input())
  sum = priceOfCar;
  
  if numOfOptions != 0:
    for j in range(numOfOptions):
      numOfParticular, option = map(int, input().split())
      sum += numOfParticular * option
  print(sum)