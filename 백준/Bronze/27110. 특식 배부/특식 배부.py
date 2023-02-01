num = int(input())
a, b, c = map(int, input().split())

sum = 0

def func(num, limit, sum):    
    
    if num >= limit:
        sum += limit
    else:
        sum += num
        
    return sum
    
sum = func(a, num, sum)
sum = func(b, num, sum)
sum = func(c, num, sum)
print(sum)