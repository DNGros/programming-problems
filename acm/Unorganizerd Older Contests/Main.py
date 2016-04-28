from sys import stdin, stdout
testCases = int(raw_input())
for case in range(testCases):
    param = [int(x) for x in stdin.readline().rstrip().split()]
    plats = param[0]
    baller = param[1]
    prices = [int(x) for x in stdin.readline().rstrip().split()]
    uses = [int(x) for x in stdin.readline().rstrip().split()]
    mony = 0;
    for i in range(len(uses)):
        mony += prices[i]*uses[i]
    if(mony >= baller):
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
