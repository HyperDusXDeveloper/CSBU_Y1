#Basic Python 1 input output 
name = input("Enter Your Name : ")
wight = int(input("Plesas Enter Wight  "))
height = int(input("Please Enter height  "))
print("You name " + name + " Wight = ",wight ,"KG", "Height = " , height,"CM")
height = height/100
bmi = wight/height**2
print("You BMI = ",bmi)
print(name + "   " + name)
#Basic Python 2 if 2 elfe
if bmi < 18.5 :
    print("light and soft ")
if bmi > 18.5 :
    print("fat")