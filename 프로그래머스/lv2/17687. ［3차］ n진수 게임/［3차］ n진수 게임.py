def solution(n, t, m, p):
    answer = '0'
    
    for i in range(1, t * m):
        answer += convertToN(i, n)

    return "".join([answer[idx] for idx in range(p-1, t * m, m)])

def convertToN(number, n):
    if number == 0:
        return '0'
    
    total = ""
    while number > 0:
        number, mod = divmod(number, n)
        
        if 10 <= mod <= 15 and n > 10:
            total += 'ABCDEF'[mod % 10]
        else:
            total += str(mod)
    
    return total[::-1]