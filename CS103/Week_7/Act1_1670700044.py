number = int(input("Please Enter Number : < ! 0 = STOP ! > "))
even = 0
odd = 0
while number != 0 :
    #step
    if number > 0 :
        if number%2 == 1 :
            odd = odd+1
        else :
            even += 1 
    number = int(input("Please Enter Number : < ! 0 = STOP ! > "))
# print output
print("-"*50)
print("Total odd number : ",odd)
print("Total even number : ",even)
print("-"*50)