from sys import stdin, stdout
import copy
testCases = int(raw_input())
from collections import deque
import math

for case in range(testCases):
    fCount, pX, pY = map(int,raw_input().split())
    startX = [] 
    startY = []
    for f in range(fCount):
        x, y = map(int, raw_input().split())
        startX.append(x)
        startY.append(y)
    avgX = float(sum(startX)) / float(len(startX))
    avgY = float(sum(startY)) / float(len(startY))

    avgX = (avgX + pX*fCount)/(fCount +1)
    avgY = (avgY + pY*fCount)/(fCount +1)
    if pX < avgX:
        avgX = math.floor(avgX)
    elif pX > avgX:
        avgX = math.ceil(avgX)

    
    if pY < avgY:
        avgY = math.floor(avgY)
    elif pY > avgY:
        avgY = math.ceil(avgY)
    print int(avgX), int(avgY)
