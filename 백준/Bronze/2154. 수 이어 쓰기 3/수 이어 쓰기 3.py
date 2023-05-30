ans = input()
string_number = "".join([str(i) for i in range(1, 100001)])

for i in range(len(string_number) - len(ans)+1):
    if string_number[i:i+len(ans)] == ans:
        print(i+1)
        break