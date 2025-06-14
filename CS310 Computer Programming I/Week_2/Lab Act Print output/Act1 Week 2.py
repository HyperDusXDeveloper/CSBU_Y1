# intiial variable
pro1,pro2,pro3 = "Apple","Bananan","cherry chili"
pr1,pr2,pr3 = 45.234,6.75,750.2558
# output 
# print(f"Product    Price ")
print(f"{'Product':<12}{'Price':>7}")
print("-"*20)
print(f"{pro1:<12} {pr1:>7.2f}")
print(f"{pro2:<12} {pr2:>6.2f}")
print(f"{pro3:<12} {pr3:>10.4f}")
