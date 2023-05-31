def fight(a, b):
    if a == b:
        return 0
    
    if a == "R":
        if b == "P":
            return 2
        else:
            return 1
    elif a == "S":
        if b == "P":
            return 1
        else:
            return 2
    elif a == "P":
        if b == "S":
            return 2
        else:
            return 1
    

for _ in range(int(input())):
    player1, player2 = 0, 0
    
    for _ in range(int(input())):
        a, b = input().split()
        if fight(a, b) == 1:
            player1 += 1
        elif fight(a, b) == 2: 
            player2 += 1
    
    if player1 == player2:
        print("TIE")
    elif player1 > player2:
        print("Player 1")
    else:
        print("Player 2")