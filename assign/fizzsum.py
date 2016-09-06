""" 
David Gros
Fizzsum - 9/7/16
"""
import fileinput
for case in [l.split() for l in fileinput.input()]:
    a, b = int(case[0]), int(case[1])
    vals = [x*x if x%15 == 0 else
            x+3 if x%3 == 0 else
            x+5 if x%5 == 0 else 0 for x in range(a, b+1)]
    print sum(vals)
