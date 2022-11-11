import math
from copy import deepcopy
from itertools import combinations, permutations

N = int(input())
player = [i for i in range(N)]

arr = []

for i in range(N):
    tmpArr = list(map(int, input().split()))
    arr.append(tmpArr)

# 팀 차이 저장 배열
diffArr = []

combination = combinations(player, math.ceil(N/2))

for teamA in combination:
    teamB = deepcopy(player)
    for i in range(len(teamA)):
        teamB.remove(teamA[i])

    
    TeamAPermutation = permutations(teamA, 2)
    TeamBPermutation = permutations(teamB, 2)
    
    aTeamSynergy = 0
    bTeamSynergy = 0
    
    for pa in TeamAPermutation:
        aTeamSynergy += arr[pa[0]][pa[1]]
        
    for pb in TeamBPermutation:
        bTeamSynergy += arr[pb[0]][pb[1]]
        
    largeSynergy = max(aTeamSynergy, bTeamSynergy)
    smallSynergy = min(aTeamSynergy, bTeamSynergy)
    
    diffArr.append(largeSynergy - smallSynergy)

print(min(diffArr))
