

# All functions used by the program
def menu():
    print("Options:\n [1]Add a member\n [2]View a member record\n [3]View all members\n [4]Edit member record\n [5]Delete a member record\n [6]Delete all member records\n [0]Exit ") 
    #print a statement to show the operations available
    choice = input("Enter your choice: ") #ask for user input using input() function 
    return choice   

def idGenerator(dict):
    members = len(dict)
    newIdNumber = members + 1
    if 1000 > newIdNumber >= 100:
        id = "M" + str(newIdNumber)
    elif 100> newIdNumber >= 10:
        id = "M0" + str(newIdNumber)
    elif 10 > newIdNumber > 0:
        id = "M00" +str(newIdNumber)
    return id

def bmi(weight, height):
    bmi = round(weight / ((height/100) ** 2), 1)
    if 0 < bmi < 18.5:
        index = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        index = "Healthy"
    elif 25 <= bmi <= 29.9:
        index = "Overweight"
    elif bmi >= 30:
        index = "Obese"
    else:
        index = "Cannot be determined"
    return bmi,index

def addMem(id, dict):
    name = input("Enter name: ")
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))
    bmiInfo = bmi(weight, height)
    print(f'BMI is {bmiInfo[0]}\nType is {bmiInfo[1]}')
    dict[id] = [name, weight, height, bmiInfo]
    return dict

def viewMem(dict):
    record = ''
    id = input("Enter member ID: ")
    name, weight, height, bmiInfo = dict[id]
    if id in dict:
        record += "=== Member Information ===\n"
        record += f'({id}) - {name} {weight} kg {height} cm (BMI: {bmiInfo[0]}; {bmiInfo[1]})\n'
    else:
        record += 'Sorry, the record does not exist!'
    return record

def viewAll(dict):
    record = '=== List of members ===\n'
    if len(dict) > 0:
        for id, data in dict.items():
            name, weight, height, bmiInfo = data
            record += f'({id}) - {name} {weight} kg {height} cm (BMI: {bmiInfo[0]}; {bmiInfo[1]})\n'
    else:
        record += 'Sorry, record is empty!'
    return record

def editMem(dict):
    id = input("Enter the ID of user that you wish to edit: ")
    if id in dict:
        weight = float(input("Enter your new weight here (kg): "))
        dict[id][1] = weight
        newBMI = bmi(weight, dict[id][2])
        dict[id][3] = newBMI
        print("Successfully Edited!")
        return dict
    else:
        print("Member does not exist!")  

def delMem(dict):
    id = input("Enter member ID: ")
    if id in dict:
        del dict[id]
        print(f'Member {id} successfully deleted.')
        return dict
    else:
        print('Sorry, the record does not exist!')

def delAll(dict):
    return dict.clear()

# Start of Program
memberData = {

}
print("Welcome to EBR Fitness Club")

while True:
    choice = menu()
    if choice == "1":
        addMem(idGenerator(memberData), memberData)
        print("Successfully Added!")
        print()
    elif choice == "2":
        print(viewMem(memberData))
    elif choice == "3":
        print(viewAll(memberData))
    elif choice == "4":
        editMem(memberData)
    elif choice == "5":
        delMem(memberData)
    elif choice == "6":
        delAll(memberData)
    elif choice == "0":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice!")


