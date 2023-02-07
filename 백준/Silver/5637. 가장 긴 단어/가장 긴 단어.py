maxLengthWords = ""

while True:
    word = input()
    
    isBreak = False
    
    for i in word.split():
        if i == "E-N-D":
            isBreak = True
            break
        count = 0
        string = ""
        
        for w in i:
            if 65 <= ord(w) <= 90 or 97 <= ord(w) <= 122 or ord(w) == 45: 
                count += 1
                string += w
                
                maxLengthWords = string if count > len(maxLengthWords) else maxLengthWords
                
            else:
                string = ""
                count = 0
                
            
    
    if isBreak:
        break
    
print(maxLengthWords.lower())