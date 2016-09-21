from collections import namedtuple;
from heapq import heappush, heappop
vertCount, edgeCount = map(int,raw_input().split())
if edgeCount == 0:
    print -1
    raise SystemExit
sources = [None] * vertCount
Edge = namedtuple("Edge", ["dest", "cost"])
edges = [[] for x in range(vertCount)]
for e in range(edgeCount):
    s, d, c = map(int,raw_input().split())
    edges[s-1].append(Edge(d-1,c))
    edges[d-1].append(Edge(s-1,c))

q = []
heappush(q, (0, None, 0)) # source, dest, cost
while len(q) > 0:
    curCost, source, dest = heappop(q)
    if sources[dest] is not None:
        continue # already seen

    sources[dest] = source

    if dest == vertCount-1:
        path = []
        tbCur = dest
        while tbCur is not None:
            path.append(str(tbCur+1))
            tbCur = sources[tbCur]
        print " ".join(reversed(path))
        break;
                


    for e in edges[dest]:
        if sources[e.dest] is None and e.dest != 0:
            heappush(q, (curCost + e.cost, dest, e.dest))
else:
    print -1

