from sys import stdin, stdout

testCases = int(raw_input())
for case in range(testCases):
    params = stdin.readline().rstrip().split()
    word = params[0]
    shift = int(params[1])
    out = ""
    for l in word:
        orig = ord(l);
        orig += shift%26
        if(orig > ord('Z')):
            orig = ord('A')+(orig-ord('Z'))-1
        out += chr(orig)
    print out;
