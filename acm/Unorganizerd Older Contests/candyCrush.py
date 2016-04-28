from sys import stdin, stdout

testCases = int(raw_input())
for case in range(testCases):
    p = [int(x) for x in stdin.readline().rstrip().split()]
    steps = 0
    for i in range(3,6):
        while p[i] != p[i-3]:
            if p[i] < p[i-3]:
                steps += p[i-3]-p[i]
                break;
            elif p[i] % 2 == 0:
                p[i] = p[i]/2
                steps += 1
            else:
                p[i] = (p[i]+1)/2
                steps += 2
    print steps;
