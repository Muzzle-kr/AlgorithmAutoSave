try :
    while True:
        a, b = input().split()
        chr = ""
        lastIndex = 0
        for i in a:
            isFind = False
            
            for j in range(lastIndex, len(b)):
                if i == b[j]:
                    chr += b[j]
                    lastIndex = j + 1
                    isFind = True
                    break
            
            if not isFind:
                break
            
        if a == chr:
            print("Yes")
        else:
            print("No")
                    
except:
    exit()
