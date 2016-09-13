from sys import stdin, stdout
testCases = int(raw_input())
from collections import deque
class FoundCount( Exception ):
        pass

for case in range(testCases):
    target, soothing, wingCount = map(int,stdin.readline().rstrip().split())
    wings = []
    for wing in range(wingCount):
        wings.append(int(stdin.readline()))
    q = deque()
    q.append((0,0)) #hottness, num of wings
    answer = None
    try:
        while(len(q) > 0):
            cur = q.popleft()
            #print "Cut ", cur
            if cur[0] == target:
                answer = cur[1]
                #print "FOUND ", answer
                raise FoundCount
            if cur[0] > target + soothing:
                continue
            sC = soothing
            while sC < max(wings):
                q.append((cur[0]-sC, cur[1]))
                sC += soothing
            for w in wings:
                #print "eat w", w, cur[1]+1
                q.append((cur[0]+w, cur[1]+1))
    except FoundCount:
        print answer





    

    
