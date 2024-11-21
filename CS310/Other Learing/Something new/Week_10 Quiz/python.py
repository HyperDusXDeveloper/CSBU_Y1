with open("Week_10 Quiz/data/Score.txt" , "r") as file :
    data_Score = file.readlines()
    print(data_Score)
    for line in data_Score :
        word = line.split()
        print(word[1])