Tittle_1 = """----------------------------------------------------
                       Menu 
----------------------------------------------------             
  ID                Menu               Price
  F01      Tuna Tartare Salsa           125
  F02      Cordon Bleu Chicken          145
  F03      Salmon Steak With Sauce      169
  F04      Caesar Salad                 139
  D01      Sparkling Sunset              90
  D02      Coke Mojito                   60
---------------------------------------------------"""
Tittle_2 = """                  Receipt 
---------------------------------------------------             
   Menu                 QTY           Total Price"""
print(Tittle_1)
menu_list = []
amount_list = []
Total_sum = []

menu = input("Menu ID : ").upper()
amount = int(input("Amount : "))
yes_no = input("Next Order(Y/N) : ").upper()
order_sum = 0
discount = 0
tax = 0
net_total = 0

i = 0
while yes_no == "Y" or "N" :
    if yes_no == "Y" :
        if menu == "F01" or menu == "F02" or menu == "F03" or menu == "F04" or menu == "D01" or menu == "D02" :
            amount_list.append(amount)
            menu_list.append(menu)
            if menu == "F01" :
                Total_sum.append(125*amount)
                menu_list.remove("F01")
                menu_list.append("Tuna Tartare Salsa")
            elif menu == "F02" :
                Total_sum.append(145*amount)
                menu_list.remove("F02")
                menu_list.append("Cordon Bleu Chicken")
            elif menu == "F03" :
                Total_sum.append(169*amount)
                menu_list.remove("F03")
                menu_list.append("Salmon Steak With Sauce")
            elif menu == "F04" :
                Total_sum.append(139*amount)
                menu_list.remove("F04")
                menu_list.append("Caesar Salad")
            elif menu == "D01" :
                Total_sum.append(90*amount)
                menu_list.remove("D01")
                menu_list.append("Sparkling Sunset")
            elif menu == "D02" :
                Total_sum.append(60*amount)
                menu_list.remove("D02")
                menu_list.append("Coke Mojito")
        else :
            print("Please Input Something in menu")
            menu = input("Menu ID : ").upper()
            amount = int(input("Amount : "))
            yes_no = input("Next Order(Y/N) : ").upper()
        menu = input("Menu ID : ").upper()
        amount = int(input("Amount : "))
        yes_no = input("Next Order(Y/N) : ").upper()
    if yes_no == "N" :
        if menu == "F01" or menu == "F02" or menu == "F03" or menu == "F04" or menu == "D01" or menu == "D02" :
            amount_list.append(amount)
            menu_list.append(menu)
            if menu == "F01" :
                Total_sum.append(125*amount)
                menu_list.remove("F01")
                menu_list.append("Tuna Tartare Salsa")
            elif menu == "F02" :
                Total_sum.append(145*amount)
                menu_list.remove("F02")
                menu_list.append("Cordon Bleu Chicken")
            elif menu == "F03" :
                Total_sum.append(169*amount)
                menu_list.remove("F03")
                menu_list.append("Salmon Steak With Sauce")
            elif menu == "F04" :
                Total_sum.append(139*amount)
                menu_list.remove("F04")
                menu_list.append("Caesar Salad")
            elif menu == "D01" :
                Total_sum.append(90*amount)
                menu_list.remove("D01")
                menu_list.append("Sparkling Sunset")
            elif menu == "D02" :
                Total_sum.append(60*amount)
                menu_list.remove("D02")
                menu_list.append("Coke Mojito")
            order_sum = sum(Total_sum)
            break
        else :
            print("Please Input Something in menu")
            menu = input("Menu ID : ").upper()
            amount = int(input("Amount : "))
            yes_no = input("Next Order(Y/N) : ").upper()
    else :
        print("Please Input Y (Yes) and N (No)")
        menu = input("Menu ID : ").upper()
        amount = int(input("Amount : "))
        yes_no = input("Next Order(Y/N) : ").upper()

print("-"*52)
Member = input("ITI Member Card (Y/N) : ")
print("-"*52)

print(Tittle_2)
while i < len(menu_list):
    print(f"{menu_list[i]:<24} {amount_list[i]:<16} {Total_sum[i]:<20}")
    i = i+1
print("-"*52)

if Member == "Y":
    discount = order_sum * 0.1
tax = order_sum * 0.07
net_total = (order_sum + tax) - discount
# ---- Display Test --------        
print(f"{"Total":<40}{order_sum:>8.2f}")
print(f"{"Tax(7%)":<40}{tax:>8.2f}")
print(f"{"Discount(10%)":<40}{discount*-1:>8.2f}")
print(f"{"Net Total ":<40}{net_total:>8.2f}")




# print("Menu List ",menu_list)
# print("Amount list ",amount_list)
# print("Total sum",Total_sum)
# while yes_no == "Y" or "N" :
#     if yes_no == "N":