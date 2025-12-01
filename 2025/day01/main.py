#!/usr/bin/env python
with open('./input.txt') as input:
    lines = input.readlines()

commands = [line.strip() for line in lines]

current = 50
result = 0

for command in commands:
    amount = int(command[1:])
    if command[0] == 'L':
        current = current - amount
    elif command[0] == 'R':
        current = current + amount

    if current < 0:
        current = 100 + current
    current = current % 100

    if current == 0:
        result = result + 1

print(commands[0:10])
print(result)
