N = int(input())
arr = [0] * 16
a = 0
b = 2
for i in range(1, 16):
    a = pow(2, i-1) 
    b += a
    arr[i] = pow(b, 2)

print(arr[N])