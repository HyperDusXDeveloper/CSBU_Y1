def menu() :
    print('''------------------------------------------------------------------
                            Menu
------------------------------------------------------------------
C : Circle Area
T : Triangle Area
R : Rectangle Area 
E : Exit 
------------------------------------------------------------------''')
    
def Circle() :
    print ('''
------------------------------------------------------------------
                        Output of Circle
------------------------------------------------------------------''')

def Triangle() :
    print ( '''
------------------------------------------------------------------
                        Output of Triangle
------------------------------------------------------------------''')

def rectangle() :
    print ('''
------------------------------------------------------------------
                        Output of rectangle
------------------------------------------------------------------''')

def inputmenu() :
    menu_input = input("Enter menu : ")
    return(menu_input.upper())

def inputarea(menu_input) :

    if menu_input == "C" :
        radius = float(input("Enter Radius : "))
        Circle()
        return(radius)
    
    elif menu_input == "T" :
        base = float(input("Enter Base : "))
        height = float(input("Enter Height : "))
        Triangle()
        return(base ,height)
    
    elif menu_input == "R" :
        width = float(input("Enter Width : "))
        length = float(input("Enter Length : "))
        rectangle()
        return(width , length)

def calculateCircle(radius):
        circle_sum = (22/7) * radius**2
        print(f"{ 'Output of Circle = '}  {circle_sum:.2f}".center(60))
        return(circle_sum)

def calculateTriangle(base , height):
        Triangle_sum = 1/2 * base * height
        print(f"{ 'Output of Triangle = '} {Triangle_sum:.2f}".center(70))
        return(Triangle_sum)

def calculateRectangle(width , length):
        rectangle_sum = width * length
        print(f"{ 'Output of Triangle = '} {rectangle_sum:.2f}".center(70))
        return(rectangle_sum)

CalculatorRun = True
while CalculatorRun :

    menu()
    menu_input = inputmenu()

    if menu_input == "C" :
        radius  = inputarea(menu_input)
        circle_sum = calculateCircle(radius)

    elif menu_input == "T" :
        base , height  = inputarea(menu_input)
        Triangle_sum = calculateTriangle(base , height)

    elif menu_input == "R" :
        width , length  = inputarea(menu_input)
        rectangle_sum = calculateRectangle(width , length)

    elif menu_input == "E" :
        CalculatorRun = False

    else :
        print("ERROR !!! ")
