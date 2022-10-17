n = int(input())
word = input()
countOfTwo = word.count('2')
countOfE = word.count('e')

if countOfTwo == countOfE:
    print('yee')
elif countOfTwo > countOfE:
    print('2')
else:
    print('e')