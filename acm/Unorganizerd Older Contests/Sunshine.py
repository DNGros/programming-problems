from sys import stdin, stdout

testCases = int(raw_input())
for case in range(testCases):
    counts = stdin.readline().rstrip().split()
    emotions = stdin.readline().rstrip().split()
    out = "YES"
    if "EXHAUSTED" in emotions:
        out = "NO"
    if "SAD" in emotions and not ("HAPPY" in emotions or "ANGRY" in emotions):
        out = "NO"
    if "SAD" in emotions and "CALM" in emotions:
        out = "NO"
    print out
