censorship = "CAMBRIDGE"

word = input().rstrip()
result = ""

for w in word:
    
    isCensor = False
    for c in censorship:
        if c == w:
            isCensor = True
            break
    
    if not isCensor:
        result += w

print(result)    