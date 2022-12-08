countArr = []
for i in range(5):
    name = input()
    
    if "FBI" in name:
        countArr.append(i+1)
        
if len(countArr) == 0:
    print("HE GOT AWAY!")
else:
    print(*countArr)