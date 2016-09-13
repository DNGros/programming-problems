from collections import namedtuple
for case in range(int(raw_input())):
    planetCount, wormCount = map(int, raw_input().rstrip().split())
    dist = [0] + [9e9]*(planetCount-1) # planet 1 source
    WormHole = namedtuple("WormHole", ["source","dest","cost"])
    wormHoles = [WormHole(*map(int, raw_input().split())) for w in range(wormCount)]
    
    for i in range(wormCount - 1):
        for w in wormHoles:
            dist[w.dest-1] = min([dist[w.dest-1], dist[w.source-1] + w.cost])

    for w in wormHoles:
        if dist[w.source-1] + w.cost < dist[w.dest-1]:
            print "UNSAFE AT ANY SPEED"
            break
    else:
        print " ".join([str(x) if x != 9e9 else "OUT" for x in dist])
