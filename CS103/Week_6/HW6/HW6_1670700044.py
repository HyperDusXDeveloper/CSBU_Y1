slist = [] #Subject
clist = [] #Credit
glist = [] #Gread
stotal = [] #Subject Total
ctotal = [] #Credit Total
title1 = """
=================================================
            GPA Calculator Program
=================================================
"""
title2 = """
=================================================
                Grade Report
=================================================
"""
print(title1)
id = input("Enter Student ID : ")
total_sub = int(input("\n Enter Total Subject : "))

for i in range (total_sub) :
    subject = input(f"Enter Subject {i+1} > ")
    credit = int(input("Enter credit : "))
    grade = input("Enter grade : ").upper()
    print("="*50)
    #add infomation into the list
    slist.append(subject)
    clist.append(credit)
    glist.append(grade) 
for i in range(total_sub) :
    if glist[i] == "A" :
        stotal.append(4.0 * credit)
    elif glist[i] == "B+" :
        stotal.append(3.5 * credit)
    elif glist[i] == "B" :
        stotal.append(3.0 * credit)
    elif glist[i] == "C+" :
        stotal.append(2.5 * credit)
    elif glist[i] == "C" :
        stotal.append(2.0 * credit)
    elif glist[i] == "D+" :
        stotal.append(1.5 * credit)
    elif glist[i] == "D" :
        stotal.append(1.0 * credit)
    elif glist[i] == "F" :
        stotal.append(0.0)
    else :
        continue #No Use 

    ctotal.append(credit)
#Sum Credit / Subject
ctotal = sum(ctotal)
stotal = sum(stotal)

# Display 
print(title2)
print('Student ID : ',id)
for i in range(total_sub) :
    print(f"{slist[i]:<34} {clist[i]:<7} {glist[i]:<7}")
print("="*50)
print(f"{'GPA':>25} : {stotal/ctotal:0.2f}") #Credit / Subject = GPA
print("="*50)
