# Basic function

def print_Vali() : 
    print("Hi Atommic")
print_Vali()



# Valable function

def valiable_function() :
    a = 2
    b = 4
    c = 6
    sum = a+b+c
    return(a,b,c,sum)
a,b,c,sum= valiable_function()
sum = sum+a+b+c+sum**sum
print(sum)



# Arguments function

def Arguments_function(a,b,c) : 
    sum = a+b+c
    return(sum)
sum = Arguments_function(1,2,3)
print(sum)

def Arguments_function(name,x,y) : 
    sum = x + y
    print("hello",name , "sum " ,sum)

Arguments_function("hi",10,20)


def Arguments_functionV2(a,b,c) :
    sum = a+b+c # 1 + 2 + 3
    a = a + 100 # 1 + 100
    return(a,b,c,sum) # 101 2 3 6
a,b,c,sum = Arguments_functionV2(1,2,3)
print(sum)
print(a)

def Arguments_function(name,x,y) : 
    sum = x + y
    z = int(input("Z : Enter number : "))
    z = z + sum * sum
    print("hello",name , "sum " ,sum)
    return(z)

x = int(input("X : Enter Number : "))
y = int(input("Y : Enter Number : "))
z = Arguments_function("hi",x,y)
print("Z : Sum = " , z)

def Arguments_function(name,x,y) : 
    sum = x + y
    z = int(input("Z : Enter number : "))
    z = z + sum * sum
    print("hello",name , "sum " ,sum)
    return(z,x) #Local

x = int(input("X : Enter Number : "))
y = int(input("Y : Enter Number : "))
z,x = Arguments_function("hi",x,y)


def  Arguments_function_return() : 
    z =  x * 10
    print("Z : Sum = " , z) #Local

Arguments_function_return()
print(z) #Global

# Functin txt File


def getdata() : 
    getdata_run = False
    while not getdata_run :
        with open ("deposit.txt" , "a" ) as file1 :
            with open ("withdraw.txt" , "a" ) as file2 :
                print("-"*40)
                print("TYPE PROGRAM".center(40))
                print("-"*40)
                loop = int(input("Input you loop : "))
                i = 1
                for i in range(loop) :
                    print("-"*40)
                    detail = input("สินค้า Detail : ")
                    print(f"E : Exit ")
                    typeDW = input("ประเภท Type (D/W): ").lower()
                    if typeDW == "e" :
                        getdata_run = True
                        break
                    total  = int(input("ราคารวม Total amount : "))
                    if typeDW == "d" :
                        file1.write(f"{detail:<20} {typeDW:<20} {total:<20.2f}\n")
                    elif typeDW == "w" :
                        file2.write(f"{detail:<20} {typeDW:<20} {total:<20.2f}\n")

                    else :
                        print("Try Again")
                    print(f"รอบที่ {i}")
getdata()


def getdata(p6,p5,oth) :
    with open ("point.txt" , "r") as file1 :
        data = file1.readlines()
        print(data)
        for line in data :
            item = line.split()

            print(item)
            name = item[1]
            sumpoint = int(item[2]) +  int(item[3]) + int(item[4])
            if item[5] == "P6" :
                p6.append([name,sumpoint,item[5]])
            elif item[5] == "P5" :
                p5.append([name,sumpoint,item[5]])
            else :
                oth.append([name,sumpoint,item[5]])
            print(p6)


def writhfile(p,nametxt) :
    with open (nametxt , 'w') as file2 :
        for i in p :
            file2.write(f"{i[0]:<20} {i[1]:<20} {i[2]:<20}\n")

p6,p5,oth = [],[],[]
getdata(p6,p5,oth)
writhfile(p6,"P6.txt")
writhfile(oth,".txt")


def getdata(deposit,withdraw) :
    amt = int(input("Please input loop "))
    for i in range(amt) :
        detail = input("สินค้า Detail : ")
        type = input("ประเภท Type (D/W): ").lower()
        total  = int(input("ราคารวม Total amount : "))
        if type == "d" :
            deposit.append([detail,type,total])
        elif type == "w" :
            withdraw.append([detail,type,total])

deposit,withdraw = [],[]

def write2file(list , filename) :
    with open (filename , "w") as file1 :
        for i in list :
            file1.write(f"{i[0]}  {i[1]} {i[2]} \n")

getdata(deposit,withdraw)
write2file(deposit,"deposit.txt")
write2file(withdraw,"withdraw.txt")