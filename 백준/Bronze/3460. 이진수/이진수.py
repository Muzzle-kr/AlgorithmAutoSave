n = int(input())
numbers = [int(input()) for _ in range(n)]

for number in numbers:
    positions = []
    binary = list(reversed(list(bin(number)[2:])))
    
    for idx in range(len(binary)):
        if binary[idx] == "1":
            positions.append(idx)
    
    print(*positions)