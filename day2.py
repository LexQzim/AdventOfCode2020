with open('day2.txt') as file:
    entries = [entry.strip() for entry in file]

minCount = []
maxCount = []
letter = []
passphrase = []

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


print(countOfCorrectPassphrases)
