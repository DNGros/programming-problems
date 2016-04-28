from sys import stdin, stdout

testCases = int(raw_input())
for case in range(testCases):
    param = [int(x) for x in stdin.readline().rstrip().split()]
    stateCount = param[0]
    totalVoters = param[1]
    needToWin = param[2]
    idToCount = [0] * (stateCount+1)
    for sI in range(stateCount):
        SP = [int(x) for x in stdin.readline().rstrip().split()]
        idToCount[SP[0]] = SP[1]

    samVotes = [0] * (stateCount+1)
    angieVotes = [0] * (stateCount+1)
    samCollege = 0
    angieCollege = 0
    for vC in range(totalVoters):
        SP = stdin.readline().rstrip().split()
        if(SP[1] == "SAM"):
            samVotes[int(SP[0])] += 1
        elif SP[1] == "ANJIE":
            angieVotes[int(SP[0])] += 1
    for i, (sV, aV) in enumerate(zip(samVotes, angieVotes)):
        if sV > aV:
            samCollege += idToCount[i]
        elif aV < sV:
            angieCollege += idToCount[i]
    if samCollege > needToWin:
        print "SAM"
    elif needToWin < angieCollege:
        print "ANJIE"
    else:
        if sum(samVotes) > sum(angieVotes):
            print "SAM"
        elif sum(samVotes) < sum(angieVotes):
            print "ANJIE"
        else:
            print "TIE"
