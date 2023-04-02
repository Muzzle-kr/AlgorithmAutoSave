n = int(input())

for _ in range(n):
    change_unit_arr = [25, 10, 5, 1]
    result = [0, 0, 0, 0]
    change = int(input())
    
    for i in range(4):
        n = change//change_unit_arr[i]
        result[i] += n
        change %= change_unit_arr[i]
    print(*result)