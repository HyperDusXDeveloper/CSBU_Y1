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

# def main() :
#     print("Login Succeed !")

def regester():
    title(3)
    check_username_found = True
    while check_username_found :
        with open("data_user.txt","r") as file :
            username = input("Please Enter Username : ")
            data = file.readlines()
            check_username = False
            for i in data :
                item = i.split()
                if username == item[0] :
                    check_username = True

            if check_username :
                print("This Username Already Exists!")
            else :
                check_username_found = False
                
    password = input("Please Enter Password : ")

    check_password_found = True
    while check_password_found :
        confirm_password = input("Please Confirm Password : ")
        if password != confirm_password :
            print("Invalid Confirm Password Please Try Again.")
        else :
            print("Regester Succeed !")
            check_password_found = False
            
    with open("data_user.txt","a") as file :
        file.write(f"{username} {password}\n")

def login() :
    title(4)
    username = input("Please Enter Username : ")
    password = input("Please Enter Password : ")
    with open("data_user.txt","r") as file :
        data = file.readlines()
        check_fail = True
        for i in data :
            item = i.split()
            if username == item[0] and password == item[1] :
                print("Login Succeed !")
                check_fail = False
                
        if check_fail :
            print("Invalid Try Again.")

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
    