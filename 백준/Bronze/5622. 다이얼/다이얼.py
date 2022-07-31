sentence = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
count = 0

for s in sentence:
  for idx, d in enumerate(dial):
    if s in d:
      count += (idx + 3)

print(count)