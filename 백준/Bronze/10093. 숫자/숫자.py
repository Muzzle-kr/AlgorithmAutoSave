a, b = map(int, input().split())

arr = []
    
if a > b:
    for i in range(b + 1, a):
        arr.append(i)
        
elif a < b:
    for i in range(a + 1, b):
        arr.append(i)

if len(arr):
    print(len(arr))

    for idx, i in enumerate(arr):
        if idx != len(arr) - 1:
            print(i, end=" ")
        else:
            print(i)
else:
    print(0)