studentlist = []
with open ('Week_10/data/student_info.txt','r') as file1 :
    with open('data/exam_scores.txt','r') as file2 :
        data1 = file1.read() .splitlines()
        for line in data1 :
            item = line.split(", ")
            # print(item)
            studentlist.append([item[0],item[1],item[2]])
        # for i in studentlist :
        #     print(studentlist)
        data2 = file2.read().splitlines()
        index = 0 
        for line in data2 :
            item = line.split(", ")
            # print(item)
            total = int(item[2]) + int(item[3])
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
            studentlist[index].append(total)
            studentlist[index].append(grade)
            index = index + 1 

# for i in studentlist :
#     # print(i)
with open("data/gradereport2.txt","w") as file3 :
    for student in studentlist :
        file3.write(f"{student[0]:<12} {student[1]:<20} {student[2]:>3} {student[3]:>5.2f} {student[4]:>4}\n")