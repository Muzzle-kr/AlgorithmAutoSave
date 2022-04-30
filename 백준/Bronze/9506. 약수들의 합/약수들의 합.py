while True:
  num = int(input())
  
  if num == -1:
    break
  
  division = []
  for i in range(1, num):
    if num % i == 0:
        division.append(i)
    

  if num == sum(division):
    print(f'{num} = ', end="")
    for j in range(len(division)):
      if j == len(division)-1:
        print(division[j])
      else:
        print(f'{division[j]} + ', end="")
  else: 
    print(f'{num} is NOT perfect.')