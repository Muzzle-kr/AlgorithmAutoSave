sentence = input()

frequentlyWords = {}
for s in sentence:
  s = s.upper()

  if s in frequentlyWords:
    frequentlyWords[s] = frequentlyWords[s] + 1
  else:
    frequentlyWords[s] = 1


frequentlyWord = "" 
maxNum = max(frequentlyWords.values())
count = 0
for j in frequentlyWords.items():
  if j[1] == maxNum:
      frequentlyWord = j[0]
      maxNum = j[1]
      count += 1

if count == 1:
  print(frequentlyWord)
else:
  print("?")