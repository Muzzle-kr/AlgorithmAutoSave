# 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayOfWeek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
month, day = map(int, input().split())

if month == 1:
    print(dayOfWeek[day % 7 - 1])
else:
    days = sum(monthDays[0:month-1]) + day
    print(dayOfWeek[days % 7 - 1])  