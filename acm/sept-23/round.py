for case in range(int(raw_input())):
    n = int(raw_input())
    rounder = 10
    dig = -1
    while n > rounder:
        n = round(n, dig)
        rounder *= 10
        dig -= 1
    print int(n)
