from sys import stdin, stdout

testCases = int(raw_input())

for case in range(testCases):
    params = stdin.readline().rstrip().split()
    rCount = int(params[0])
    cCount = int(params[1])
    grid = []
    for r in range(rCount):
        te = [bool(x) for x in stdin.readline()]
        grid.append(te)
    maxN = 0
    for r in range(rCount):
        for c in range(cCount):
            n = 2
            #check rhombus
            v = 1
            while v == 1:
                for rR in range(rCount):
                    if v == 1:
                        for cR in range(cCount):
                            if abs(r-rR)+abs(c-cR) <= (n-1)/2:
                                if rR < 0 or rR >= rCount:
                                    v = 0
                                elif cR < 0 or cR >= cCount:
                                    v = 0
                                elif not grid[rR][cR]:
                                    v = 0           
                if v == 1:
                    if n > maxN:
                        maxN = n
                    n += 2
    print maxN
