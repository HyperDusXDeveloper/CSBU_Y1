numsum = 0
loop = int(input("Enter loop : "))
for i in range (loop) :
        num = int(input(f"Loop : {i+1}  > Enter Number : "))
        numsum = numsum + num
        print(f"Loop : {i+1}  = {numsum}")
        