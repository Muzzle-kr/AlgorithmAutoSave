def recursion(s, l, r, count):
    # print(f's: {s}, l: {l}, r: {r}')
    if l >= r: return (1, count)
    elif s[l] != s[r]: return (0, count)
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s):

    result = recursion(s, 0, len(s)-1, 1)
    return result
    
for i in range(int(input())):
  print(*isPalindrome(input().rstrip()))