for case in range(int(raw_input())):
    plotsPoints = []
    for plot in range(int(raw_input())):
        points = set()
        for p in range(int(raw_input())):
            x, y = map(int, raw_input().split())
            points.add(x);
        plotsPoints.append(len(points))
    cumXor = 0
    for p in plotsPoints:
        cumXor = cumXor ^ p
    if cumXor:
        print "SCOTT"
    else:
        print "JARED"
