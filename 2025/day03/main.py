#!/usr/bin/env python
with open('./input.txt') as input:
    lines = input.readlines()

banks = [line.strip() for line in lines]
result = 0

for bank in banks:
    first_i = 0
    secon_i = 0
    i = 1

    while i < len(bank) - 1:
        if bank[i] > bank[first_i]:
            first_i = i
        i = i + 1

    secon_i = first_i + 1
    i = secon_i + 1
    while i < len(bank):
        if bank[i] > bank[secon_i]:
            secon_i = i
        i = i + 1

    result = result + int(bank[first_i] + bank[secon_i])


print('part one:', result)
