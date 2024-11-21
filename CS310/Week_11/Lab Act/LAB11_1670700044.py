with open("Week_11/data/employee.txt", "w") as file1:
    file1.write(f"No.     Name         Surname           Username      Password      ID Card\n")
# with open("Week_11/data/employee_output.txt", "w") as file1:
#     file1.write(f"No.     Name         Surname           Username      Password      ID Card\n")
i = 0
info = []
Tittle_start = '''1 Register Employee
2 Delete Employee 
3 Show Data Employee 
4 Exit Program '''
title_menu_1 = '''
=====================================================================
                        REGISTER EMPLOYEE
====================================================================='''
title_menu_2 = '''
=====================================================================
                        DELETE EMPLOYEE
=====================================================================
    '''
title_5 = '''
=====================================================================
Program exit.
===================================================================== '''
print("================= Welcome Employee System Program ===================")
print(Tittle_start)
select_menu = int(input("Please select menu[1-4] : "))

while select_menu > 0:
    if select_menu in [1, 2, 3, 4]:
        if select_menu == 1:
            data = []
            print(title_menu_1)
            name = input("Enter Name Surname  : ")
            id_card = input("Enter ID Card  [13 digits]: ")
            while len(id_card) != 13:
                print("Invalid ID Card")
                id_card = input("Enter ID Card  : ")

            name_username = name
            name_password = name
            name = name.split()
            index = name_username.find(" ")

            if index > -1:
                username = name_username[0:index-1] + "." + name_username[index+1]

            len_namenum_password = len(name_password)
            password_num1 = name_password[1].lower()
            password_num2 = name_password[3].upper()
            password_num3 = name_password[2].upper()
            lennamenum = str(len_namenum_password)
            password_num4 = name_password[4].lower()
            password = password_num1 + password_num2 + password_num3 + lennamenum + password_num4

            i = i + 1
            data.extend([i, name[0].lower(), name[1].lower(), username.lower(), password, id_card])
            # print(data)

            info.append(data)

            with open("Week_11/data/employee.txt", "a") as file1:
                file1.write(f"{data[0]:<5}   {data[1]:<7}    {data[2]:<17} {data[3]:<13} {data[4]:<13} {data[5]:<25}\n")
                # print(info)

            print("Register Complete")
            print("=" * 69)

        elif select_menu == 2:
            print(title_menu_2)
            while True:
                del_employee = input("Enter first name of Employee to delete : ").lower()
                matching_employee = [line for line in info if line[1] == del_employee]
                if matching_employee:
                    info = [line for line in info if line[1] != del_employee]
                    i = i-1
                    print("Delete complete")
                    print("=" * 69)
                    break
                else:
                    print("Invalid name !! ")

        elif select_menu == 3:
            print("=" * 69)
            print("\nAll data is displayed in the employee.txt\n")
            with open("Week_11/data/employee_output.txt", "w") as file1:
                file1.write(f"No.     Name         Surname           Username      Password      ID Card\n")
                for line in info:
                    file1.write(f"{line[0]:<5}   {line[1]:<7}    {line[2]:<17} {line[3]:<13} {line[4]:<13} {line[5]:<25}\n")
                print("=" * 69)
        elif select_menu == 4:
            print(title_5)
            break
    else:
        print("=" * 69)
        print("\nIncorrect menu!!\n")
        print("=" * 69)
        
    print(Tittle_start)
    select_menu = int(input("Please select menu[1-4]  : "))

