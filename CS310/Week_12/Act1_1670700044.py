def getinput():
    mid = float(input("Enter Midterm Score : "))
    final = float(input("Enter final Score : "))
    ass = float(input("Enter assignment Score : "))
    return(mid,final,ass)

def summation(mid,final,ass):
    total = mid + final + ass
    return(total)

def cal_gread(total):
    if total >= 80 :
        grade = "A"
    elif total >= 70 :
        grade = "B"
    elif total >= 60 :
        grade = "C"
    elif total >= 50 :
        grade = "D"
    else : 
        grade = "F"
    return(grade)

def display(total , grade ):

    print("-"*45)
    print(f"Total = {total} : Grade = {grade}")
    print("-"*45)

#main Function
mid,final,ass = getinput()
total = summation(mid,final,ass)
print("total : " ,total)
grade = cal_gread(total)
display(total,grade)