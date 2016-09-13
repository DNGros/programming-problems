from sys import stdin, stdout
import copy
testCases = int(raw_input())
from collections import deque
class bird():
    def __init__(self, home, left, right):
        self.home = home
        self.left = left
        self.right = right
        self.curLoc = home
        self.movedThisTurn = 0

    def distLeft(self):
        if self.left is None:
            return 9999
        return abs(self.left.curLoc - self.curLoc)

    def distRight(self):
        if self.right is None:
            return 9999
        return abs(self.right.curLoc - self.curLoc)

    def isHappy(self):
        return self.distRight() > 1 and self.distLeft() > 1

def allHappy(nowBirds):
    for b in nowBirds:
        if not b.isHappy():
            return False
    return True

for case in range(testCases):
    numbirds = int(raw_input())
    birdpos = map(int,stdin.readline().rstrip().split())
    birdpos.sort()

    nowbirds = []
    lastbird = None
    for b in birdpos:
        b = bird(b, lastbird, None)
        if lastbird is not None:
            lastbird.right = b
        lastbird = b
        nowbirds.append(b)
     
    moves = 0
    while not allHappy(nowbirds):
        newBirds = copy.deepcopy(nowbirds)
        for nB, oB in zip(newBirds, nowbirds):
            if not oB.isHappy():
                if oB.distLeft() == 1 and oB.distRight() == 1: 
                    continue
                elif oB.distLeft() == 1:
                    nB.curLoc += 1
                else:
                    nB.curLoc -= 1
        nowbirds = newBirds 
        for p in range(3):
            newBirds = copy.deepcopy(nowbirds)
            for nB,oB in zip(newBirds, nowbirds):
                if oB.distLeft == 0:
                    nB.curLoc += 1
                if oB.distRight == 0:
                    nB.curLoc -= 1
                    
            nowbirds = newBirds 


    print max([abs(b.curLoc - b.home) for b in nowbirds])




    






    

    
