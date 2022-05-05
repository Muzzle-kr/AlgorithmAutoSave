for _ in range(int(input())):
    r, c, e = map(int, input().split())
    if r > c - e: 
        print('do not advertise')
    elif r < c - e:
        print('advertise')
    else:
        print('does not matter')