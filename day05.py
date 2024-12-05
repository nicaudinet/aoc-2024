import ast
from math import floor

with open("input05.txt", "r") as file:
    contents = file.read()

ruleLines, updateLines = contents.split("\n\n")

rules = []
for line in ruleLines.splitlines():
    left, right = line.split("|")
    rules.append((int(left), int(right)))

updates = [list(ast.literal_eval(line)) for line in updateLines.splitlines()]

def is_correct(update):
    for i, page in enumerate(update):
        for pre, post in rules:
            if page == pre and post in update[:i+1]:
                return False
    return True

part1 = 0
for update in updates:
    if is_correct(update):
        middle = update[floor(len(update) / 2)]
        part1 += middle
print(part1)

###

def fix(update):
    while not is_correct(update):
        for i, page in enumerate(update):
            for pre, post in rules:
                if page == pre and post in update[:i+1]:
                    j = update[:i+1].index(post)
                    update = update[:j] + [update[i]] + update[j:i] + update[i+1:]
                    # print(update)
                    break
    return update

part2 = 0
for update in updates:
    if not is_correct(update):
        update = fix(update)
        middle = update[floor(len(update) / 2)]
        part2 += middle
print(part2)
