from collections import defaultdict

color_dict = defaultdict(int)
num_arr = [0] * 10

# Input color and number 5 times
for _ in range(5):
    color, number = input().split()
    number = int(number)
    
    color_dict[color] += 1
    num_arr[number] += 1

# Find the maximum color
max_color = max(color_dict, key=color_dict.get)

# Find the maximum number count and the maximum existing number
max_number_count = max(num_arr)

max_exist_number = 0

for i in range(9, 0, -1):
    if num_arr[i] == 1:
        max_exist_number = i
        break
    
result = 0

if color_dict[max_color] == 5:
    if any(num_arr[i:i+5] == [1, 1, 1, 1, 1] for i in range(6)):
        result = 900 + max_exist_number
    else:
        result = 600 + max_exist_number
        
elif max_number_count == 4:
    result = 800 + num_arr.index(4)
    
elif max_number_count == 3:
    if 2 in num_arr:
        result = 700 + (num_arr.index(3) * 10) + num_arr.index(2)
    else:
        result = 400 + num_arr.index(3)
        
elif any(num_arr[i:i+5] == [1, 1, 1, 1, 1] for i in range(6)):
    result = 500 + max_exist_number
    
elif max_number_count == 2:
    if num_arr.count(2) == 2:
        in_max_number = max([i for i, x in enumerate(num_arr) if x == 2])
        result = 300 + in_max_number * 10 + num_arr.index(2)
    else:
        result = 200 + num_arr.index(2)
else:
    result = 100 + max_exist_number

print(result)
