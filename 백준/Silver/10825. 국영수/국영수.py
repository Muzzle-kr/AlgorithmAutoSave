arr = []
for i in range(int(input())):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math) 
    
    arr.append([name, korean, english, math])
    
print("\n".join([i[0] for i in sorted(arr, key=lambda x:(-x[1], x[2], -x[3], x[0]))]))