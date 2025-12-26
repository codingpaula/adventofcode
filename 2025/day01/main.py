#!/usr/bin/env python

with open('./input.txt') as input:
    lines = input.readlines()

commands = [line.strip() for line in lines]

current = 50
result = 0
part_two = 0


for command in commands:
    amount = int(command[1:])

    while amount > 0:
        if command[0] == 'L':
            current = current - 1
            if current == -1:
                current = 99
        else:
            current = current + 1
            if current == 100:
                current = 0

        if current == 0:
            part_two = part_two + 1
        amount = amount - 1

print('part_two', part_two)


current = 50
for command in commands:
    amount = int(command[1:])
    new_current = (current - amount) \
        if command[0] == 'L' else (current + amount)

    if new_current > 99:
        current = new_current % 100
    elif new_current < 0:
        current = (100 + new_current) % 100
    else:
        current = new_current

    if current == 0:
        result = result + 1


print('part_one', result)
