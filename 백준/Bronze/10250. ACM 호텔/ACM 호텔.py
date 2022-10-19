import math
repeat = int(input())

for _ in range(repeat):
    H, W, N = map(int, input().split())
    number = ""
    floor = ""
    
    if (N / H < 1):
        number = str(math.floor(N / H) + 1).zfill(2)
    else:
        if N % H == 0:
            number = str(math.floor(N / H)).zfill(2)
        else:
            number = str(math.floor(N / H) + 1).zfill(2)
    
    if N % H == 0:
        floor = str(H)
    else:
        floor = str(N % H)
    result = int(floor + number)
    print(str(result))