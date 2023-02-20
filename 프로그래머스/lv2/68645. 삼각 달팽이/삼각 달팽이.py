from itertools import chain
def solution(n):
    answer = [[0] * (i+1) for i in range(n)]
    answer[0][0] = 1
    global count, i, j
    i = 0
    j = 0
    count = 2
    
    def ascending():
        global count, i, j
        
        for k in range(i+1, n):
            if answer[k][j] != 0:
                i = k - 1
                break
            
            if k == n-1:
                i = k
                
            answer[k][j] = count
            count += 1
            
    
    def descending():
        global count, i, j
        
        for k in range(i-1, -1, -1):
            if answer[k][j-1] != 0:
                # print(f'descending: i: {i}, j: {j}')
                i = k + 1
                break
            
            j -= 1
            answer[k][j] = count
            count += 1
            
    def inARow():
        global count, i, j
        
        for k in range(j+1, n):
            # print(answer)
            # print(f'inARow: i: {i}, j: {j}, k: {k}')
            if answer[i][k] != 0:
                j = k - 1
                break
            
            if k == n-1:
                j = k
                
                
            answer[i][k] = count
            count += 1
            
    number = n
    while number > 0:
    
        ascending() 
        
        number -= 1
        # print(f'ascending 후 number: {number}')
        if number == 0:
            break
        
        inARow()
        
        number -= 1
        # print(f'inArow 후 number: {number}')
        if number == 0:
            break
        
        
        descending()
        
        number -= 1
        # print(f'descending 후 number: {number}')
        if number == 0:
            break
        
    
    return list(chain(*answer))