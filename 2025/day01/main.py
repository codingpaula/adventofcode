#!/usr/bin/env python
import math

with open('./input.txt') as input:
    lines = input.readlines()

commands = [line.strip() for line in lines]
# commands = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

current = 50
result = 0
part_two = 0


for command in commands:
    amount = int(command[1:])

    new_full_current = (current - amount) \
        if command[0] == 'L' else (current + amount)

    new_current =

    if new_current > 99:
        if current == 0 or new_current % 100 == 0:
            rounds = math.floor(new_current / 100) - 1
        else:
            rounds = math.floor(new_current / 100)
        current = new_current % 100
        part_two = part_two + rounds
        print(current, ':', new_current, '> 99: +', rounds)
    elif new_current < 0:
        if current == 0 or new_current % 100 == 0:
            rounds = math.floor(new_current / 100) + 1
        else:
            rounds = math.floor(new_current / 100)
        current = (100 + new_current) % 100
        part_two = part_two - rounds
        print(current, ':', new_current, '< 0: +', -rounds)
    else:
        current = new_current

    if current == 0:
        result = result + 1

print(result)
print(result+part_two)
