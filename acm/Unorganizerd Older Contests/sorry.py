from collections import Counter
from sys import stdin, stdout
import re

testCases = int(raw_input())
for case in range(testCases):
    param = [int(x) for x in stdin.readline().rstrip().split()]
    wordsUsed = param[0]
    timesNeeded = param[1]
    lines = param[2]
    lyr = []
    for i in range(lines):
        new = [str(x).lower() for x in stdin.readline().rstrip().split()]
        regex = re.compile('[^a-z]')
        #First parameter is the replacement, second parameter is your input string
        new = [regex.sub('', x) for x in new]
        lyr = lyr + new
    coun = Counter(lyr)
    foundInLim = 0;
    for w in coun:
        if(w != '' and coun[w] >= timesNeeded):
            foundInLim += 1
    if(foundInLim >= timesNeeded):
        print "WRITE"
    else:
        print "LET IT GO"
