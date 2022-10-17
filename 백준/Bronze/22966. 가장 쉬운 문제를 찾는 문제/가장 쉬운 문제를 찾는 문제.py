smallLevel = 99999
result = ""

for _ in range(int(input())):
    title, level = input().split()
    level = int(level)
    
    if smallLevel > level:
        smallLevel = level
        result = title
        
print(result)