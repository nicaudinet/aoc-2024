import copy
from collections import defaultdict

with open("input11.txt", "r") as file:
    contents = file.read()

def update_stone(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        num = str(num)
        half = len(num) // 2
        left = num[:half]
        right = num[half:]
        assert len(left) + len(right) == len(num)
        return [int(left), int(right)]
    else:
        return [2024 * num]

def blink(stones):
    new_stones = []
    for s in [update_stone(stone) for stone in stones]:
        new_stones += s
    return new_stones

init_stones = [int(num) for num in contents.strip().split(" ")]
stones = copy.copy(init_stones)
for _ in range(25):
    stones = blink(stones)
part1 = len(stones)
print(part1)

###

def blink_fast(counts):
    new_counts = defaultdict(lambda: 0)
    for num, count in counts.items():
        if num == 0:
            new_counts[1] += count
        elif len(str(num)) % 2 == 0:
            num = str(num)
            half = len(num) // 2
            left = int(num[:half])
            right = int(num[half:])
            new_counts[left] += count
            new_counts[right] += count
        else:
            num = 2024 * num
            new_counts[num] += count
    return new_counts

counts = {stone: 1 for stone in init_stones}
for _ in range(75):
    counts = blink_fast(counts)
part2 = sum(counts.values())
print(part2)
