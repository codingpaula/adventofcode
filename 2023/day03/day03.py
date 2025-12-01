with open('day03.txt') as input:
  entries = [entry.strip() for entry in input]

symbols = [] # pos x,y
numbers = []
two = []

entries = [[x for x in entry] for entry in entries]
gears = []


for entry in entries:
  new_line = []
  for element in entry:
    new_line.append(element)
  gears.append(new_line)


for i in range(0, len(entries)):
  for j in range(0, len(entries[i])):
    if not str.isnumeric(entries[i][j]) and entries[i][j] != '.':
      symbols.append([i, j])


def find_number_around_position(i, j, schematic):
  start_j = j
  end_j = j

  while True:
    start_j = start_j - 1
    if start_j < 0:
      break
    if not str.isnumeric(schematic[i][start_j]):
      break

  start_j = start_j + 1

  while True:
    end_j = end_j + 1
    if end_j >= len(schematic[0]):
      break
    if not str.isnumeric(schematic[i][end_j]):
      break

  end_j = end_j - 1
  return int(''.join(schematic[i][start_j:end_j+1])), start_j, end_j


for symbol in symbols:
  # look around the symbol
  from_i = symbol[0]-1 if symbol[0]-1 >= 0 else symbol[0]
  to_i = symbol[0]+1 if symbol[0]+1 <= len(entries) else symbol[0]
  from_j = symbol[1]-1 if symbol[1] >= 0 else symbol[1]
  to_j = symbol[1]+1 if symbol[1] <= len(entries[0]) else symbol[1]
  for i in range(from_i, to_i+1):
    for j in range(from_j, to_j+1):
      if str.isnumeric(entries[i][j]):
        # we found a potential number, i has to stay the same, so we need the start and end j
        new_number, start_j, end_j = find_number_around_position(i, j, entries)
        numbers.append(new_number)

        # erase this number from the input
        for num in range(start_j, end_j+1):
          entries[i][num] = '.'

  # if we have a gear, we need to check for parts
  if entries[symbol[0]][symbol[1]] == '*':
    gear_numbers = []
    for i in range(from_i, to_i+1):
      for j in range(from_j, to_j+1):
        if str.isnumeric(gears[i][j]):
          new_number, start_j, end_j = find_number_around_position(i, j, gears)
          gear_numbers.append(new_number)
    gear_numbers = set(gear_numbers)
    gear_numbers = list(gear_numbers)
    if len(gear_numbers) == 2:
      two.append(gear_numbers[0] * gear_numbers[1])

print('part 1:', sum(numbers))
print('part 2:', sum(two))