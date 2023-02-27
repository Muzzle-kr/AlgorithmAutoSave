from collections import Counter
n, m, block = map(int, input().split())

mine = sum([list(map(int, input().split())) for _ in range(n)],[])
minHeight = 257
maxHeight = -1
time = 1000000000
answerHeight = 0
hash = Counter(mine)
maxHeight = max(mine)
minHeight = min(mine)    


for height in range(minHeight, maxHeight+1):
        isPossible = True
        tmpTime = 0
        tmpBlock = block
        
        for [key, val] in sorted(hash.items(), key=lambda x: x[0], reverse=True):
            if key > height:
                tmpTime += (key - height) * val * 2
                tmpBlock += (key - height) * val
                    
            else:
                if tmpBlock >= (height - key) * val:
                    tmpTime += (height - key) * val
                    tmpBlock -= (height - key) * val
                else:
                    isPossible = False
                    break
            if not isPossible:
                break
        
        if isPossible and time >= tmpTime:
            time = tmpTime
            answerHeight = height
            
print(time, answerHeight)