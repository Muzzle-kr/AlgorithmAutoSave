from datetime import datetime

# 현재 날짜와 시간을 가져오기
current_datetime = datetime.now()
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day

print(str(year))
print(str(month).zfill(2))
print(str(day).zfill(2))