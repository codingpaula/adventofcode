with open('./day01.txt') as input:
  entries = [entry.strip() for entry in input]

sum = 0

def search_simple(entry):
  first = 0
  second = 0
  for element in entry:
    if str.isnumeric(element):
      if first == 0:
        first = int(element)
      else:
        second = int(element)
  if second == 0:
    second = first
  return first, second

for entry in entries:
  first, second = search_simple(entry)
  sum = sum + first * 10 + second

print(sum)

sum = 0
numbers = [
  ("one", 1),
  ("two", 2),
  ("three", 3),
  ("four", 4),
  ("five", 5),
  ("six", 6),
  ("seven", 7),
  ("eight", 8),
  ("nine", 9)
]

for entry in entries:
  # find digits first
  digits = []
  first = 0
  second = 0
  if any([num[0] in entry for num in numbers]):
    possible = 0
    for i in range(0, len(entry)):
      # found a normal digit -> add it to the array
      if str.isnumeric(entry[i]):
        digits.append(int(entry[i]))
        possible = i
      # might find a written digit
      elif i - possible >= 2:
        for num in numbers:
          if num[0] in entry[possible:i+1]:
            digits.append(num[1])
            possible = i
    first = digits[0]
    second = digits[-1]
  else:
    first, second = search_simple(entry)
  sum = sum + first * 10 + second

print(sum)