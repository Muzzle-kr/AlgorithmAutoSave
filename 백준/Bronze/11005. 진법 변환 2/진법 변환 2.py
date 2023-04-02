import string
B, N = map(int, input().split())
arr = [i for i in range(10)] + list(string.ascii_uppercase)

def convert(num, base):
    result = ""
    while num >= base:
        remain = num % base 
        if remain >= 10:
            result += arr[remain]
        else:
            result += str(remain)
        
        num //= base
    
    if num >= 10:
        result += arr[num]
    else:
        result += str(num)
    return "".join(list(reversed(result)))

print(convert(B, N))