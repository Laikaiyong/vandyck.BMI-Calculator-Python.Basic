weight = int(input("Weight in kilogram (kg): "))
height = float(input("Height in metre (m): "))

bmi = weight / (height ** 2)

print(bmi)

if bmi < 18.5:
    print("\nUnderweight \n"+"Please consume more food and don't starve yourself!")
elif bmi >= 18.5 and bmi < 25:
    print("\nNormal")
elif bmi >= 25 and bmi < 30:
    print("\nOverweight \n"+"Be aware of your daily diet")
elif bmi >= 30:
    print("\nObesity \n"+"Gotta exercise to cut down some weight!")
