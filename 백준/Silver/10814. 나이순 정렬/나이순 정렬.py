repeat = int(input())
result = {}
for _ in range(repeat):
    age, name = input().split()
    age = int(age)
    name = name.strip()
    if age in result:
        result[age].append(name)
    else:
        result[age] = [name]

sorted_result = sorted(result.items(), key = lambda item: item[0]);

for key, val in sorted_result:
    if len(val) >= 2:
        for each in val:
            print(key, each)
    else:
        print(key, val[0])