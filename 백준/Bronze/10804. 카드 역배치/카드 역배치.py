arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for _ in range(10):
    a, b = map(int, input().split())
    
    while a < b:
        # print('a = %d, b = %d' % (a, b))
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
        a += 1
        b -= 1

for idx, i in enumerate(arr[1::]):
    if idx != len(arr[1::]) - 1:
        print(i, end= " ")
    else:
        print(i)