n = int(input())
fibonacci_num_arr = [1, 1, 2, 4]

for i in range(4, 68):
    fibonacci_num_arr.append(fibonacci_num_arr[i-1] + fibonacci_num_arr[i-2] + fibonacci_num_arr[i-3] + fibonacci_num_arr[i-4])

for i in range(n):
    print(fibonacci_num_arr[int(input())])