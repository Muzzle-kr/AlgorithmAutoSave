dictOfLastName = {}

for i in range(int(input())):
    lastName = input()[0]    
    
    if lastName in dictOfLastName:
        dictOfLastName[lastName] += 1
    else:
        dictOfLastName[lastName] = 1
    

dictOfLastName = sorted(dictOfLastName.items())

result = ""

for key, value in dictOfLastName:
    if value >= 5:
        result += key

if result == "":
    print("PREDAJA")
else:
    print(result)
