repeat = int(input())

for i in range(repeat):
    candy, numOfBrothers = map(int, input().split())
    
    brothers = candy // numOfBrothers
    dad = candy % numOfBrothers
    print('You get %d piece(s) and your dad gets %d piece(s).' %(brothers, dad))
