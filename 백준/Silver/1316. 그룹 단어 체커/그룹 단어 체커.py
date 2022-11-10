N = int(input())

count = 0 

for _ in range(N):
  word = input()  
  lastWord = ""
  obj = {}
  groupYn = 1
  
  for w in word:
    if lastWord == "":
      lastWord = w
      obj[w] = 1
      continue
  
    if lastWord == w:
      obj[w] = obj[w] + 1
      continue
    
    else:
      if w in obj:
        groupYn = 0
        break
      else:
        lastWord = w
        obj[w] = 1
  if groupYn == 1:
    count += 1
    
print(count)