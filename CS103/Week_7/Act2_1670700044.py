totalp = 0
print("Menu : H = Hamburger , P = Pizza , W =Water , E = Exit")
menu = input("Enter menu (H,P,W,E) : ").upper()
while menu != 'E' :
    if menu == 'H' or menu == 'P' or menu == "W" :
        amount = int(input("Enter Amount "))
        if menu == 'H' :
            total = amount * 90
            # totalp = totalp + (amount*90)
            # price = 90
        elif menu == 'P' :
            total = amount * 185
             # price = 185
        else :
            total =  amount * 20
             # price = 90
        #total = amount * price
        totalp = totalp + total
    else :
        print("Invalid Menu! Please order again :")
    menu = input("Enter menu (H,P,W,E) : ").upper()
#-------------------------- Display summary
discount = 0
if totalp >= 500 : 
    discount = totalp / 10 
net = totalp - discount
print("-"*50)
print(f"Total Price   = {totalp:0.2f} baths")
print(f"Discount   = {discount:0.2f} baths")
print(f"Net Price    = {net:0.2f} baths")