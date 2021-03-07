weight = int(input("Weight in kilogram (kg): "))
height = float(input("Height in metre (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight \n"+"Please consume more food and don't starve yourself!")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight \n"+"Be aware of your daily diet")
elif bmi >= 30:
    print("Obesity \n"+"Gotta exercise to cut down some weight!")