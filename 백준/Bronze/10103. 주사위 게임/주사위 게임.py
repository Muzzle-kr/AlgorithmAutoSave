chang = 100
sang = 100

for _ in range(int(input())):
    c, s = map(int, input().split())
    
    if c > s:
        sang -= c
    elif c < s:
        chang -= s

print(chang, sang, sep="\n") 