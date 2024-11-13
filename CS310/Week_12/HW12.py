title_1 = '''
------------------------------------------------------------------
                            Menu
------------------------------------------------------------------
C : Circle Area
T : Triangle Area
R : Rectangle Area 
E : Exit 
------------------------------------------------------------------'''

output_circle = '''
------------------------------------------------------------------
                        Output of Circle
------------------------------------------------------------------'''

output_triangle = '''
------------------------------------------------------------------
                        Output of Triangle
------------------------------------------------------------------'''

output_rectangle = '''
------------------------------------------------------------------
                        Output of rectangle
------------------------------------------------------------------'''

# i = 1
# while i > 0 :
# while i > 1 :
print(title_1)
def Function_input_Area() :
    menu_input = input("Enter menu : ")
    return(menu_input.upper())

def function_if(menu_input) :
    if menu_input == "C" :
        radius = int(input("Enter Radius : "))
        print(output_circle)
        return(radius)
    elif menu_input == "T" :
        base = int(input("Enter Base : "))
        height = int(input("Enter Height : "))
        print(output_triangle)
        return(base,height)
    elif menu_input == "R" :
        width = int(input("Enter Width : "))
        length = int(input("Enter Length : "))
        print(output_rectangle)
        return(width,length)
    # elif menu_input == "E" :
    else :
         print("ERROR !!!")
    # return(radius , base , height , width , length)

def calculate_area(radius , base , height , width , length):
    if menu_input == "C" :
        circle_sum = (22/7) * radius**2
        print(f"{ 'Output of Circle = '}:>20 {circle_sum}")
    return(circle_sum)

menu_input = Function_input_Area()
som1 , som2 = function_if(menu_input)
circle_sum = calculate_area()
# Circle , Triangle , Rectangle