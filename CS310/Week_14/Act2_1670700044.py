def getdata (ftime,ptime):
    with open("profile.txt" , "r") as file1:
        data = file1.readlines()
        for line in data :
            item = line.split()
            name = item[1]+ " " +item[2]
            com = int(item[5])*0.1
            income = int(item[4]) + com
            if item[3] == "F" :
                ftime.append([name,item[4],item[5],income])
            else :
                ptime.append([name,item[4],item[5],income])
def write2file(cuslist,filename) :
    with open(filename,"w") as file :
        for i in cuslist :
            file.write(f"{i[0]:<20}{int(i[1]):>10.2f}{int(i[2]):>10.2f}{i[3]:>10.2f}\n")
            # print(i)

# main
ftime,ptime = [],[]
getdata(ftime,ptime)
write2file(ftime,"fulltime.txt")
write2file(ptime,"pasttime.txt")

