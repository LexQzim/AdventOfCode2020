with open('day5.txt') as file:
    entries = [entry.strip() for entry in file]

# Part One
highestSeatId = 0
listOfIds = []
for entry in entries:
    row = range(128)
    col = range(8)
    for i in range(0, len(entry)):
        if i < 7:
            lenght = int(len(row)/2)
            # print(lenght)
            if(entry[i] == 'F'):
                row = row[:lenght]
            else:
                row = row[lenght:]
        else:
            lenght = int(len(col)/2)
            # print(lenght)
            if(entry[i] == 'L'):
                col = col[:lenght]
            else:
                col = col[lenght:]

    seatId = row[0] * 8 + col[0]
    listOfIds.append(seatId)
    if seatId > highestSeatId:
        highestSeatId = seatId
    # print(row[0])
    # print(col[0])

print('Part One: highestSeatId= ' + str(highestSeatId))

listOfIds.sort()
leftNeighbour = 0
rightNeighbour = 0
for i in range(0, len(listOfIds)):
    if i+1 < len(listOfIds):
        if listOfIds[i+1] - listOfIds[i] > 1:
            leftNeighbour = listOfIds[i]

        if listOfIds[i] - listOfIds[i+1] < -1:
            rightNeighbour = listOfIds[i+1]

mySeat = 0
if leftNeighbour < rightNeighbour:
    mySeat = leftNeighbour + (rightNeighbour - leftNeighbour)/2
else:
    mySeat = rightNeighbour + (leftNeighbour - rightNeighbour)/2

print("Part Two: My Seat Id = " + str(int(mySeat)))
