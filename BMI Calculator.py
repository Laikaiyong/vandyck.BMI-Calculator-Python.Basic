weight = int(input("Weight in kilogram (kg): "))
height = float(input("Height in metre (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(bmi + "\nUnderweight \n"+"Please consume more food and don't starve yourself!")
elif bmi >= 18.5 and bmi < 25:
    print(bmi + "\nNormal")
elif bmi >= 25 and bmi < 30:
    print(bmi + "\nOverweight \n"+"Be aware of your daily diet")
elif bmi >= 30:
    print(bmi + "\nObesity \n"+"Gotta exercise to cut down some weight!")
