import time
def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    global answer
    answer = 0
    
    def dfs(string):
        global answer
        answer += 1
        if string == word:
            return True
        
        if len(string) == 5:
            return False
        
        for alphabet in alphabets:
            if dfs(string + alphabet):
                return True
        
    if dfs(""):
        return answer - 1