from sys import stdin, stdout

testCases = int(raw_input())
for case in range(testCases):
    param = [int(x) for x in stdin.readline().rstrip().split()]
    cupCount = param[0]
    commandCount = param[1]
    keyLoc = param[2]
    for pC in range(commandCount):
        thisCommand = stdin.readline().rstrip().split();
        if thisCommand[0] == "REVERSE":
            keyLoc = cupCount - 1 - keyLoc;
        elif int(thisCommand[1]) == keyLoc:
            keyLoc = int(thisCommand[2])
        elif int(thisCommand[2]) == keyLoc:
            keyLoc = int(thisCommand[1])
    print keyLoc;
