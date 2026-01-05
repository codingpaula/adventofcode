with open('./input.txt') as input:
    lines = input.readlines()


ranges: list[tuple[int, int]] = []
ingredients: list[int] = []

for line in lines:
    stripped = line.strip()
    if '-' in stripped:
        one, two = stripped.split('-')
        ranges.append((int(one), int(two)))
    elif len(stripped) > 0:
        ingredients.append(int(stripped))


fresh = 0
for ing in ingredients:
    for ran in ranges:
        start, end = ran
        if ing >= start and ing <= end:
            fresh = fresh + 1
            break

print('part one:', fresh)


sorting = sorted(ranges, key=lambda r: r[0])
cleaning = True

while cleaning:
    cleaning = False
    for i, ran in enumerate(sorting):
        if i == 0:
            continue
        previous = sorting[i-1]
        if previous[1] >= ran[1]:
            sorting[i] = previous
            cleaning = True
        elif previous[1] >= ran[0]:
            new_one = (previous[0], ran[1])
            sorting[i-1] = new_one
            sorting[i] = new_one
            cleaning = True
    sorting = sorted(list(set(sorting)), key=lambda r: r[0])

total = 0
for element in sorting:
    total = total + element[1] - element[0] + 1

print('part two:', total)
