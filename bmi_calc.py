# this program is about The BMI calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

final = round(weight / (height ** 2))
if final <= 18:
    print(f"Your BMI is {final}, you are underweight.")
elif 18 < final <= 25:
    print(f"Your BMI is {final}, you have a normal weight.")
elif 25 < final <= 30:
    print(f"Your BMI is {final}, you are slightly overweight.")
elif 30 < final <= 35:
    print(f"Your BMI is {final}, you are obese.")
elif 35 < final:
    print(f"Your BMI is {final}, you are clinically obese.")




