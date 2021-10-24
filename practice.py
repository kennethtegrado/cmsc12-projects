listGrade = []
listUnits = []
x = 0

while x < 5:
    userGrade = float(input("Write your grade here: "))
    userUnit = int(input("Write units here: "))
    listGrade.append(userGrade)
    listUnits.append(userUnit)
    x += 1

print(listGrade)
print(listUnits)