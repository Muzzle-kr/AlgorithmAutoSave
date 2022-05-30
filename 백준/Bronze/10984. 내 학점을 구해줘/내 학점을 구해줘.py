num = int(input())

for i in range(num):
  repeat = int(input())
  sumOfGrade = 0;
  totalSum = 0;
  for j in range(repeat):
    grade, gpa = input().split()
    grade = int(grade)
    gpa = float(gpa)
    sumOfGpa = grade * gpa
    sumOfGrade += grade 
    totalSum += sumOfGpa
  print(sumOfGrade, round((totalSum / sumOfGrade), 1))