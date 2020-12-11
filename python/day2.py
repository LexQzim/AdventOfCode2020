with open('day2.txt') as file:
    entries = [entry.strip() for entry in file]

# part one
countOfCorrectPassphrases = 0

for entry in entries:
    minCount = int(entry.split(' ', -1)[0].split('-', -1)[0])
    maxCount = int(entry.split(' ', -1)[0].split('-', -1)[1])
    letter = entry.split(' ', -1)[1][0]
    passphrase = entry.split(' ', -1)[2]

    letterCount = 0
    for char in passphrase:
        if char == letter:
            letterCount += 1

    if letterCount >= minCount and letterCount <= maxCount:
        countOfCorrectPassphrases += 1

print('part one ' + str(countOfCorrectPassphrases))

# part two
countOfCorrectPassphrases = 0

for entry in entries:
    firstPos = int(entry.split(' ', -1)[0].split('-', -1)[0]) - 1
    secondPos = int(entry.split(' ', -1)[0].split('-', -1)[1]) - 1
    letter = entry.split(' ', -1)[1][0]
    passphrase = entry.split(' ', -1)[2]

    letterFound = False
    for i in range(0, len(passphrase)):
        if i == firstPos and passphrase[i] == letter:
            letterFound = True

        if i == secondPos and passphrase[i] == letter:
            if letterFound:
                letterFound = False
            else:
                letterFound = True

    if(letterFound):
        countOfCorrectPassphrases += 1


print('part two ' + str(countOfCorrectPassphrases))
