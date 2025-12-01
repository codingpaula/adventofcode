#!/usr/bin/env python3


with open('./input.txt') as input:
    lines = input.readlines()

raws: list[str] = [line.strip() for line in lines]
print(raws)

ranges: list[tuple[str, str]] = []

for r in raws:
    x_and_ys = r.split(',')
    for x_y in x_and_ys:
        if len(x_y) > 2:
            x, y = x_y.split('-')
            if x and y:
                ranges.append((x, y))


for ids in ranges:
    first, last = ids
print(ranges)
