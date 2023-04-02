while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    arr = sorted([a, b, c])
    
    
    if a == b and b == c:
        print("Equilateral")
    elif arr[2] >= arr[1] + arr[0]:
        print("Invalid")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")