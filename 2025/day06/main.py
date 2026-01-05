with open('./input.txt') as input:
    lines = input.readlines()

problems: list[list[int]] = []
operators: list[str] = []

for e in lines[0].strip().split():
    problems.append([])

for line in lines:
    numbers = line.strip().split()
    for i, num in enumerate(numbers):
        if num in ('+', '*'):
            operators.append(num)
        else:
            problems[i].append(int(num))

part_one = 0

for numbers, operator in zip(problems, operators, strict=True):
    if operator == '*':
        result = 1
        for num in numbers:
            result = result * num
    elif operator == '+':
        result = 0
        for num in numbers:
            result = result + num
    part_one = part_one + result

print('part one:', part_one)
