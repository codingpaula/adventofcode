#!/usr/bin/env python3


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
for ids in ranges:
    first, last = ids
    print(f'checking from {first} to {last}')
    while first <= last:
        length = len(str(first))
        if length % 2 == 0:
            exponent = 10**(length / 2)
            last_digits = first % exponent
            first_digits = (first - last_digits) / exponent
            if last_digits == first_digits:
                print('found one:', first)
                summe = summe + first
        first = first + 1

print(ranges)
print(summe)
