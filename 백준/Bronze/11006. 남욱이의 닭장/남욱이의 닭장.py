for _ in range(int(input())):
    legs, chickens = map(int, input().split())
    
    print(chickens * 2 - legs, chickens - (chickens * 2 - legs))