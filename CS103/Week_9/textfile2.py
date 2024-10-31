# with open("data/test1.txt","r") as file1 :
#     print("hello1")
#     data1 = file1.read()
#     print(data1)
# with open("data/information.txt","r") as file2 :
#     print("hello2")

# with open("data/infomation.txt","r") as file1 :
#     print("hello1")
#     data1 = file1.read()
#     print(data1)
# with open("data/infomation.txt","r") as file2 :
#     print("hello3")
#     data = file1.read()
#     print(data)

with open("data/information.txt","r") as file2 :
    print("hello4")
    data = file2.readline()
    print("Total student = ",len(data))
    for line in data :
        word = line.split()
        print("ID = " , word[0],"Age = " ,word[3])
        if word[3] >= '20' :
            print("WOWW")
        print(type(line))

