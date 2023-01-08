def convertDateToNumber(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day
    
def solution(today, terms, privacies):
    answer = []
    termsObj = {}
    referenceDate = convertDateToNumber(today)
    
    for i in terms:
        sort, limit = i.split()
        termsObj[sort] = int(limit)
    
    
    for idx, i in enumerate(privacies):
        date, limit = i.split()
        afterDayNumber = termsObj[limit] * 28
        dateNumber = convertDateToNumber(date)
        expiration = afterDayNumber + dateNumber

        if expiration <= referenceDate:
            answer.append(idx+1)
            
    return answer