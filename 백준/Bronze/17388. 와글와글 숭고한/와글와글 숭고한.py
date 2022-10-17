s, k, h = map(int, input().split())

if k + s + h >= 100:
    print("OK")
else:
    small = 9999
    if small > k:
        small = k
    
    if small > s:
        small = s
        
    if small > h:
        small = h
    
    if small == k:
        print("Korea")
    elif small == s:
        print("Soongsil")
    else:
        print("Hanyang")
