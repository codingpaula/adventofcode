with open('day02.txt') as input:
  entries = [entry.strip() for entry in input]

sum = 0
power = 0

limits = {
  'red': 12,
  'green': 13,
  'blue': 14
}

maximums = {
  'red': 0,
  'green': 0,
  'blue': 0
}

for entry in entries:
  # reset maximum tracker
  for num in maximums:
    maximums[num] = 0

  splitted = entry.split(':')
  game_number = int(splitted[0].split(' ')[1])
  rounds = [element.strip() for element in splitted[1].split(';')]
  # ["3 blue, 4 red", "1 red, 2 green", "6 blue", "2 green"]
  valid = True
  for round in rounds:
    values = [element.strip() for element in round.split(',')]
    # ["3 blue", "4 red"]
    for pair in values:
      amount_color = [element.strip() for element in pair.split(' ')]
      # ["3", "blue"]
      amount = int(amount_color[0])
      color = amount_color[1]
      if amount > limits[color]:
        valid = False
      if amount > maximums[color]:
        maximums[color] = amount
  if valid:
    sum = sum + game_number
  power = power + maximums['blue'] * maximums['green'] * maximums['red']

print(sum)
print(power)