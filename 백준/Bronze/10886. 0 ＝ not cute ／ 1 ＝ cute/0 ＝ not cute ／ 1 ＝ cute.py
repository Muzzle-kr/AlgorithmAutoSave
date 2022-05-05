N = int(input())

cute = 0
notCute = 0
for _ in range(N):
  vote = int(input())
  
  if vote == 0:
    notCute += 1
  else:
    cute += 1
    
if cute > notCute:
  print("Junhee is cute!")
else:
  print("Junhee is not cute!")
    