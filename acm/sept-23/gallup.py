for case in range(int(raw_input())):
    qs = []
    satCount = 0
    for q in range(int(raw_input())):
        skip, needed = map(int, raw_input().split())    
        qs.append([skip, needed])
    neededToSat = [skip*needed for skip, needed in qs]
    haveToGetTo = max(neededToSat)
    realCounts = [haveToGetTo / skip for skip, needed in qs] 
    print sum(realCounts)
