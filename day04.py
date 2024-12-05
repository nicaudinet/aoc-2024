with open("input04.txt", "r") as file:
    grid = list(map(list, file.read().splitlines()))

# grid = """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """
# grid = list(map(list, grid.splitlines()))[1:]
# print(grid)

def find_locations(grid, c):
    return [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == c]

def check_direction(loc, direction, grid):
    for c, (i, j) in zip("XMAS", direction):
        ii, jj = loc[0] + i, loc[1] + j
        rows = len(grid)
        cols = len(grid[0])
        if ii < 0 or jj < 0 or rows <= ii or cols <= jj or grid[ii][jj] != c:
            return False
    return loc

directions = [
    [(0,0), (1,0), (2,0), (3,0) ],
    [(0,0), (1,1), (2,2), (3,3) ],
    [(0,0), (0,1), (0,2), (0,3) ],
    [(0,0), (-1,1), (-2,2), (-3,3) ],
    [(0,0), (1,-1), (2,-2), (3,-3) ],
    [(0,0), (-1,-1), (-2,-2), (-3,-3) ],
    [(0,0), (-1,0), (-2,0), (-3,0) ],
    [(0,0), (0,-1), (0,-2), (0,-3) ]
]

count = 0
for location in find_locations(grid, 'X'):
    for direction in directions:
        if check_direction(location, direction, grid):
            count += 1
part1 = count
print(part1)

###

diag1 = [
    [(1,1), (-1,-1)],
    [(-1,-1), (1,1)],
]

diag2 = [
    [(-1,1), (1,-1)],
    [(1,-1), (-1,1)],
]

def check_direction(loc, direction, grid):
    for c, (i, j) in zip("MS", direction):
        ii, jj = loc[0] + i, loc[1] + j
        rows = len(grid)
        cols = len(grid[0])
        if ii < 0 or jj < 0 or rows <= ii or cols <= jj or grid[ii][jj] != c:
            return False
    return loc

count = 0
for location in find_locations(grid, 'A'):
    d1 = any(check_direction(location, d, grid) for d in diag1)
    d2 = any(check_direction(location, d, grid) for d in diag2)
    if d1 and d2:
        count += 1
part2 = count
print(part2)
