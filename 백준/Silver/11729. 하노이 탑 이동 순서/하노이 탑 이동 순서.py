def towerOfHanoi(n, a, b, c):
    if n == 1:
        print(a, b)
        return
    
    if n > 1:
        towerOfHanoi(n-1, a, c, b)
        print(a, b)
        towerOfHanoi(n-1, c, b, a)
         
N = int(input())
count = 0
print(2**N - 1)
towerOfHanoi(N, 1, 3, 2)