from sys import stdin, stdout
from heapq import heappush, heappop, heapify
import math
testCases = int(raw_input())
for case in range(testCases):
    paramsV = stdin.readline().rstrip().split()
    ns = int(paramsV[0]);
    print ns(ns-1)/2
