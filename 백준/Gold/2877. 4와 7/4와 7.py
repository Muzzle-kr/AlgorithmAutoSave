arr = [4, 7]

binary = format(int(input())+1, 'b')
ans = ""
for b in binary[1:]:
    if b == '0':
        ans += '4'
    else:
        ans += '7'
print(ans)