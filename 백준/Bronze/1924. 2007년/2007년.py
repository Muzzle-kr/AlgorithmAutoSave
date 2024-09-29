month, day = map(int, input().split())
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEK = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

days = sum(month_days[:month])
print(WEEK[(days + day) % 7])