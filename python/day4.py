import re

with open('day4.txt') as file:
    entries = [entry.strip() for entry in file]

byr = 'byr'
iyr = 'iyr'
eyr = 'eyr'
hgt = 'hgt'
hcl = 'hcl'
ecl = 'ecl'
pid = 'pid'
cid = 'cid'

passDict = dict.fromkeys([cid, byr, iyr, eyr, hgt, hcl, ecl, pid])
listOfPassports = []

for i in range(0, len(entries)):
    for entry in entries[i].split(' '):
        element = entry.split(':')
        if(len(element) > 1):
            passDict[element[0]] = element[1]

    if not entries[i].strip():
        listOfPassports.append(passDict)
        passDict = dict.fromkeys([cid, byr, iyr, eyr, hgt, hcl, ecl, pid])

listOfPassports.append(passDict)

countOfCorrectPassports = len(listOfPassports)
print('countOfPassports: ' + str(countOfCorrectPassports))

listOfNone = []

for passport in listOfPassports:
    for k, v in passport.items():
        if passport[k] is None and k != cid:
            listOfNone.append(passport)
            # print(k)
            # print(passport[k])
            countOfCorrectPassports -= 1
            break

listOfCorrectPassports = [
    elem for elem in listOfPassports if elem not in listOfNone]

print('Part One: ' + str(len(listOfCorrectPassports)))
# Part two

hairColorRe = "\A#[a-f0-9]{6}"
pidRe = "[0-9]{9}"
eclValidEntrie = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

validPassports = 0

for passport in listOfCorrectPassports:
    validEntries = 0
    if(int(passport[byr]) > 1919 and int(passport[byr]) < 2003):
        validEntries += 1
        # print(passport[byr])
    if(int(passport[iyr]) > 2009 and int(passport[iyr]) < 2021):
        validEntries += 1
        # print(passport[iyr]
    if(int(passport[eyr]) > 2019 and int(passport[eyr]) < 2031):
        validEntries += 1
        # print(passport[eyr])
    if(re.search(hairColorRe, passport[hcl])):
        validEntries += 1
        # print(passport[hcl])
    if(re.search(pidRe, passport[pid]) and len(passport[pid]) == 9):
        validEntries += 1
        # print(passport[pid])
    if passport[ecl] in eclValidEntrie:
        validEntries += 1
        # print(passport[ecl])
    if re.search("cm$", passport[hgt]):
        cm = int(passport[hgt].split("cm")[0])
        if cm >= 150 and cm <= 193:
            validEntries += 1
            # print(cm)
    if re.search("in$", passport[hgt]):
        inch = int(passport[hgt].split("in")[0])
        if inch >= 59 and inch <= 76:
            validEntries += 1
            # print(inch)

    if validEntries == 7:
        validPassports += 1

print('Part Two: ' + str(validPassports))
