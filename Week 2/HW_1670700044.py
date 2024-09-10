# Get data values BMI Calculator
# output line_1
print(" ","="*30)
print(f"{'|':<9} BMI Calculator {'|':>9}")
print(" ","-"*30)

# output line_2
first_name = input("Enter youe first Name :")
last_name = input("Enter youe last Name :")
age = int(input("Year of birth :"))
height = float(input("Please height(cm):"))
weight = float(input("Please weight(kg):"))

# Calculate year old
age = 2024-age

# Output Result BMI Calculator

# output line_1
print("="*40)
print(f"{'BMI':<17} {'Weight Status':>20}")
print("="*40)


# output line_2
print(f"{'Below 18.5':<17} {'Underweight':>18}")
print(f"{'18.5 - 24.9':<17} {'Healthy Weight':>21}")
print(f"{'25.0 - 29.9':<17} {'Overweight':>17}")
print(f"{'30.0 and Above':<17} {'Obesity':>14}")
print("-"*40)
print(f"{'Name':<7} : {first_name:<7} {last_name:<7}")
print(f"{'Height':<7} : {height:>3.1f} CM")
print(f"{'Weight':<7} : {weight:>5.1f} KG")
print(f"{'Age':<7} : {age:>1}")

# Calculate BMI
height = height/100
bmi = weight/height**2

# output line_3
print("-"*19)
print(f"{'|':<2} Your BMI {bmi:1.2f} {'|':<3}")
print("-"*19)
