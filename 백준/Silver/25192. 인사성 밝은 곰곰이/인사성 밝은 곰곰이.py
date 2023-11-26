id_set = set()
result = 0

for _ in range(int(input())):
    w = input()
    if w == "ENTER":
        result += len(id_set)
        id_set = set()
        continue
    
    id_set.add(w)


print(result + len(id_set))