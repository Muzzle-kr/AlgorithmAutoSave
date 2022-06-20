numOfProblems = int(input())
problems = map(int, input().split());

sum = 0;
previous = 0;
for i in problems:
    if i != 0:
        previous += 1
        sum += previous
    else: 
        previous = 0

print(sum)