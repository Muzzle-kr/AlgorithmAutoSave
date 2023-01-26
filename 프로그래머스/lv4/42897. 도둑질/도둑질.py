import math

def solution(money):
    moneyStart = [0] + money[1:]
    moneyEnd = [0] + money[:-1]
    
    for i in range(2, len(moneyStart)):
        moneyStart[i] = max(moneyStart[i-1], moneyStart[i-2] + moneyStart[i])
        
    for i in range(2, len(moneyEnd)):
        moneyEnd[i] = max(moneyEnd[i-1], moneyEnd[i-2] + moneyEnd[i])  
    return max(moneyStart + moneyEnd)