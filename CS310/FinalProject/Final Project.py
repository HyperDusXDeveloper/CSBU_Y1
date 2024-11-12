import random
import hashlib

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
        print(f"คำใบ้: {hint}")
    else:
        # Hint in hard mode is the first few letters only
        print(f"คำใบ้: {hint[:len(hint)//2]}...")

def guess_word(word):
    attempts = 0
    while True:
        guess = input("ทายคำศัพท์: ")
        attempts += 1
        if guess.lower() == word.lower():
            print(f"ถูกต้อง! คุณทายคำศัพท์ถูกใน {attempts} ครั้ง")
            return attempts
        else:
            print("ผิด! ลองใหม่")

def save_score(attempts):
    try:
        with open("score.txt", "a", encoding="utf-8") as file:
            file.write(f"ทายถูกใน {attempts} ครั้ง\n")
    except:
        print("เกิดข้อผิดพลาดในการบันทึกคะแนน")

def show_score():
    try:
        with open("score.txt", "r", encoding="utf-8") as file:
            print("ประวัติการทายคำศัพท์:")
            print(file.read())
    except FileNotFoundError:
        print("ยังไม่มีประวัติการทายคำศัพท์")

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

def register():
    users = load_users()
    username = input("กรุณากรอกชื่อผู้ใช้ใหม่: ")
    if username in users:
        print("ชื่อผู้ใช้นี้ถูกใช้แล้ว!")
        return False

    password = input("กรุณากรอกรหัสผ่าน: ")
    confirm_password = input("กรุณายืนยันรหัสผ่าน: ")
    if password == confirm_password:
        save_user(username, password)
        print("ลงทะเบียนสำเร็จ!")
        return True
    else:
        print("รหัสผ่านไม่ตรงกัน!")
        return False

def login():
    users = load_users()
    username = input("กรุณากรอกชื่อผู้ใช้: ")
    password = input("กรุณากรอกรหัสผ่าน: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in users and users[username] == hashed_password:
        print("เข้าสู่ระบบสำเร็จ!")
        return True
    else:
        print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง!")
        return False

# เพิ่มการเรียกใช้งาน login และ register ใน main function
def main():
    print("ยินดีต้อนรับสู่เกมทายคำศัพท์")
    while True:
        print("1. ลงทะเบียน")
        print("2. เข้าสู่ระบบ")
        choice = input("กรุณาเลือก (1-2): ")

        if choice == "1":
            if register():
                break
        elif choice == "2":
            if login():
                break
        else:
            print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่")
    
    # รันเกมเมื่อเข้าสู่ระบบเรียบร้อยแล้ว
    words = load_words()
    difficulty = "easy"
    
    while True:
        print("\n--- เกมทายคำศัพท์ ---")
        print("1. เริ่มเกมใหม่")
        print("2. ดูประวัติการทายคำศัพท์")
        print("3. เพิ่มคำศัพท์ใหม่")
        print("4. ลบคำศัพท์")
        print("5. รีเซ็ตคะแนน")
        print("6. ตั้งค่าการเล่นเกม")
        print("7. ออกจากเกม")
        choice = input("กรุณาเลือกคำสั่ง (1-7): ")

        if choice == "1":
            word, hint = get_random_word(words)
            display_hint(hint, difficulty)
            attempts = guess_word(word)
            save_score(attempts)
        elif choice == "2":
            show_score()
        elif choice == "3":
            add_word()
        elif choice == "4":
            delete_word()
            words = load_words()
        elif choice == "5":
            reset_score()
        elif choice == "6":
            difficulty = game_settings()
        elif choice == "7":
            print("ขอบคุณที่เล่นเกม! ลาก่อน!")
            break
        else:
            print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main()
