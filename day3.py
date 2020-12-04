with open('day3.txt') as file:
    entries = [entry.strip() for entry in file]

right = 3
down = 1
lineLenght = len(entries[0])

# part one
foundRule2 = 0
for i in range(0, len(entries)-1):
    # print('right % lineLenght ' + str(right % lineLenght))
    # print('down ' + str(down))
    # print(entries[down][right % lineLenght])
    if(entries[down][right % lineLenght] == '#'):
        # print('found')
        foundRule2 += 1

    right += 3
    down += 1

print('Part One: ' + str(foundRule2))

# part two

right1 = 1
right3 = 5
right4 = 7
down2 = 2
down = 1
# part one
foundRule1 = 0
foundRule3 = 0
foundRule4 = 0
foundRule5 = 0

for i in range(0, len(entries)-1):
    if(entries[down][right1 % lineLenght] == '#'):
        foundRule1 += 1

    if(entries[down][right3 % lineLenght] == '#'):
        foundRule3 += 1

    if(entries[down][right4 % lineLenght] == '#'):
        foundRule4 += 1

    if(down2 <= len(entries)-1):
        if(entries[down2][right1 % lineLenght] == '#'):
            foundRule5 += 1

    right1 += 1
    right3 += 5
    right4 += 7
    down += 1
    down2 += 2

print('Part Two: ')
print('foundRule1 ' + str(foundRule1))
print('foundRule2 ' + str(foundRule2))
print('foundRule3 ' + str(foundRule3))
print('foundRule4 ' + str(foundRule4))
print('foundRule5 ' + str(foundRule5))

print('Solution: ' + str(foundRule1 * foundRule2 *
                         foundRule3 * foundRule4 * foundRule5))
