from itertools import combinations

n = int(input())
result = [0, 0]

for i in range(n):
    arr = list(map(int, input().split()))
    
    combi_arr = list(combinations(arr, 3))
    
    # print(f'combi_arr: {combi_arr}')
    for ca in combi_arr:
        # print(f'ca: {ca}')
        if sum(ca) % 10 >= result[0]:
            result = [sum(ca) % 10, i+1]

print(result[1])