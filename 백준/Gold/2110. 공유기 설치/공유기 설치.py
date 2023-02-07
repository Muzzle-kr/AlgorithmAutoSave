n, c = map(int, input().split())

houses = []

for i in range(n):
    houses.append(int(input()))

houses.sort()

start = 0
end = houses[-1] - houses[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    current = houses[0]
    count = 1
    isMany = False
    
    for i in range(1, len(houses)):
        # count가 공유기 갯수보다 많다면 공유기 거리를 넓힘
        if current + mid <= houses[i]:
            current = houses[i]
            count += 1
            
        if count >= c:
            result = mid
            start = mid + 1
            isMany = True
            break

    if not isMany:
        end = mid - 1
        
            
print(result)