with open("input01.txt", "r") as file:
    contents = file.read()

list_A = []
list_B = []
for line in contents.splitlines():
    a, b = line.split("   ")
    list_A.append(int(a))
    list_B.append(int(b))

list_A.sort()
list_B.sort()

part1 = sum(abs(a - b) for a, b in zip(list_A, list_B))
print(part1)

###

counts = {a: list_B.count(a) for a in set(list_A)}
part2 = sum(a * counts[a] for a in list_A)
print(part2)
