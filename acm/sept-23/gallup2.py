for case in range(int(raw_input())):
    qs = []
    satCount = 0
    for q in range(int(raw_input())):
        skip, needed = map(int, raw_input().split())    
        qs.append([skip, needed, 0])
    quesAsked = 0
    persNum = 0
    while satCount < len(qs):
        persNum += 1
        for i, q in enumerate(qs):
            if persNum % q[0] == 0:
                q[2] += 1
                quesAsked += 1
                if q[2] == q[1]:
                    satCount += 1
    print quesAsked
