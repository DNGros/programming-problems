from sys import stdin, stdout
testCases = int(raw_input())
for case in range(testCases):
    title = stdin.readline().rstrip()
    l = len(title.split())
    if l == 1:
        print title + " Returns"
    else:
        print title + ": Age of Darkness"
