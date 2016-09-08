from collections import Counter
lc = int(raw_input())
if lc > 26:
    print -1
    raise SystemExit
word = raw_input()
counts = Counter(word)
print sum(c - 1 for l, c in counts.most_common())
