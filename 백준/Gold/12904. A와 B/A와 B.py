import sys
input = sys.stdin.readline
W = list(input().rstrip())
T = list(input().rstrip())
    
while W != T:
    
    if len(T) == 0:
        print("0")
        exit()
        
    if T[-1] == "A":
        T.pop()
        
    elif T[-1] == "B":
        T.pop()
        T.reverse()
        
    else:
        print("0")
        exit()

print("1")