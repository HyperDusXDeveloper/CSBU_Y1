with open ("Week_9/data/students.txt","r") as file :
    info_students = file.readlines()
    for line in info_students :
        word = line.split()
        if float(word[4]) < 2.0 :
            print(f"Retention >> {word[4]} Information : {word[0]} {word[1]} {word[2]} ")