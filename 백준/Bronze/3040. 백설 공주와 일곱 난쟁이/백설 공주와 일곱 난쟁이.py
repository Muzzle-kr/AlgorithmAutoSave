result = []
dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
    
# 오름차순 정렬
dwarf.sort(reverse=True)

sumOfHeights = sum(dwarf)

targetSum = sumOfHeights - 100
catchDwarf = []
for i in range(8):
    for j in range(i+1, 9):
        if dwarf[i] + dwarf[j] == targetSum:
            catchDwarf.append(dwarf[i])
            catchDwarf.append(dwarf[j])

for i in dwarf:
    if i not in catchDwarf:
        print(i)