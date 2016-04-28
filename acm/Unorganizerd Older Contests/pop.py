from sys import stdin, stdout

testCases = int(raw_input())
for case in range(testCases):
    param = [int(x) for x in stdin.readline().rstrip().split()]
    stateCount = param[0]
    docCount= param[1]
    pops = [int(x) for x in stdin.readline().rstrip().split()]
    for sI in range(docCount):
        SP = [int(x) for x in stdin.readline().rstrip().split()]
        pops[SP[0]-1] += SP[1]
    print ' '.join(map(str,pops));

