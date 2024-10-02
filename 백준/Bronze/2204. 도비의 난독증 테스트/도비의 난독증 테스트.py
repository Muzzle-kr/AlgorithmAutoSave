while True:
    n = int(input())
    
    if n == 0:
        break
    
    words = []
    for i in range(n):
        word = input()
        words.append(word)
    
    words.sort(key=lambda x: x.lower())
    
    print(words[0])