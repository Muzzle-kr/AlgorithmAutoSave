height = 0
prevBowl = ''
for i in input():  
  if prevBowl == i:
    height += 5
  else: 
    height += 10
  prevBowl = i

print(height)