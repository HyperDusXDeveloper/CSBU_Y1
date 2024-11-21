import random
import hashlib

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

def play():
    global score
    words = []
    with open("words.txt", "r") as file:
        for line in file:
            word, hint = line.strip().split(":")
            words.append((word, hint))
            
    for i in range(10) :
        word, hint = random.choice(words)
        print(f"คำใบ้: {hint}")
        guess = input("ทายคำศัพท์: ")
        if guess.lower() == word.lower():
            score += 1
            print(f"ถูกต้อง! คุณทายคำศัพท์ถูก")
        else:
            score -= 1
            print("ผิด! ลองใหม่")
        print(score)

    save_user(user, score)

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
        file.write(f"{username} {password} 0\n")

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
                global check_login
                global user
                global score
                check_login = False
                user = username
                score = int(item[2])
                
        if check_fail == True:
            print("Invalid Confirm Password Please Try Again.")

def save_user(username, score):
    info = []
    with open("data_user.txt","r") as file :
        data = file.readlines()
        for i in data :
            item = i.split()
            if username == item[0] :
                info.append([item[0],item[1],score])
            else :
                info.append([item[0],item[1],item[2]])

    with open("data_user.txt","w") as file :
        for item in info :
            if username == item[0] :
                file.write(f"{item[0]} {item[1]} {item[2]}\n")
            else :
                file.write(f"{item[0]} {item[1]} {item[2]}\n")

def profile():
    print('Username : ',user)
    print('Score : ',score)
    # print('score1')
    # print('score2')
    # print('score3')


user = ''
score = 0

check_login = True
main_menu = True
while main_menu :
    if check_login :
        title(1)
        title(2)
        user_input = input("Please Choich Number : ")
        if user_input == "1" :
            regester()
        elif user_input == "2" :
            login()
        elif user_input == "3" :
            main_menu = False
        else :
            print("Incorrect Menu !! Pleasse Try Again ")
    else :
        title(5)
        user_input = input("Please Choich Number : ")
        if user_input == "1" :
            print('Play')
            play()
        elif user_input == "2" :
            print('Profile')
            profile()
        elif user_input == "3" :
            print('Logout')
            user = ''
            score = 0
            check_login = True
        else :
            print("Incorrect Menu !! Pleasse Try Again ")