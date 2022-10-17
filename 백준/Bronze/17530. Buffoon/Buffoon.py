resultOfVote = []

for _ in range(int(input())):
    resultOfVote.append(int(input()))
    
if resultOfVote[0] == max(resultOfVote):
    print("S")
else:
    print("N")