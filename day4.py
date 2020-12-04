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
# print(listOfPassports)

listOfNone = []

for passport in listOfPassports:
    for k, v in passport.items():
        if passport[k] is None and k != cid:
            listOfNone.append(passport)
            # print(k)
            # print(passport[k])
            countOfCorrectPassports -= 1
            break

print(countOfCorrectPassports)

