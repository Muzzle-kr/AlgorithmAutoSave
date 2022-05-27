num = int(input());

max = 0;
oldboy = '';
min = 99999999;
youngboy = '';
for _ in range(num):
    name, day, month, year = input().split();
    day = int(day);
    month = int(month);
    year = int(year);
    
    sum = day + (month * 30) + (year * 365)
    if sum > max:
        max = sum;
        youngboy = name;
    
    if sum < min:
        min = sum;
        oldboy = name;

print(youngboy);
print(oldboy);