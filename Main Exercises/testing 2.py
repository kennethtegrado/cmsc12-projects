def fileReader(dict):  # define a new user function named fileReader then set the parameter to dict
    # use this function to load a database with the Gym.txt file
    # use the open() function to open the file Gym.txt with a 'r' read to declare that we are going to read the contents of the file
    # if the database is empty then the function will  do nothing
    dict.clear()
    file = open("Member's Database", 'r')
    # store the file object returned by the open() variable on the file variable
    for lines in file:  # use this loop to iterate on every lines on the file
        # use the .split() function to remove all the spaces in between words of the current line
        # at the same time, it will also convert all contents to a list that can easily be unparsed
        # use the hash (#) symbol as a separator of texts in single line
        # note that the data inside the texts are using the hash (#) symbol as the delimiter and we are just following that format
        line = lines.split('#')
        # using indexing, unparse all the data from the current line of text using the format below
        name, weight, height, bmi, classification = line[1:]
        weight = float(weight)  # convert weight to a float object
        height = float(height)  # convert height to a float object
        newClassification = classification.rstrip(" \n")
        # store the bmi and classification variable on a tuple to since some parts of the program is coded to process a tuple for the bmiInfo
        bmiInfo = (bmi, newClassification)
        print(bmiInfo)
        # then create a new item on the dictionary parameter with the key of line[0] with the value containing the variables below
        dict[line[0]] = [name, weight, height, bmiInfo]
    file.close()  # use the close() method to tell the program to close the file variable to avoid data loss
    return dict  # return the newly created dict parameter back to the main program


dict = {}

print(fileReader(dict))
