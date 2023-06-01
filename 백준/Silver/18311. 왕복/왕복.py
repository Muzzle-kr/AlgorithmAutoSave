n, k = map(int, input().split())
course = list(map(int, input().split()))
course = [*course] + [*reversed(course)]

s = 0
for idx, c in enumerate(course):
    s += c
    
    if s >= k:
        if idx > n:
            if s == k:
                print(n - (idx - n)-1)
            else:
                print(n - (idx - n))
        else:
            if s == k:
                print(idx+2)
            else:
                print(idx+1)
        exit()