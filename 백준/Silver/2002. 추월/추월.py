N = int(input())

out_cars = {}
in_cars = {}

for i in range(N):
    in_cars[input()] = i
    
for i in range(N):
    out_cars[input()] = i
    
answer = 0
out_car_numbers = list(out_cars.keys())

for i in range(N-1):
    now_in = in_cars[out_car_numbers[i]]
    
    for j in range(i+1, N):
        next_in = in_cars[out_car_numbers[j]]
        
        if now_in > next_in:
            answer += 1
            break
    
print(answer)