def fileReader(dict):
    bmiInfo = ()
    checkFile = open("Gym", 'w')
    file = open("Gym", 'r')
    for lines in file:
        line = lines.split()
        name, weight, height, bmi, classification = line[1:]
        bmiInfo = (bmi, classification)
        dict[line[0]] = [name, weight, height, bmiInfo]
    file.close()
    return dict


def fileMaker(dict):
    file = open('Gym', 'w')
    for keys, values in dict.items():
        file.write(
            f'{keys} {values[0]} {values[1]} {values[2]} {values[3][0]} {values[3][1]} \n')
    file.close()


# name, weight, height, bmiinfo
dict = {
    'M0001': ['Aubrey', '49', '158', (19.9, 'Normal')],
    'M0002': ['Kenneth', '71', '175', (24.5, 'Normal')],
    'M0003': ['Renz', '90', '197', (19, 'Normal')]
}

dict2 = {

}
fileMaker(dict)
print(fileReader(dict2))
