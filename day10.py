from itertools import product
import copy 

with open("input10.txt", "r") as file:
    contents = file.read()

# contents = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# """

def find_trailheads(tmap):
    trailheads = set()
    for i, j in product(range(len(tmap)), range(len(tmap[0]))):
        if tmap[i][j] == 0:
            trailheads.add((i,j))
    return trailheads

def in_bounds(tmap, coord):
    return 0 <= coord[0] < len(tmap) and 0 <= coord[1] < len(tmap[0])

def extend_trails(tmap, trails):
    new_trails = []
    for trail in trails:
        head = trail[-1]
        curr_height = tmap[head[0]][head[1]]
        if curr_height == 9:
            new_trails.append(trail)
        else:
            for n in [(1,0), (-1,0), (0,1), (0,-1)]:
                i = head[0] + n[0]
                j = head[1] + n[1]
                if in_bounds(tmap, (i,j)) and tmap[i][j] - curr_height == 1:
                    new_trail = copy.copy(trail)
                    new_trail.append((i,j))
                    new_trails.append(new_trail)
    return new_trails

def find_trails(tmap, trailhead):
    prev_trails = []
    trails = [[trailhead]]
    while prev_trails != trails:
        prev_trails = copy.copy(trails)
        trails = extend_trails(tmap, trails)
    return trails

def score_trailhead(tmap, trailhead):
    trails = find_trails(tmap, trailhead)
    return len(set(trail[-1] for trail in trails))

tmap = []
for line in contents.splitlines():
    tmap.append([int(c) for c in line])
trailheads = find_trailheads(tmap)
part1 = sum(score_trailhead(tmap, trailhead) for trailhead in trailheads)
print(part1)

###

part2 = sum(len(find_trails(tmap, trailhead)) for trailhead in trailheads)
print(part2)

