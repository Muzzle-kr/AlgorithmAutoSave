x = []
y = []

for _ in range(3):
    a, b = map(int, input().split())
    
    x.append(a)
    y.append(b)

print(min(set(x), key=x.count), min(set(y), key=y.count))