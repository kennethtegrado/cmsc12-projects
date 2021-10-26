def bmi(weight, height):
    bmi = round(weight / ((height/100) ** 2), 1)
    return bmi


print(bmi(49, 157))
