calendar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, D, Y, T = input().split()
tot_day = 365

# 윤년 처리
if int(Y) % 400 == 0 or (int(Y) % 4 == 0 and int(Y) % 100 != 0):
    day[1] = 29
    tot_day += 1
    
tot_time = tot_day * 24 * 60
D = D.split(",")[0]
H, M = map(int, T.split(':'))
current_time = sum([day[i] for i in range(calendar.index(month))]) * 24 * 60 + ((int(D)-1) * 24 * 60) + H * 60 + M

print(current_time / tot_time * 100)