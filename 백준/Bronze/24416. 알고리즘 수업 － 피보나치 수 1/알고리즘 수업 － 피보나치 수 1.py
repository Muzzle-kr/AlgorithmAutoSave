def fib(n, count):
    count += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1, count) + fib(n - 2, count);
    

def fibonacci(n, count):
    count += 1
    arr = [0] * (n + 1)
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1
    
    if n == 1 or n == 2:
        count += 1 
    else:
        for i in range(3, n):
            arr[i] = arr[i-2] + arr[i-1]
            count += 1
    return count


result = [0, 0]

N = int(input())
result[0] = fib(N, result[0])
result[1] = fibonacci(N, result[1])
print(*result)