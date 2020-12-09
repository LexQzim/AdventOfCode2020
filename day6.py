import copy

with open('day6.txt') as file:
    entries = [entry.strip() for entry in file]

count = 0
yesAnswers = []
letterList = set()
for i in range(0, len(entries)):
    for letter in entries[i]:
        if letter not in letterList:
            letterList.add(letter)

    if not entries[i].strip():
        yesAnswers.append(letterList)
        letterList = set()
        count += 1

yesAnswers.append(letterList)

countOfAnswers = 0
for answer in yesAnswers:
    countOfAnswers += len(answer)


print("Part One: Count of right answer = " + str(countOfAnswers))

# Part two


def intersection(letterList):
    letterDict = {i: 0 for i in letterList[0]}

    length = len(letterList)-1

    for letter in letterList:
        if(len(letter) > 0):
            for let in letter:
                # print(let)
                if let in letterDict:
                    letterDict[let] += 1

    # print("length " + str(length))

    tmpDict = copy.deepcopy(letterDict)
    for k, v in tmpDict.items():
        if v < length:
            letterDict.pop(k)

    return letterDict


yesAnswers = []
letterList = []
for i in range(0, len(entries)):
    letterList.append(list(entries[i]))

    if not entries[i].strip() or i == len(entries)-1:

        if len(letterList) > 2:
            countList = intersection(letterList)
            # print(countList)
            yesAnswers.append(len(countList))

        else:
            yesAnswers.append(len(letterList[0]))

        letterList = []

countOfAnswers = 0
for answer in yesAnswers:
    countOfAnswers += answer

print("Part Two: Count of right answer = " + str(countOfAnswers))
