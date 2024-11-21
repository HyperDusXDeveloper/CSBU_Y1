info = []

def showmenu():
    print("1 Register Employee")
    print("2 Delete Employee")
    print("3 Show Data Employee")
    print("4 Exit Program")

def register():
    name = input("Enter Name Surname : ")
    check_idcard = True
    while check_idcard :
        idcard = input("Enter ID card [13 digits] : ")
        if len(idcard) != 13 :
            print("Invalid ID card")
        else :
            check_idcard = False
    firstname,lastname = name.split()
    username = firstname  + "." + lastname[0]
    password = firstname[1].lower() + firstname[3].upper() + firstname[2].upper() + str(len(name)) + firstname[4].lower()
    userid = firstname + " " + lastname + " " + username + " " + password + " " + idcard
    info.append(userid)
    print("Register Complete")
    print("="*80)

def delete():
    check_name = True
    while check_name:
        name = input("Enter name of employee to delete: ")
        found = False
        updated_info = []
        for line in info:
            item = line.split()
            if item[0] == name:
                print("Delete Complete")
                print("="*80)
                found = True
                check_name = False
            else:
                updated_info.append(line)
        if not found:
            print("Invalid name !!")
        else:
            info.clear()
            info.extend(updated_info)

def show():
    index = 1
    with open("employee.txt", "w") as file:
        file.write(f"{'No.':<5} {'Name':<15} {'Surname':<15} {'Username':<15} {'Password':<10} {'ID Card'}\n")
        for line in info :
            item = line.split()
            file.write(f"{index:<5} {item[0]:<15} {item[1]:<15} {item[2]:<15} {item[3]:<10} {item[4]}\n")
            index += 1

print("========================Welcome Employee System Program=========================")

check_exit = True
while check_exit :
    showmenu()
    nummenu = int(input("Please select menu[1-3] : "))
    if nummenu == 1 :
        print("="*80)
        print(f"{'REGISTER EMPLOYEE':>47}")
        print("="*80)
        register()
    elif nummenu == 2 :
        print("="*80)
        print(f"{'DELETE EMPLOYEE':>45}")
        print("="*80)
        delete()
    elif nummenu == 3 :
        print("="*80)
        print("All data display in the employee.txt")
        print("="*80)
        show()
    elif nummenu == 4 :
        print("="*80)
        print("Program exit.")
        print("="*80)
        check_exit = False
    else :
        print("="*80)
        print("Incorrect menu!!")
        print("="*80)
