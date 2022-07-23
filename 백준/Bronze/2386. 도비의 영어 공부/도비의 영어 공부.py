while True:
    a = input()
    if a == '#':
        break
    
    alphabet = a[0]
    sentence = a[2:]
    
    count = 0
    for syllable in sentence:
        if syllable.lower() == alphabet:
            count += 1
    
    print(f'%s %d' %(alphabet, count))