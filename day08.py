from itertools import product

with open("input08.txt", "r") as file:
    grid = list(map(list, file.read().splitlines()))

# test = """......#....#
# ...#....0...
# ....#0....#.
# ..#....0....
# ....0....#..
# .#....A.....
# ...#........
# #......#....
# ........A...
# .........A..
# ..........#.
# ..........#.
# """
# grid = list(map(list, test.splitlines()))

def find_antennas(grid):
    antennas = {}
    for i, j in product(range(len(grid)), range(len(grid[0]))):
        char = grid[i][j]
        if char in antennas:
            antennas[char].append((i,j))
        elif char.isdigit() or char.isalpha():
            antennas[char] = [(i,j)]
    return antennas

def in_bounds(coord):
    i, j = coord
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def find_antinodes(antennas):
    antinodes = []
    pairs = [(i,j) for i, j in product(antennas, repeat=2) if i != j]
    for a1, a2 in pairs:
        node1 = (a1[0] - (a2[0] - a1[0]), (a1[1] - (a2[1] - a1[1])))
        node2 = (a2[0] - (a1[0] - a2[0]), (a2[1] - (a1[1] - a2[1])))
        antinodes += [node1, node2]
    return antinodes

antennas = find_antennas(grid)
antinodes = set()
for _, locs in antennas.items():
    antinodes |= set(find_antinodes(locs))
antinodes = [coord for coord in antinodes if in_bounds(coord)]
part1 = len(antinodes)
print(part1)

###

def find_antinodes2(antennas):
    antinodes = []
    pairs = [(i,j) for i, j in product(antennas, repeat=2) if i != j]
    for a1, a2 in pairs:

        dx = a2[0] - a1[0]
        dy = a2[1] - a1[1]
        x, y = a1
        while in_bounds((x,y)):
            antinodes.append((x,y))
            x = x - dx
            y = y - dy

        dx = a1[0] - a2[0]
        dy = a1[1] - a2[1]
        x, y = a2
        while in_bounds((x,y)):
            antinodes.append((x,y))
            x = x - dx
            y = y - dy

    return antinodes

antennas = find_antennas(grid)
antinodes = set()
for _, locs in antennas.items():
    antinodes |= set(find_antinodes2(locs))
antinodes = [coord for coord in antinodes if in_bounds(coord)]
part2 = len(antinodes)
print(part2)
