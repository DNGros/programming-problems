from collections import namedtuple
cases = int(raw_input())
for c in range(cases):
    planetCount, wormCount = map(int, raw_input().split())
    dist = [0] + [9e9]*(planetCount-1) # planet 1 source
    wormHoles = []
    WormHole = namedtuple("WormHole", ["source","dest","cost"])
    for w in range(wormCount):
        wormHoles.append(WormHole( *map(int, raw_input().split() )))
    
    for i in range(wormCount - 1):
        for w in wormHoles:
            dist[w.dest-1] = min([dist[w.dest-1], dist[w.source-1] + w.cost])

    for w in wormHoles:
        if dist[w.source-1] + w.cost < dist[w.dest-1]:
            print "UNSAFE AT ANY SPEED"
            raise SystemExit

    print " ".join([str(x) if x != 9e9 else "OUT" for x in dist])

