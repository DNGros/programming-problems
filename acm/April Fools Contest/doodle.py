from sys import stdin, stdout
from heapq import heappush, heappop, heapify
import math
testCases = int(raw_input())
for case in range(testCases):
    params = stdin.readline().rstrip().split()
    pointCount = int(params[0])
    pointList = []
    heapify(pointList)
    #Load in
    for pi in range(pointCount):
        point = [float(x) for x in stdin.readline().rstrip().split()];
        angle = math.atan2(point[1],point[0]);
        heappush(pointList, (ale, point[0], point[1]));
    longestDist = 0;
    
    pointList = sorted(pointList)
    #print pointList;
    for i in range(len(pointList)):
        xDif = pointList[i][1] - pointList[i-1][1]
        yDif = pointList[i][2] - pointList[i-1][2]
        dist = math.sqrt(xDif**2 + yDif**2)
        #print xDif, yDif, dist
        if dist > longestDist:
            longestDist = dist;
    print '%.3f' % longestDist;
