b, n = input().split()
n = int(n)
import string
arr = [i for i in range(10)] + list(string.ascii_uppercase)

def convertToBaseN(x, n):
    result = 0
    length = len(x)
    
    for i in range(length):
        idx = 0
        
        if x[i].isdigit():
            idx = int(x[i])
        else:
            idx = arr.index(x[i])
        
        result += pow(n, length-i-1) * idx
    
    return result
        
print(convertToBaseN(b, n))