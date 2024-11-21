print("-"*47)
print(f"{'|***':<5} {'Area of Calculator Program':>30} {'***|':>10}")
print("-"*47)
print(f"{'|':<3} {'Shape code list :':<16} {'|':>25}")
print(f"{'|':<4} {'(R)Rectangle':<16} {'|':>25}")
print(f"{'|':<4} {'(T)Trapezoid':<16} {'|':>25}")
print(f"{'|':<4} {'(P)Parallelogram':<16} {'|':>25}")
print(f"{'|':<4} {'(C)Circle':<16} {'|':>25}")
print("-"*47)
code = input("Select Code [ R , T . P , C ] : ")
if code == "R" or code == "r" :
    print("R = Rectangle")
    print("\n")
    width = int(input("Enter width : "))
    height = int(input("Enter Height : "))
    
    area = width * height

    print("="*30)
    print(f"{'Area':>13} = {area:.2f}")
    print("="*30)
    
elif  code == "T" or code == "t" :
    print(" T = Trapezoid")
    Prallel_A = int(input("Enter Prallel side (A): "))
    Prallel_B = int(input("Enter Prallel side (B): "))
    height = int(input("Enter Height : "))
    Prallelbase = Prallel_A + Prallel_B
    area = 1/2*Prallelbase*height

    print("="*30)
    print(f"{'Area':>13} = {area:.2f}")
    print("="*30)


elif  code == "P" or code == "p" :
    print(" P = Prallelogram ")
    print("\n")
    base = int(input("Enter base : "))
    height = int(input("Enter Height : "))
    area = base * height

    print("="*30)
    print(f"{'Area':>13} = {area:.2f}")
    print("="*30)
    


elif  code == "C" or code == "c" :
    print(" C = Circle")
    print("\n")
    radius = int(input("Enter radius :"))
    area = 3.1625 * radius**2

    print("="*30)
    print(f"{'Area':>13} = {area:.2f}")
    print("="*30)

else : 
    print("Invalid shape code !")
    print("Please try again ")

