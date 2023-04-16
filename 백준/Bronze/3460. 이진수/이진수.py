def convertToBinary(n):
    string = ""
    
    while n > 1:
        string += str(n % 2)
        n = n // 2
    
    string += str(n)
    return string

for _ in range(int(input())):
    number = int(input())
    arr = []
    
    binary = convertToBinary(number)

    for idx, b in enumerate(binary):
        if b == "1":
            arr.append(idx)
    print(*arr)