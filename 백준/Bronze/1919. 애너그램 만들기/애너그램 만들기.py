from collections import Counter

a = input()
b = input()

counterA = Counter(a)
counterB = Counter(b)

print(sum((counterA-counterB).values()) + sum((counterB-counterA).values()))