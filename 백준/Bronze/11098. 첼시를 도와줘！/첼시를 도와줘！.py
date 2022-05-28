repeat = int(input())

for i in range(repeat):
    numOfPlayers = int(input())
    maxPrice = 0;
    mostExpensivePlayer = '';
    for _ in range(numOfPlayers):
        price, nameOfPlayer = input().split();
        price = int(price);
        if price > maxPrice:
            maxPrice = price;
            mostExpensivePlayer = nameOfPlayer;
            
    print(mostExpensivePlayer);


