from typing import List

with open('input.txt') as input:
  entries = [entry.strip() for entry in input]


def make_number_list(number_string: str) -> List[int]:
  # ' 23  4  3 23 98 '
  return [int(num) for numbers in number_string.strip().split('  ') for num in numbers.split(' ')]

all_winning = []
all_matches = []
all_mine = []
total_cards = [1 for _ in entries]
score = []

for entry in entries:
  whole_card = entry.split(':')
  card_number = int(whole_card[0].strip().split(' ')[-1])
  numbers = whole_card[1].split('|')
  winning = make_number_list(numbers[0])
  mine = make_number_list(numbers[1])
  all_winning.append(winning)
  all_mine.append(mine)
  matches = set(winning) & set(mine)
  if len(matches) > 0:
    score.append(pow(2, len(matches)-1))
    all_matches.append(len(matches))
  else:
    score.append(0)
    all_matches.append(0)


for i in range(0, len(entries)):
  matches = all_matches[i]
  while matches > 0:
    if i+matches < len(entries):
      total_cards[i+matches] = total_cards[i+matches] + 1 * total_cards[i]
    matches = matches - 1


print('part 1:', sum(score))
print('part 2:', sum(total_cards))