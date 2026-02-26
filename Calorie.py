print("Calorie Calculator developed by Monty")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))
age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ").lower()

if gender == "male":
    calories = 10 * weight + 6.25 * height - 5 * age + 5
else:
    calories = 10 * weight + 6.25 * height - 5 * age - 161

print("Daily Calories Needed:", int(calories))
