n = int(input())
ans = n - 2
x, y = 1, 1
mod = 1000000007
for i in range(n-2):
    y, x = (x + y)%mod, y
    
print(y, ans)