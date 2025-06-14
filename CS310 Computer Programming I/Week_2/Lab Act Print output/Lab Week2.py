# User input
name = input("Please Enter Your Name :  ")
height = int(input("Please Enter Height  : "))
weight = int(input("Please Enter Weight  : "))
# calculate BMI
height = height/100
heightN = height*100
bmi = weight/height**2
# output
print("_"*50)
print(f"{'Name':<12} : {name:<10}")
print(f"{'Height':<12} : {heightN :>7.1f}"," CM")
print(f"{'Weight':<12} : {weight:>7.1f}"," KG")
print("_"*50)
print(f"{'Your BMI':<12} : {bmi:>7.2f}")
print("_"*50)