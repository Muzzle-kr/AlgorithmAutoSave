N = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']


for _ in range(N):
    countOfVowels = 0
    countOfConsonants = 0
    sentence = input().lower()
    
    for w in sentence:
        if w != ' ' and w in vowels:
            countOfVowels += 1
        else:
            if w != ' ':
                countOfConsonants +=1
    print(countOfConsonants, countOfVowels)
    