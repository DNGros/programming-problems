from sys import stdin, stdout, setrecursionlimit
from bisect import bisect_left, bisect
#setrecursionlimit(1500)


def findNumNextE(event):
    
    #thisEventEnd = eventByStart[startI][2]
    startAfterIEndIndex = bisect_left(eBE, event[2]) + 1
    print event, startAfterIEndIndex
    afterMe = 0
    if startAfterIEndIndex == eventCount:
        #No next event found
        return afterMe;
    print eventByStart[startAfterIEndIndex:eventCount]
    #loop through everthing after end time and check
    return (eventCount-startAfterIEndIndex + 1) + \
        sum(map(findNumNextE, eventByStart[startAfterIEndIndex:eventCount]))

testCases = int(raw_input())
for case in range(testCases):
    param = [int(x) for x in stdin.readline().rstrip().split()]
    eventCount = param[0]
    eventT = [int(x) for x in stdin.readline().rstrip().split()]
    eventByIndex = [(i, eventT[i*2],eventT[i*2]+eventT[i*2+1]) for i in range(eventCount)]
    eventByIndex.sort(key=lambda tup: tup[0]) 
    eventByStart = sorted(eventByIndex, key=lambda tup: tup[1])
    eventByEnd = sorted(eventByIndex, key=lambda tup: tup[2])
    eBE = [tup[2] for tup in eventByEnd]
    print eventByIndex
    print eventByStart
    print eventByEnd
    for er in eventByStart:
        print "-- ", er
        print findNumNextE(er)
    print max(map(findNumNextE,))
