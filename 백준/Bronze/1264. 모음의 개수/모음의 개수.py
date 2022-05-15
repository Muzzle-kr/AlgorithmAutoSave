while True:
    def findNumberOfVowel(str):
        result = 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        for w in str:
            if w.lower() in vowel:
                result += 1

        return result
    sentence = input()
    if sentence == "#":
        exit()
    else:
        print(findNumberOfVowel(sentence))
    
    