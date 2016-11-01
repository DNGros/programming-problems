coinTypes = [1, 5, 10, 25]
for case in range(int(raw_input())):
    coinVal = [0] * (int(raw_input()) + 1)
    coinVal[0] = 1
    # handle the zero case
    if len(coinVal) == 1:
        print 1
        continue
    for val, _ in enumerate(coinVal):
        for coin in coinTypes:
            if val - coin >= 0:
                coinVal[val] += coinVal[val-coin]
    print int(coinVal[-1] % (1e9 + 7))
