repeat = int(input())

for i in range(repeat):
    targetNum = int(input())
    pairs = []
    
    
    for j in range(1, targetNum + 1):
        for k in range(j, targetNum):
            if j == k:
                continue
            if j + k == targetNum:
                pairs.append((j, k))
    print(f'Pairs for {targetNum}: ', end="")
    
    if len(pairs) > 0:
        for idx, l in enumerate(pairs):
            if idx != len(pairs) - 1:
                print(l[0], l[1], end=", ")
            else:
                print(l[0], l[1])
    else:
        print()