import itertools

with open("input07.txt", "r") as file:
    lines = file.read().splitlines()

# content = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """
# lines = content.splitlines()

def parse_line(line):
    goal, rest = line.split(': ')
    terms = list(map(int, rest.split(' ')))
    return int(goal), terms

def eval(terms, ops):
    accum = terms[0]
    for op, term in zip(ops, terms[1:]):
        if op == 0:
            accum += term
        else:
            accum *= term
    return accum

def valid(goal, terms):
    for ops in itertools.product(range(2), repeat=len(terms)-1):
        if eval(terms, ops) == goal:
            return True
    return False

total = 0
for line in lines:
    goal, terms = parse_line(line)
    if valid(goal, terms):
        total += goal
part1 = total
print(part1)

###

def eval2(terms, ops):
    accum = terms[0]
    for op, term in zip(ops, terms[1:]):
        if op == 0:
            accum += term
        elif op == 1:
            accum *= term
        else:
            accum = int(str(accum) + str(term))
    return accum

def valid2(goal, terms):
    for ops in itertools.product(range(3), repeat=len(terms)-1):
        if eval2(terms, ops) == goal:
            return True
    return False

total = 0
for line in lines:
    goal, terms = parse_line(line)
    if valid2(goal, terms):
        total += goal
part2 = total
print(part2)
