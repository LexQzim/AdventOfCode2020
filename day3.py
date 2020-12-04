with open('day3.txt') as file:
    entries = [entry.strip() for entry in file]

right = 3
down = 1
lineLenght = len(entries[0])

# part one
foundCounter = 0
for i in range(0, len(entries)-1):
    # print('right % lineLenght ' + str(right % lineLenght))
    # print('down ' + str(down))
    # print(entries[down][right % lineLenght])
    if(entries[down][right % lineLenght] == '#'):
        # print('found')
        foundCounter += 1

    right += 3
    down += 1

print('Part One: ' + str(foundCounter))
