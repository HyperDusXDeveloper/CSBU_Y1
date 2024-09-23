slist = [] #Subject
clist = [] #Credit
glist = [] #Gread
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
amt = int(input("\n Enter Total Subject : "))
for i in range (amt) :
    subject = input(f"Enter Subject {i+1} > ")
    credit = int(input("Enter credit : "))
    grade = input("Enter grade : ").upper()
    print("="*50)
    #add data into the list
    slist.append(subject)
    clist.append(credit)
    glist.append(grade)
#Display
# print(slist)
# print(clist)
# print(glist)
stotal = 0
ctotal = 0
for i in range(amt) :
    if glist[i] == "A" :
        stotal = stotal + (4.0*clist[i])
        ctotal = ctotal + clist[i]
    elif glist[i] == "B+" :
        stotal = stotal + (3.5*clist[i])
        ctotal = ctotal + clist[i]
    elif glist[i] == "B" :
        stotal = stotal + (3*clist[i])
        ctotal = ctotal + clist[i]
    elif glist[i] == "C+" :
        stotal = stotal + (2.5*clist[i])
        ctotal = ctotal + clist[i]
    elif glist[i] == "C" :
        stotal = stotal + (2.0*clist[i])
        ctotal = ctotal + clist[i]
    elif glist[i] == "D+" :
        stotal = stotal + (1.5*clist[i])
        ctotal = ctotal + clist[i]
    elif glist[i] == "D" :
        stotal = stotal + (1.0*clist[i])
        ctotal = ctotal + clist[i]
    elif glist[i] == "F" :
        ctotal = ctotal + clist[i]
#Display the output
print(title2)
print('Student ID : ',id)
for i in range(amt) :
    print(f"{slist[i]:<40} {clist[i]:<7} {glist[i]:<7}")
print("="*50)
print(f"{'GPA':>25} : {stotal/ctotal:0.2f}")
print("="*50)