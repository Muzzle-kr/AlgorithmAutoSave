totalOfCost = 0
sumOfCost = 0

for i in range(10):
    cost = int(input())
    if i == 0:
        totalOfCost = cost
    else:
        sumOfCost += cost

print(totalOfCost - sumOfCost)