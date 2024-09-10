# Get data values BMI Calculator
# output line_1
print(" ","="*30)
print(f"{'|':<9} BMI Calculator {'|':>9}")
print(" ","="*30)

# output line_2
first_name = input("Enter youe first Name : ")
last_name = input("Enter youe last Name : ")
age = int(input("Year of birth : "))
height = float(input("Please height(meters) : "))
weight = float(input("Please weight(kg) : "))
# Calculate year old
age = 2024-age

# Output Result BMI Calculator

# output line_1
print()
print(f"{' ':>4}{'BMI':<17} {'Weight Status':>16}")
print("="*40)

# output line_2
print(f"{'Below  18.5':<17} {'Underweight':>18}")
print(f"{'18.5 - 24.9':<17} {'Healthy Weight':>21}")
print(f"{'25.0 - 29.9':<17} {'Overweight':>17}")
print(f"{'30.0 and Above':<17} {'Obesity':>14}")
print("-"*40)
print("\n")
height_CM = height*100
print(f"{'Name':<7} : {first_name:<7} {last_name:<7}")
print(f"{'Height':<7} : {' ':>1} {height_CM:>4.1f} CM.")
print(f"{'Weight':<7} : {' ':>1} {weight:>5.1f} KG.")
print(f"{'Age':<7} : {age:>1}")

# Calculate BMI
bmi = weight/height**2

# output line_3
print("*"*60)
if bmi < 18.5 :
    print(f"{'|':<6} Your BMI is {bmi:1.2f} {'|':>7} {' ':>7} Underweight {'|':>7}")
elif bmi > 18.5 and bmi < 25.0 : 
    print(f"{'|':<6} Your BMI is {bmi:1.2f} {'|':>7} {' ':>6} Healthy Weight {'|':>5}")
elif bmi > 25.0 and bmi < 30.0 : 
    print(f"{'|':<6} Your BMI is {bmi:1.2f} {'|':>7} {' ':>7} Overweight {'|':>8}")
elif bmi > 30.0: 
    print(f"{'|':<6} Your BMI is {bmi:1.2f} {'|':>7} {' ':>9} Obesity {'|':>9}")
print("*"*60)
