morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
def solution(letter):
    morseArray = list(letter.split(" "))
    answer = ""
    standardNum = 97
    for m in morseArray:
        answer += chr(standardNum + morse.index(m))
    return answer