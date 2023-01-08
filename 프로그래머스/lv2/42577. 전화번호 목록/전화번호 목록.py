def solution(phone_book):
    answer = True
    hashTable = {}
    
    for i in phone_book:
        hashTable[i] = 1
    
    for i in phone_book:
        for j in range(1, len(i)):    
            if i[:j] in hashTable:
                # return False
                hashTable[i[:j]] += 1
    
    if max(list(hashTable.values())) > 1:
        return False
        
    return True