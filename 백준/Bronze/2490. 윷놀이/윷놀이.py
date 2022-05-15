while True:
    try:
        li = list(input().split())
        bae = li.count('0')
        if bae == 0:
            print('E')
        elif bae == 1:
            print('A')
        elif bae == 2:
            print('B')
        elif bae == 3:
            print('C')
        elif bae == 4:
            print('D')
    except EOFError:
        exit()