# Basic function

# def print_Vali() : 
#     print("Hi Atommic")
# print_Vali()



# Valable function

# def valiable_function() :
#     a = 2
#     b = 4
#     c = 6
#     sum = a+b+c
#     return(a,b,c,sum)
# a,b,c,sum= valiable_function()
# sum = sum+a+b+c+sum**sum
# print(sum)



# Arguments function

# def Arguments_function(a,b,c) : 
#     sum = a+b+c
#     return(sum)
# sum = Arguments_function(1,2,3)
# print(sum)

# def Arguments_function(name,x,y) : 
#     sum = x + y
#     print("hello",name , "sum " ,sum)

# Arguments_function("hi",10,20)


# def Arguments_functionV2(a,b,c) :
#     sum = a+b+c # 1 + 2 + 3
#     a = a + 100 # 1 + 100
#     return(a,b,c,sum) # 101 2 3 6
# a,b,c,sum = Arguments_functionV2(1,2,3)
# print(sum)
# print(a)

# def Arguments_function(name,x,y) : 
#     sum = x + y
#     z = int(input("Z : Enter number : "))
#     z = z + sum * sum
#     print("hello",name , "sum " ,sum)
#     return(z)

# x = int(input("X : Enter Number : "))
# y = int(input("Y : Enter Number : "))
# z = Arguments_function("hi",x,y)
# print("Z : Sum = " , z)

# def Arguments_function(name,x,y) : 
#     sum = x + y
#     z = int(input("Z : Enter number : "))
#     z = z + sum * sum
#     print("hello",name , "sum " ,sum)
#     return(z,x) #Local

# x = int(input("X : Enter Number : "))
# y = int(input("Y : Enter Number : "))
# z,x = Arguments_function("hi",x,y)


# def  Arguments_function_return() : 
#     z =  x * 10
#     print("Z : Sum = " , z) #Local

# Arguments_function_return()
# print(z) #Global