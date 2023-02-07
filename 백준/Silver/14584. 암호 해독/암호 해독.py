from string import ascii_lowercase
word = input()

arr = []
for i in range(int(input())):
    arr.append(input())

result = ""
index = 0

while True:
    newWord = "" 
    ascii = sorted(list(ascii_lowercase))
    index += 1    
    
    if index == 27:
        break
    
    for w in word:
        newWord += ascii[(ord(w) + index) % 97 % 26]
    
    isFind = False
    for i in arr:
        if i in newWord:
            result = newWord
            isFind = True
            break
        
    if isFind:
        break

print(result)

