with open("data/custormer.txt") as file1 :
    data = file1.readlines()
    # print(data) 
    male,female = 0,0
    salary = 0 
    for line in data :
        item = line.split()
        # print(item)
        if item[3] == "M" :
            male = male + 1 
        else :
            female = female + 1
        salary = salary + int(item[5])
with open("data/summary.txt","w") as file2 :
    file2.write(f"Total male = {male} , Total female = {female}\n")
    file2.write(f"Average of salary = {salary/(male+female):0.2f}")

# print("-" * 45 )
# print(f"Total male = {male} , Total female = {female}")
# print(f"Average of salary = {salary/(male+female):0.2f}")
# print("-" * 45 )