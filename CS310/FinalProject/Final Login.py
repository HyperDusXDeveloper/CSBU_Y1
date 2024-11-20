# Random Word 
def title(title_num):
    if title_num == 1 : # Start Game Word Guessing Game MENU
       print("-"*40)
       print(f"- Word Guessing Game - ".center(40))
    elif title_num == 2 : # Menu login Register Exit
        print(f"- SELECT MENU -".center(40))
        print("-"*40)
        print(f"1 Register\n2 Login\n3 Exit")
        print("-"*40)
    elif title_num == 3 : # REGESTER MAIN
       print("-"*40)
       print(f"REGESTER".center(40))
       print("-"*40)
    elif title_num == 4 : # LOGIN MAIN
       print("-"*40)
       print(f"LOGIN".center(40))
       print("-"*40)
    elif title_num == 5 : # Game Menu 
        print(f"- SELECT MENU -".center(40))
        print("-"*40)
        print(f"1 Play\n2 Profile\n3 Logout")
        print("-"*40)

def regester():
    title(3)
    username = input("Please Enter Username : ")
    password = input("Please Enter Password : ")
    check_password_found = False
    while not check_password_found:
        confirm_password = input("Please Confirm Password : ")
        for check in password:
            if confirm_password == password: 
                print("Regester Succeed !")
                check_password_found = True
                break  
        if not check_password_found:
            print("Invalid Password Please Try Again.")


def login() :
    title(4)
    username = input("Please Enter Username : ")
    password = input("Please Enter Password : ")



def login_main():
    login_run = True
    while login_run :
        title(1)
        title(2)
        user_input = int(input("Please Choich Number : "))
        if user_input == 1 :
            regester()
        elif user_input == 2 :
            login()
        elif user_input == 3 :
            login_run = False
        else :
            print("Incorrect Menu !! Pleasse Try Again ")
        
login_main()

