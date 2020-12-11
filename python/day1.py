import itertools

with open('day1.txt') as file:
    entries = [int(entry.strip()) for entry in file]

for a, b in itertools.combinations(entries, 2):
    year = a + b
    if year == 2020:
        print('Part One: ' + str(a * b))

for a, b, c in itertools.combinations(entries, 3):
    year = a + b + c
    if year == 2020:
        print('Part Two: ' + str(a * b * c))
