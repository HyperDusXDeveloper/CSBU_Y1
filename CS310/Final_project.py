import random
import hashlib

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

def load_words():
    words = []
    with open("words.txt", "r", encoding="utf-8") as file:
        for line in file:
            word, hint = line.strip().split(":")
            words.append((word, hint))
    return words

def get_random_word(words):
    return random.choice(words)

def display_hint(hint, difficulty="easy"):
    if difficulty == "easy":
        print(f"Hint : {hint}")
    else:
        # Hint in hard mode is the first few letters only
        print(f"Hint : {hint[:len(hint)//2]}...")

def guess_word(word):
    attempts = 0
    while True:
        guess = input("Input Guess The Word")
        attempts += 1
        if guess.lower() == word.lower():
            print("-"*40)
            print(f"- Perfect - ".center(40))
            print(f"That's right ! Now You Have Guessed The Word Correctly ( {attempts} ) Time")
            return attempts
        else:
            print("-"*40)
            print(f"- Nice Try - ".center(40))
            print(f"- Please Try Again - ".center(40))

def save_score(attempts):
    try:
        with open("score.txt", "a", encoding="utf-8") as file:
            file.write(f"You Have Guessed The Word Correct ! {attempts} Time\n")
    except:
        print("An Error Occurred While Saving The Score.")

def show_score():
    try:
        with open("score.txt", "r", encoding="utf-8") as file:
            print("History Of Word Guessing:")
            print(file.read())
    except FileNotFoundError:
        print("There Is No History Of Guessing Words.")

def add_word():
    word = input("กรุณาป้อนคำศัพท์ใหม่: ")
    hint = input("กรุณาป้อนคำใบ้สำหรับคำศัพท์นี้: ")
    with open("words.txt", "a", encoding="utf-8") as file:
        file.write(f"{word}:{hint}\n")
    print("เพิ่มคำศัพท์ใหม่เรียบร้อยแล้ว")

def delete_word():
    word_to_delete = input("กรุณาป้อนคำศัพท์ที่ต้องการลบ: ")
    words = load_words()
    with open("words.txt", "w", encoding="utf-8") as file:
        for word, hint in words:
            if word.lower() != word_to_delete.lower():
                file.write(f"{word}:{hint}\n")
    print("ลบคำศัพท์เรียบร้อยแล้ว")

def reset_score():
    with open("score.txt", "w", encoding="utf-8") as file:
        file.write("")
    print("รีเซ็ตคะแนนทั้งหมดเรียบร้อยแล้ว")

def game_settings():
    difficulty = input("เลือกระดับความยาก (ง่าย/ยาก): ").strip().lower()
    if difficulty == "ง่าย":
        return "easy"
    else:
        return "hard"

def load_users():
    users = {}
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                username, hashed_password = line.strip().split(":")
                users[username] = hashed_password
    except FileNotFoundError:
        pass  # ถ้าไฟล์ยังไม่ถูกสร้าง ให้ข้ามไปก่อน
    return users

def save_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("users.txt", "a", encoding="utf-8") as file:
        file.write(f"{username}:{hashed_password}\n")

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
    while check_password_found : #เช็ค Passwords
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
                return True

        if check_fail == True:
            print("Username or password is incorrect. Please try again.")
            return False

def main():
    login_run = True
    while True:
        title(1)
        title(2)
        choice = (input("Please Choich Number : "))

        if choice == "1" :
            if regester() :
                break
        elif choice == "2" :
            if login() :
                break
        elif choice == "3" :
            if login_run == False :
                break
        else :
            print("Incorrect Menu !! Pleasse Try Again ")

    words = load_words()
    difficulty = "easy"
    
    while True:
        title(1)
        print(f"1 Start Game\n2 Profile\n3 Check Score\n4 Log Out")
        choice = input("Please Choich Number : ")

        if choice == "1":
            word, hint = get_random_word(words)
            display_hint(hint, difficulty)
            attempts = guess_word(word)
            save_score(attempts)
        elif choice == "2":
            print("-"*40)
            print(f"- Profile - ".center(40))
            print("-"*40)
        elif choice == "3":
            print(f"- Score - ".center(40))
            show_score()
        elif choice == "4":
            print("Log Out Succeed ! ")
            break
        else:
            print("Invalid Choice Please try again.")
            
if __name__ == "__main__":
    main()

        # if choice == "1":
        #     word, hint = get_random_word(words)
        #     display_hint(hint, difficulty)
        #     attempts = guess_word(word)
        #     save_score(attempts)
        # elif choice == "2":
        #     show_score()
        # elif choice == "3":
        #     add_word()
        # elif choice == "4":
        #     delete_word()
        #     words = load_words()
        # elif choice == "5":
        #     reset_score()
        # elif choice == "6":
        #     difficulty = game_settings()
        # elif choice == "7":
        #     print("ขอบคุณที่เล่นเกม! ลาก่อน!")
        #     break
        # else:
        #     print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่")