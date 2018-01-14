weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
bmi = weight/height**2
if bmi>25:
    print("Overweight")
elif bmi>=18.5:
    print("Normal weight")
else:
    print("Underweight")