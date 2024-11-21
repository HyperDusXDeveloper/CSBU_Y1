number = input("Enter a number : ")
while number.isnumeric() == False :
    print("Error.")
    number = input("Enter a number : ")
    
number = int(number)
digit = 0
while number > 0 :
    digit += 1
    number = number//10
    print(number)
print("Total digit = ",digit)