#!/usr/bin/env python3
import math

with open('./input.txt') as input:
    lines = input.readlines()

raws: list[str] = [line.strip() for line in lines]
print(raws)

ranges: list[tuple[int, int]] = []

for r in raws:
    x_and_ys = r.split(',')
    for x_y in x_and_ys:
        if len(x_y) > 2:
            x, y = x_y.split('-')
            if x and y:
                ranges.append((int(x), int(y)))


summe = 0
two = 0
for ids in ranges:
    first, last = ids
    while first <= last:
        length = len(str(first))
        if length % 2 == 0:
            exponent = 10**(length / 2)
            last_digits = first % exponent
            first_digits = (first - last_digits) / exponent
            if last_digits == first_digits:
                summe = summe + first

        max_length = math.floor(length / 2)
        pattern_length = 1
        while pattern_length <= max_length:
            string = str(first)
            elements = []
            while len(string) >= pattern_length:
                elements.append(string[0:pattern_length])
                string = string[pattern_length:]
            if len(string) == 0 and len(set(elements)) == 1:
                two = two + first
                break
            pattern_length = pattern_length + 1
        first = first + 1


print('part one:', summe)
print('part two:', two)
