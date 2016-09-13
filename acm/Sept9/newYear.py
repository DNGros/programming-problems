from sys import stdin, stdout
import copy
testCases = int(raw_input())
from collections import deque

class airport():
    def __init__(self):
        self.connections = []
        self.distForK = 9e9
        self.distForS = 9e9

for case in range(testCases):
    numAirports, numFlights = map(int,raw_input().split())
    # search for K
    q = deque()


    
