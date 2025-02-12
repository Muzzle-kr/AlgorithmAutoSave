from itertools import permutations
n = int(input())

numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
operators_list = []
for op in range(4):
    for _ in range(operators[op]):
        operators_list.append(op)

permutations_list = list(permutations(operators_list, len(operators_list)))


def calculate(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2


min_answer = float('inf')
max_answer = -float('inf')

for perm_operators in permutations_list:
    temp_answer = numbers[0]
    for i in range(1, len(numbers)):
        temp_answer = calculate(temp_answer, numbers[i], perm_operators[i - 1])
    min_answer = min(min_answer, temp_answer)
    max_answer = max(max_answer, temp_answer)

print(max_answer)
print(min_answer)