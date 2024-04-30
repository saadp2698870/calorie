import math

def calculate_bmr(weight, height, age, sex):
    if sex == "male":
        bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return bmr

def calculate_daily_calories(bmr, activity_level):
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return calories

def create_diet_plan(calories):
    meals = {
        'breakfast': calories * 0.25,
        'lunch': calories * 0.35,
        'dinner': calories * 0.35,
        'snacks': calories * 0.05
    }
    return meals

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
sex = input("Enter your sex (male or female): ")
activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active): ")

bmr = calculate_bmr(weight, height/100, age, sex)
daily_calories = calculate_daily_calories(bmr, activity_level)
diet_plan = create_diet_plan(daily_calories)

print("Your daily calorie needs are: ", daily_calories)
print("Your diet plan is: ", diet_plan)