from copy import copy
from itertools import pairwise 

with open("input02.txt", "r") as file:
    contents = file.read()

reports = [[int(level) for level in line.split(" ")] for line in contents.splitlines()]

def safe(report):
    inc = sorted(report)
    increasing = report == inc
    dec = sorted(report, reverse=True)
    decreasing = report == dec
    distance = all(1 <= abs(a-b) <= 3 for (a,b) in pairwise(report))
    return (increasing or decreasing) and distance

part1 = len(list(report for report in reports if safe(report)))
print(part1)

###

def safe_pd(report):
    safes = [safe(report)]
    for i in range(len(report)):
        rep = copy(report)
        del rep[i]
        safes.append(safe(rep))
    return any(safes)

part2 = len(list(report for report in reports if safe_pd(report)))
print(part2)
