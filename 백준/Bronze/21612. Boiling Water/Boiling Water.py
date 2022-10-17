degree = int(input())
resultDegree = degree * 5 - 400

print(resultDegree)

if resultDegree > 100:
    print(-1)
elif resultDegree < 100:
    print(1)    
else:
    print(0)