print("-"*45)
with open ("data/information.txt","r") as file :
    data = file.readlines()
    sum,max = 0,0
    for line in data :
        word = line.split()
        print(word[3],word[0],word[1],word[2])
        sum = sum + int(word[3])
        if int(word[3]) > max  :
            max = int(word[3])
print("-"*45)
print(f"The average age : {sum/len(data):0.2f}, the hightest age : {max} ")
print("-"*45)