num = int(input())
n1, n2, n3, n4, n5 = map(int, input().split());
notToDrive = 0;

if n1 == num: notToDrive += 1;
if n2 == num: notToDrive += 1;
if n3 == num: notToDrive += 1;
if n4 == num: notToDrive += 1;
if n5 == num: notToDrive += 1;

print(notToDrive);