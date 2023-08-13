N = int(input())

def check_palindrome(word, cnt):
    length = len(word)
    
    for i in range(length//2):
        if word[i] != word[length-1-i]:
            if cnt == 1:
                return 2
            
            word_arr1 = list(word)
            word_arr2 = list(word)
            
            word_arr1[i] = ''
            word_arr2[length-1-i] = ''
            
            # print(f'word: {word}')
            # print(f'word_arr1: {"".join(word_arr1)}')
            # print(f'word_arr2: {"".join(word_arr2)}')
            
            
            if check_palindrome("".join(word_arr1), cnt+1) == 0 or check_palindrome("".join(word_arr2), cnt+1) == 0:
                return 1
            else:
                return 2
    return 0

for _ in range(N):
    word = input()
    
    print(check_palindrome(word, 0))
        
    


