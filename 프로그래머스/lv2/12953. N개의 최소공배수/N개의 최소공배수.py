import math
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
        
        
def lcm(a, b):
     return (a * b) // gcd(a, b)

def solution(arr):
    answer = []
    stack = []
    
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            stack.append(lcm(stack.pop(), i))
    
    return stack[0]