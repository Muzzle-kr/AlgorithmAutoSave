n = input()
cnt = 0

while True:
    
    if len(n) > 1:
        s = 0
        
        for i in range(len(n)):
            s += int(n[i])
            
        n = str(s)
    else:
        print(cnt)
        if int(n) % 3 == 0:
            print("YES")
        else:
            print("NO")
        break
    cnt += 1