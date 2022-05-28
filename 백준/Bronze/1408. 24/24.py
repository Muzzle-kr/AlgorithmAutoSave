curHour, curMin, curSec = map(int, input().split(":"));
endHour, endMin, endSec = map(int, input().split(":"));

def convertToStrWithZero(num):
    if num < 10: 
        return '0' + str(num)
    else:
        return str(num)
    
if endSec - curSec < 0:
    restSec = convertToStrWithZero(60 + endSec - curSec);
    endMin -= 1;
else:
    restSec = convertToStrWithZero(endSec - curSec);

if endMin - curMin < 0:
    restMin = convertToStrWithZero(60 + endMin - curMin);
    endHour -= 1;
else:
    restMin = convertToStrWithZero(endMin - curMin);
    
if endHour - curHour < 0:
    restHour = convertToStrWithZero(24 + endHour - curHour);
else:
    restHour = convertToStrWithZero(endHour - curHour);
    
print(restHour + ":" + restMin + ":" + restSec);
