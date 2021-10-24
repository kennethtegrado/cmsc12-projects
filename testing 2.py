def idGenerator(dict):  # define a function named idGenerator and set one input paramater to a dict
    # use this function to generate an id for a user
    # use the dict parameter to check a dictionary
    members = len(dict)
    if members == 0:
        id = 'M0001'
    else:
        lastElement = list(dict.keys())[-1]
        idNum = ''
        for char in lastElement:
            if char.isnumeric():
                idNum += char

        newIdNumber = int(idNum) + 1
        if 1000 > newIdNumber >= 100:
            id = "M" + str(newIdNumber)
        elif 100 > newIdNumber >= 10:
            id = "M0" + str(newIdNumber)
        elif 10 > newIdNumber > 0:
            id = "M00" + str(newIdNumber)
    return id


mem = {
    'M0001': '',
    'M0002': '',
    'M0003': '',
    'M0004': '',
    'M0005': '',
    'M0006': '',
}

emp = {}

print(idGenerator(emp))
