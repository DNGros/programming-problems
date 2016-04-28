from sys import stdin, stdout
import math
testCases = int(raw_input())
def distance(p, oP):
    return math.sqrt((p[0]-oP[0])**2+(p[1]-oP[1])**2)

for case in range(testCases):
    numP = stdin.readline()
    pointsRaw = stdin.readline().rstrip().split()
    points = []
    for i in range(0,len(pointsRaw),2):
        points.append((int(pointsRaw[i]), int(pointsRaw[i+1])))

    minD = 9e9
    for i in range(0,len(points)):
        for oI in range(i+1,len(points)):
            dist = distance(points[i],points[oI])
            if dist < minD:
                minD = dist
    
    print "{0:.4f}".format(round(minD,4))
