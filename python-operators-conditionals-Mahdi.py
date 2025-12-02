# ==============================
# PYTHON TRAINING – ALL TASKS 1 TO 30
# ==============================

# ==============================
# TASK 1 – LOGIC OPERATORS
# ==============================
a = True
b = False
c = True
print("TASK 1")
print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT b:", not b)
print("-----------------------------")

# ==============================
# TASK 2 – LOGIC PRACTICE
# ==============================
is_member = True
has_coupon = False
discount_applies = is_member or has_coupon
print("TASK 2")
print("Discount applies:", discount_applies)
print("-----------------------------")

# ==============================
# TASK 3 – BINARY OPERATORS
# ==============================
print("TASK 3")
print("5 & 3:", 5 & 3)
print("5 | 3:", 5 | 3)
print("5 ^ 3:", 5 ^ 3)
print("5 << 1:", 5 << 1)
print("5 >> 1:", 5 >> 1)
print("-----------------------------")

# ==============================
# TASK 4 – BINARY CONVERSIONS
# ==============================
num = 10
binary = bin(num)
back_to_int = int(binary, 2)
print("TASK 4")
print("Binary:", binary)
print("Back to int:", back_to_int)
print("-----------------------------")

# ==============================
# TASK 5 – LAMBDA OPERATORS
# ==============================


def square(x): return x**2
def sum_two(x, y): return x + y
def is_even(x): return x % 2 == 0


print("TASK 5")
print("Square of 5:", square(5))
print("Sum of 3 and 4:", sum_two(3, 4))
print("Is 8 even?", is_even(8))
print("-----------------------------")

# ==============================
# TASK 6 – LAMBDA SORTING
# ==============================
people = [("Alice", 25), ("Bob", 19), ("Eve", 30)]
sorted_people = sorted(people, key=lambda x: x[1])
print("TASK 6")
print("Sorted by age:", sorted_people)
print("-----------------------------")

# ==============================
# TASK 7 – OPERATOR PRECEDENCE
# ==============================
step1 = 2 ** 2
step2 = 3 * step1
step3 = step2 / 2
result = 5 + step3
print("TASK 7")
print("Result:", result)
print("-----------------------------")

