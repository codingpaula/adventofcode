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

print(fresh)


total = 0
for start, end in ranges:
    total = end - start + 1

print(total)
