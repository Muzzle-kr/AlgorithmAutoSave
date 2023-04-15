for _ in range(int(input())):
    total = 0
    min_num = int(1e9)
    arr = list(map(int, input().split()))
    
    for num in arr:
        if num % 2 == 0:
            total += num
            min_num = min(min_num, num)
    print(total, min_num)