# ==============================
# TASK 8 – OPERATORS 1
# ==============================
x = 7
y = 3
print("TASK 8")
print("x + y:", x + y)
print("x - y:", x - y)
print("x * y:", x * y)
print("x / y:", x / y)
print("x // y:", x // y)
print("x % y:", x % y)
print("x ** y:", x ** y)
print("-----------------------------")

# ==============================
# TASK 9 – OPERATORS 2 (BMI)
# ==============================
weight = 70
height = 1.75
bmi = weight / height**2
print("TASK 9")
print("BMI:", bmi)
print("-----------------------------")

# ==============================
# TASK 10 – OPERATORS 3
# ==============================
num = 5
num = (num + 10) * 3 - 5
print("TASK 10")
print("Result:", num)
print("-----------------------------")

# ==============================
# TASK 11 – OPERATORS 4 (SWAP)
# ==============================
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print("TASK 11")
print("a:", a, "b:", b)
print("-----------------------------")

# ==============================
# TASK 12 – OPERATORS 5
# ==============================
x = 15
y = 4
print("TASK 12")
print("x // y:", x // y)
print("x % y:", x % y)
print("(x + y) * (x - y):", (x + y) * (x - y))
print("-----------------------------")

# ==============================
# TASK 13 – OPERATORS 6
# ==============================
a = 10
b = 20
c = 30
average = (a + b + c) / 3
print("TASK 13")
print("Average:", average)
print("-----------------------------")

# ==============================
# TASK 14 – OPERATORS 7 (Checkout)
# ==============================
price_a = 4.99
price_b = 7.49
tax = 0.12
subtotal = price_a + price_b
total = subtotal * (1 + tax)
print("TASK 14")
print("Total with tax:", total)
print("-----------------------------")

# ==============================
# TASK 15 – OPERATORS 8 (Compound Interest)
# ==============================
P = 1000
r = 0.05
t = 3
A = P * (1 + r)**t
print("TASK 15")
print("Future value:", A)
print("-----------------------------")

# ==============================
# TASK 16 – CASTING
# ==============================
num_str = "123"
num_int = int(num_str)
float_str = "45.9"
num_float = float(float_str)
num = 100
num_str2 = str(num)
print("TASK 16")
print("Integer:", num_int)
print("Float:", num_float)
print("String:", num_str2)
print("-----------------------------")

# ==============================
# TASK 17 – CASTING PRACTICE
# ==============================
age_str = input("TASK 17 – Enter your age: ")
age = int(age_str)
age_plus_5 = age + 5
print("Your age in 5 years:", age_plus_5)
print("-----------------------------")

# ==============================
# TASK 18 – ROUNDING
# ==============================
num = 4.456
print("TASK 18")
print("Nearest integer:", round(num))
print("1 decimal place:", round(num, 1))
print("2 decimal places:", round(num, 2))
print("-----------------------------")

# ==============================
# TASK 19 – ROUNDING PRACTICE
# ==============================
numbers = [4.67, 5.12, 3.49]
rounded_numbers = [round(n, 1) for n in numbers]
print("TASK 19")
print("Rounded list:", rounded_numbers)
print("-----------------------------")

# ==============================
# TASK 20 – CONDITIONAL STATEMENTS BASIC
# ==============================
score = 78
print("TASK 20")
if score >= 50:
    print("Pass")
else:
    print("Fail")
print("-----------------------------")

# ==============================
# TASK 21 – CONDITIONAL CHAINS
# ==============================
temperature = 18
print("TASK 21")
if temperature < 0:
    print("Freezing")
elif 0 <= temperature <= 15:
    print("Cold")
elif 16 <= temperature <= 25:
    print("Warm")
else:
    print("Hot")
print("-----------------------------")

# ==============================
# TASK 22 – CONDITIONAL & OPERATORS
# ==============================
age = 20
has_id = True
print("TASK 22")
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
print("-----------------------------")

# ==============================
# TASK 23 – NESTED CONDITIONALS
# ==============================
income = 60000
credit_score = 720
print("TASK 23")
if income >= 50000:
    if credit_score >= 700:
        print("Loan approved")
    else:
        print("Loan denied due to credit score")
else:
    print("Loan denied due to income")
print("-----------------------------")

# ==============================
# TASK 24 – MINI PROJECT – CONDITIONALS
# ==============================
username = input("TASK 24 – Username: ")
password = input("Password: ")
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Username not found")
print("-----------------------------")

# ==============================
# TASK 25 – COMBINED OPERATORS
# ==============================
num1 = int(input("TASK 25 – Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)
print("First number even?", num1 % 2 == 0)
print("Second number even?", num2 % 2 == 0)
print("-----------------------------")

# ==============================
# TASK 26 – BINARY + LAMBDA
# ==============================
numbers = [3, 5, 12, 7]
double_numbers = list(map(lambda x: x*2, numbers))
binary_numbers = [bin(x) for x in double_numbers]
print("TASK 26")
print("Doubled numbers:", double_numbers)
print("Binary of doubled numbers:", binary_numbers)
print("-----------------------------")

# ==============================
# TASK 27 – STRING + LOGIC + CASTING
# ==============================
birth_year = int(input("TASK 27 – Enter your year of birth: "))
current_year = 2025
age = current_year - birth_year
if age < 18:
    print("You are a minor")
else:
    print("You are an adult")
print("-----------------------------")

# ==============================
# TASK 28 – OPERATOR PRECEDENCE
# ==============================
step1 = 3 * 5
step2 = 10 + step1
step3 = step2 ** 2
step4 = 4 % 3 + 1
result = step3 / step4
print("TASK 28")
print("Result:", result)
print("-----------------------------")

# ==============================
# TASK 29 – CONDITIONAL CALCULATOR
# ==============================
num1 = float(input("TASK 29 – Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
print("-----------------------------")

# ==============================
# TASK 30 – MINI PROGRAM
# ==============================
name = input("TASK 30 – Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / height**2
bmi_rounded = round(bmi, 2)
age_category = (lambda age: "Minor" if age < 18 else "Adult")(age)
can_vote = age >= 18
print("\n--- Summary ---")
print("Name:", name)
print("Age:", age, "(", age_category, ")")
print("BMI:", bmi_rounded)
print("Can vote?", can_vote)
