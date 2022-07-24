# 나머지와 몫이 같은 숫자를 구함

division = int(input())
base = division + 1
increase = 0
total = 0
arr = []
for i in range(1, division):
    increase += base
    total += increase
    # arr.append(increase)
    # print(f'increase: %d, base: %d, total: %d' % (increase, base, total))

# print(arr)
print(total)