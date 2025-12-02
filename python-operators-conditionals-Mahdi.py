# ==============================
# TASK 30 – MINI PROGRAM
# ==============================
# Combining variables, operators, logic, rounding, lambda, conditionals

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# BMI calculation
bmi = weight / height**2
bmi_rounded = round(bmi, 2)

# Age category using lambda
age_category = (lambda age: "Minor" if age < 18 else "Adult")(age)

# Eligibility check
can_vote = age >= 18

# Summary print
print("\n--- Summary ---")
print("Name:", name)
print("Age:", age, "(", age_category, ")")
print("BMI:", bmi_rounded)
print("Can vote?", can_vote)
