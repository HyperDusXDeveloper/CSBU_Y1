num = int(input("Please Enter Number (0-1000)  : "))
if num >= 0 and num <= 100 :
    print("num : 0 - 100 ")
    print("-"*40)
    if num%2 == 0 :
        print (f"{num} devided by 2 , result = {num**2:0.2f} ")
    if num%4 == 0 :
        print (f"{num} devided by 4 , result = {num**3:0.2f} ")
    if num%5 == 0 :
        print (f"{num} devided by 5 , result = {num/2:0.2f} ")
    if num%8 == 0 :
        print (f"{num} devided by 8 , result = {num/2*8:0.2f} ")
elif num >= 101 and num <= 1000 :
    print("num : 101 - 1000 : ")
    if num%10 == 0 :
        print (f"{num} devided by 10 , result = {num*10:0.2f} ")
    if num%15 == 0 :
        print (f"{num} devided by 15 , result = {num/2*8:0.2f} ")
else :
    print("Out of Range ! \n Please enter 0 - 1000 ")
print("-"*40) 