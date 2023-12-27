s = input()
s_length = len(s)

def convertToInt(s):
    return int(s)

def getSum(str):
    total = 0
    
    for s in str:
        total += convertToInt(s)
    
    return total    
if getSum(s[:s_length//2]) == getSum(s[s_length//2:]):
    print("LUCKY")
else:
    print("READY")