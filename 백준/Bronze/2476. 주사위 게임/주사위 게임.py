from collections import Counter
throw = int(input())

largest_prize = 0;
    
for _ in range(throw):
    
    def f1(x):
        return dictionary[x]
    
    a = list(map(int, input().split()))
    dictionary = dict(Counter(a))
    max_key = max(dictionary.keys(), key=dictionary.get)
    largest_key = max(list(dictionary.keys()))
    if len(dictionary) == 1:
        prize = int(10000 + (list(dictionary.keys())[0]) * 1000)
    elif len(dictionary) == 2:
        prize = int(1000 + max_key * 100)
    else: 
        prize = int(largest_key * 100)
    
    if largest_prize < prize:
        largest_prize = prize

print(largest_prize)