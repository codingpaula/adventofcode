with open('./input.txt') as input:
    lines = input.readlines()

map: list[list[int]] = []
y = 0
for line in lines:
    x = 0
    map.append([])
    for elem in line.strip():
        map[y].append(1 if elem == '@' else 0)
        x = x+1
    y = y+1

# print(map)

schablone = [
    [-1, -1],
    [-1, 0],
    [0, -1],
    [1, 1],
    [1, 0],
    [0, 1],
    [-1, 1],
    [1, -1]
]

def identify_rolls(m: list[list[int]]) -> list[list[int]]:
    for y_ in range(0, y):
        for x_ in range(0, x):
            if m[y_][x_] == 0:
                continue
            count = 0
            for test in schablone:
                test_x = x_ + test[0]
                test_y = y_ + test[1]
                if test_x < 0 or test_y < 0 or test_x >= x or test_y >= y:
                    continue
                # print(test_x, test_y)
                if m[test_y][test_x] > 0:
                    count = count + 1

            if count < 4:
                m[y_][x_] = 2
    return m

def remove_rolls(m: list[list[int]]) -> tuple[list[list[int]], int]:
    removed = 0
    for y_ in range(0, y):
        for x_ in range(0, x):
            if m[y_][x_] == 2:
                m[y_][x_] = 0
                removed = removed + 1
    return m, removed

map = identify_rolls(map)
map, part_one = remove_rolls(map)

print('part one', part_one)

removed = part_one
total = part_one

while removed > 0:
    map = identify_rolls(map)
    map, removed = remove_rolls(map)
    print(removed)
    total = total + removed

print('part two', total)
