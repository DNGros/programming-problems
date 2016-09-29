from bisect import bisect_left
for case in range(int(raw_input())):
    rockCount = int(raw_input())
    myRocks = map(int, raw_input().split())
    myRocks.sort()
    oponRocks = map(int, raw_input().split())
    totalLosses = 0
    for opR in oponRocks:
        # find the index of my smallest rock that greater than or equal
        i = bisect_left(myRocks, opR)
        if i == len(myRocks):
            # I don't have rock big enough, so play smallest
            i = 0
            totalLosses += myRocks[0]
        # Note: the delete operation on a list is actually really expensive. The 
        # alternative efficient solution is a self balancing tree, but unfortunately
        # there's no built-in for that, and given the small input size (N <= 10000), 
        # writing one by hand just didnt seem worth it....
        del  myRocks[i] 
    print totalLosses
