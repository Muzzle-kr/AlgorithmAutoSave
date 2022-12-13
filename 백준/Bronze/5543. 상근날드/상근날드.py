burger = 30000
coke = 30000
for i in range(5):
    price = int(input())
    if i < 3:
        if burger > price:
            burger = price
    else:
        if coke > price:
            coke = price

print(burger + coke - 50)
            
    