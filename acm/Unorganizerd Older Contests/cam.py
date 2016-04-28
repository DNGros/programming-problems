from sys import stdin, stdout

def spread(r, c):
    if(r >= rCount or c >= cCount or r < 0 or c < 0 or blocks[r][c] == 0):
        return 0
    out = blocks[r][c];
    blocks[r][c] = 0;
    out += spread(r-1,c-1)
    out += spread(r-1,c)
    out += spread(r-1,c+1)
    out += spread(r,c-1)
    out += spread(r,c+1)
    out += spread(r+1,c-1)
    out += spread(r+1,c)
    out += spread(r+1,c+1)
    return out

testCases = int(raw_input())
for case in range(testCases):
    param = [int(x) for x in stdin.readline().rstrip().split()]
    rCount = param[0]
    cCount = param[1]
    if(rCount != 0 and cCount != 0):
        start = [int(x) for x in stdin.readline().rstrip().split()]
        blocks = []
        for r in range(rCount):
            blocks.append([int(x) for x in stdin.readline().rstrip().split()])
        stdout.write(str(spread(start[0], start[1])))
        stdout.write("\n")
    else:
        stdout.write("0\n")
