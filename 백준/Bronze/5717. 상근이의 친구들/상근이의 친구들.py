while True:
    boy, girl = map(int, input().split())
    if boy == 0 and girl == 0:
        break
    else:
        print(boy + girl)