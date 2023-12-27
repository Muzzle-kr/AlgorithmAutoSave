import sys
input = sys.stdin.readline

n = int(input())
student_marks = []

for _ in range(n):
    name, kor, eng, math = input().split()
    student_marks.append([name, int(kor), int(eng), int(math)])

student_marks.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student_info in student_marks:
    print(student_info[0])