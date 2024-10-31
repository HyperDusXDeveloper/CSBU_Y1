with open("data/exam_scores.txt","r") as file1 : 
    with open("data/gragereport.txt","w") as file2 :#output
        data = file1.read() .split("\n")
        for line in data :
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
            file2.write(f"{item[0]:12} {item[1]:<20} {total:<5} {grade:<5}\n")