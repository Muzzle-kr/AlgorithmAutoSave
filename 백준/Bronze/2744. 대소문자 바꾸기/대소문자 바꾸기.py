result = ""

for w in input():
    if ord(w) >= 65 and ord(w) <= 90:
        result += chr(ord(w) + 32)
    else:
        result += chr(ord(w) - 32)
        

print(result)