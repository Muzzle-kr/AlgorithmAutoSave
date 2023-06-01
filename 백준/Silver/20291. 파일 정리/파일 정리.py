from collections import defaultdict
ext_dict = defaultdict(int)
for _ in range(int(input())):
    name, ext = input().split(".")
    ext_dict[ext] += 1
    
result = sorted(ext_dict.items(), key=lambda x: x[0])

for name, ext in result:
    print(name, ext)