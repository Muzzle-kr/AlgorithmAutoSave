arr = input().split("-")
total = 0

for i in arr[0].split("+"):
    total += int(i)

for i in arr[1:]:
    total -= sum([int(i) for i in i.split("+")])

print(total)