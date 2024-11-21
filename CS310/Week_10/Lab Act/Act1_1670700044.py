with open("data/score.txt" , "r") as file1 : #input
    with open("data/report.txt" , "w") as file2 : #output
        # data = file1.readlines()
        data = file1.read() .splitlines()
        for line in data :
            item = line.split(", ")
            # print(item)
            if int(item[1]) >= 80 :
                file2.write(f"{item[0]:12} {item[1]:>4} {'A':>3}\n")
            else : 
                file2.write(f"{item[0]:12} {item[1]:>4} {'-':>3}\n")