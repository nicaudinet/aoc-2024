import re

with open("input03.txt", "r") as file:
    contents = file.read()

def sum_muls(str):
    muls = re.findall("mul\\(\\d+,\\d+\\)", str)
    muls = [re.findall("\\d+", m) for m in muls]
    return sum(int(a) * int(b) for a,b in muls)

part1 = sum_muls(contents)
print(part1)

###

donts = re.split("don't()", contents)
allowed = [donts[0]] + ["".join(re.split("do()", dont)[1:]) for dont in donts]
allowed = "".join(allowed)
part2 = sum_muls(allowed)
print(part2)
