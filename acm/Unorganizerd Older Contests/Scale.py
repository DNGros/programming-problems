from sys import stdin, stdout

testCases = int(raw_input())
for case in range(testCases):
    counts = stdin.readline().rstrip().split()
    souls = [int(x) for x in stdin.readline().rstrip().split()]
    souls.sort();
    happy = 0;
    pSum = 0;
    for pi in range(len(souls)):
        if(pSum <= souls[pi]):
            happy += 1
        pSum += souls[pi]
    print happy
