#!/usr/bin/env python
with open('./input.txt') as input:
    lines = input.readlines()

banks = [line.strip() for line in lines]
result = 0
result_two = 0

for bank in banks:
    def find_highest(left_bound: int, right_bound: int, jolts: str) -> int:
        i = left_bound + 1
        while i < len(jolts) - right_bound:
            if jolts[i] > jolts[left_bound]:
                left_bound = i
            i = i + 1
        return left_bound

    rounds = 11
    digits = ''
    left = 0
    while rounds >= 0:
        left = find_highest(left, rounds, bank)
        digits = digits + bank[left]
        rounds = rounds - 1
        left = left + 1

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
    result_two = result_two + int(digits)


print('part one:', result)
print('part two:', result_two)
