# bmi_calculator.py

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# Example usage
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = calculate_bmi(weight, height)
print(f"\nYour BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are healthy.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
