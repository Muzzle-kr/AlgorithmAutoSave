def main():
    N = int(input())
    flag = True
    
    for _ in range(N):
        S = int(input())
        
        if isValidPasswordKey(S):
            print("YES")
        else:
            print("NO")
    
def isValidPasswordKey(s):
    for i in range(2, 1_000_000):
        if s % i == 0:
            return False
    return True

main()