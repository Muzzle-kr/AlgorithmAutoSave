while True:
    def findPalindrome(str):
        start = 0
        end = len(str) - 1
        isPalindrome = True
        
        while start <= end:
            if str[start] != str[end]:
                isPalindrome = False
                
            start += 1
            end -= 1
        return isPalindrome
    
    num = int(input())
    if num == 0:
        exit()
    else:
        if findPalindrome(str(num)):
            print("yes")
        else:
            print("no")

    
    