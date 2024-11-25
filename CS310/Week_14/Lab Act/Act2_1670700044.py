def getdata (ftime,ptime): #อกิวเม้นเป็น List ที่ส่งค่าเข้า
    with open("profile.txt" , "r") as file1: # เปิดไฟล์ Profile
        data = file1.readlines() 
        for line in data :
            item = line.split()
            
            #item[1] ID , # item[2] Name , item[3] lastname , item[4] Work F/P , item[5] คอมมิสชั่น , item[6] รายได้

            name = item[1]+ " " +item[2]
            com = int(item[5])*0.1
            income = int(item[4]) + com

            if item[3] == "F" :
                ftime.append([name,item[4],item[5],income]) 
            else :
                ptime.append([name,item[4],item[5],income])
            print("ftime ",ftime)
            print("ptime ",ptime)

def write2file(fulltime_pasttimelist,filename) :
    with open(filename,"w") as file :
        for i in fulltime_pasttimelist :
            file.write(f"{i[0]:<20}{int(i[1]):>10.2f}{int(i[2]):>10.2f}{i[3]:>10.2f}\n")
            # print(i)

# main
ftime,ptime = [],[] #List ftime,ptime 
getdata(ftime,ptime) #ส่งค่า list ftime,ptime เข้า อกิวเม้น
write2file(ftime,"fulltime.txt")
write2file(ptime,"pasttime.txt")

