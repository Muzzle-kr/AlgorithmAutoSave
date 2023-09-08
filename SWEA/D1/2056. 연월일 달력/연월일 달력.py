date_dict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10:31,
    11:30,
    12:31
}

for t in range(1, int(input())+1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    
    if int(month) > 12 or int(month) < 1:
        print(f'#{t} -1')
        continue
    
    if int(day) > date_dict[int(month)] or int(day) < 1:
        print(f'#{t} -1')
        continue
    
    print(f'#{t} {year}/{month}/{day}')