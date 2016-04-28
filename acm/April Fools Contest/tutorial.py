from sys import stdin, stdout
from heapq import heappush, heappop, heapify
import math
testCases = int(raw_input())
for case in range(testCases):
    paramsV = stdin.readline().rstrip().split()
    rows = int(paramsV[0]);
    qCount = int(paramsV[1]);
    matrix = []
    #Load in
    for pi in range(rows):
        matrix.append([int(x) for x in stdin.readline().rstrip().split()]);
    #print pointList;
    for q in range(qCount):
        param = [int(x) for x in stdin.readline().rstrip().split()];
        print max([max(x[param[1]-1:param[3]]) for x in matrix[param[0]-1:param[2]]])
