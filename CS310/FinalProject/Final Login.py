import random

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
    global total_score
    global fail_score
    global nc_score
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
            total_score += 1
            nc_score += 1
            print(f"ถูกต้อง! คุณทายคำศัพท์ถูก")
            print("Score +1")
        else:
            score -= 1
            total_score += 1
            fail_score += 1
            print("ผิด! ลองใหม่")
            print("Score -1")

    save_user()

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
        file.write(f"{username} {password} 0 0 0 0\n")

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
                global total_score
                global fail_score
                global nc_score
                check_login = False
                user = item[0]
                score = int(item[2])
                total_score = int(item[3])
                fail_score = int(item[4])
                nc_score = int(item[5])
                
        if check_fail == True:
            print("Invalid Confirm Password Please Try Again.")

def save_user():
    info = []
    with open("data_user.txt","r") as file :
        data = file.readlines()
        for i in data :
            item = i.split()
            if user == item[0] :
                info.append([item[0],item[1],score,total_score,fail_score,nc_score])
            else :
                info.append([item[0],item[1],item[2],item[3],item[4],item[5]])

    with open("data_user.txt","w") as file :
        for item in info :
            file.write(f"{item[0]} {item[1]} {item[2]} {item[3]} {item[4]} {item[5]}\n")

def profile():
    print('Username : ',user)
    print('Score : ',score)
    print('Succeed : ',nc_score)
    print('Fail : ',fail_score)
    print('Total : ',total_score)

user = ''
score = 0
total_score = 0
fail_score = 0
nc_score = 0

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
            total_score = 0
            fail_score = 0
            nc_score = 0
            check_login = True
        else :
            print("Incorrect Menu !! Pleasse Try Again ")