def solution(s):
    answer = True
    
    s = s.lower()
    np = 0
    ny = 0
    
    for i in s:
        if i == "p":
            np += 1
        
        if i == "y":
            ny += 1
    if np == ny:
        return True
    else:
        return False