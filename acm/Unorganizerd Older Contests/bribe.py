from sys import stdin, stdout

testCases = int(raw_input())
for case in range(testCases):
    params = stdin.readline().rstrip().split()
    bagsCount = int(params[0])
    TACount = int(params[1])
    bags =[]
    for b in range(bagsCount):
        bags.append([int(x) for x in stdin.readline().rstrip().split()])
    TAs =[]
    for t in range(TACount):
        TAs.append(stdin.readline().rstrip().split())
    
    happyTAs = []
    for ta in TAs:
        for tryBag in bags:
            thisHappy = 0
            for i in range(2,6):
                thisHappy += tryBag[i-2]*int(ta[i])
            if thisHappy >= int(ta[1]):
                happyTAs.append(ta[0])
                break;
    print ' '.join(sorted(happyTAs))
