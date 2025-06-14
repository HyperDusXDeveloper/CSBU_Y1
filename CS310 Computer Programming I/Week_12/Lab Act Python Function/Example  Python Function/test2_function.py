def oddeven(number) :
    if number%2 == 0 :
        print("Even")
    else :
        print("Odd")

def oddeven2(number) :
    if number%2 == 0 :
        return("Even")
    else :
        return("Odd")

# #main Program
# oddeven(2)
# oddeven(3)
# result1 = oddeven2(2)
# result2 = oddeven2(3)
numbers = [10,11,12,13,14,15]
for i in range(len(numbers)):
    result = oddeven2(numbers[i])
    print("Result = " , result)