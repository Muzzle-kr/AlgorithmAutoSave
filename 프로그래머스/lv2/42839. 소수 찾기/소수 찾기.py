import math
import itertools

def isPrime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
        
    return True
        
    
    

def solution(numbers):
    answer = 0
    length = len(numbers)
    listOfNumber = []

    for i in range(1, length + 1):
        combination = list(itertools.permutations(numbers, i))
        
        for num in combination:
            combineNumber = int("".join(num))
            if combineNumber not in listOfNumber and isPrime(combineNumber):
                listOfNumber.append(combineNumber)
                answer += 1
    return answer