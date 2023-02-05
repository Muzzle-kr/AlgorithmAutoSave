from collections import Counter
dict = {}

n, m = map(int, input().split())

arr = list(map(int, input().split()))


new_arr = sorted(list(Counter(arr).items()), key=lambda x: -x[1])

print_result = []
for i in new_arr:
    for j in range(i[1]):
        print_result.append(i[0])

print(*print_result)
    