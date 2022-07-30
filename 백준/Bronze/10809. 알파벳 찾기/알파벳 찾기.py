string = input()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
result = []
    
for a in alphabet:
    try:
        idx = string.index(a)
        result.append(idx)
    except:
        result.append(-1)

for a in result:
    print(a, end=" ") 