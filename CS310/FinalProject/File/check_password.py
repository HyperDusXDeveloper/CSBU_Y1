password = input("Please Enter Password : ")
check_password_found = False
while not check_password_found:
    confirm_password = input("Please Confirm Password : ")
    for check in password:
        if confirm_password == password: 
            print("Password match found!")
            check_password_found = True
            break  
    if not check_password_found:
        print("Invalid password, please try again.")

# def regester():
#     title(3)
#     username = input("Please Enter Username : ")
#     password = input("Please Enter Password : ")
#     check_password_found = False
#     while not check_password_found:
#         confirm_password = input("Please Confirm Password : ")
#         for check in password:
#             if confirm_password == password: 
#                 print("Regester Succeed !")
#                 check_password_found = True 
#                 break
#         if not check_password_found:
#             print("Invalid Confirm Password Please Try Again.")