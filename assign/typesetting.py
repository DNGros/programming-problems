from collections import Counter

for case in range(int(raw_input())):
    distinctChars, height = map(int, raw_input().split())

    # Parse and store all the widths
    widths = dict()
    for c in range(distinctChars):
        char, w = raw_input().split()
        widths[char] = int(w)

    # parse other inputs    
    boxW, boxH = map(int, raw_input().split())
    line = raw_input()

    # Binary search possible widths
    maxS = boxH/height # Aproximate starting point
    minS = 0
    while maxS != minS:
        curS = (maxS+minS)/2 + 1
        # Layout line based off of this size 
        numLines = boxH/(curS*height)
        linesNeeded = 1
        spaceUsedOnThisLine = 0
        for char in line:
            spaceUsedOnThisLine += widths[char]*curS
            if spaceUsedOnThisLine > boxW:
                linesNeeded += 1
                spaceUsedOnThisLine = 0
        # Adjust bounds based off of current sizes 
        if linesNeeded > numLines:
            maxS = curS - 1
        elif linesNeeded < numLines or spaceUsedOnThisLine < boxW:
            minS = curS
        else: # spot on
            minS, maxS  = curS, curS
    print minS

