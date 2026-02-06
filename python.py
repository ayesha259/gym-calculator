weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    result = "Underweight"
elif bmi < 25:
    result = "Normal"
elif bmi < 30:
    result = "Overweight"
else:
    result = "Obese"

print("BMI:", round(bmi, 2))
print("Result:", result)

