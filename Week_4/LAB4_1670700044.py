title1 = '''
==========================================
|           *** Order Total ***          |
------------------------------------------
'''
title2 = """
-------------------------------------------
| Destination:                              |                 
|   (BK) The Bangkok Metropolitan Region    |
|   (TH) For areas in other provinces       |
-------------------------------------------
"""
title3 = """
------------------------------------------
|   Weight  |      BK       |     TH     |
------------------------------------------
|    1-5    |       80      |     140    |
|    6-10   |      150      |     200    |
|    10+    |      200      |     250    |
------------------------------------------
"""
order = int(input("Enter order Summary : "))
print(title3)
des = input("Enter destination : ").upper()
if des == "BK" or des == "TH" :
    weight = float(input("Enter total weight(KG.) : "))
    if des == "BK" :
        if weight <= 5 :
            shipping = 80 
        elif weight <= 10 :
            shipping = 150
        else :
            shipping = 200
    else : #TH Zone
        if weight <= 5 :
            shipping = 140 
        elif weight <= 10 :
            shipping = 200
        else: 
            shipping = 250
    #Calculate discount 
    discount = 0 
    if order > 5000 :
        discount = -120
    elif order >= 3000 :
        discount = -60
    #display total order 
    print(title1)
    print(f"{"Order summary ":<17} : {order:>10.2f}")
    print(f"{"Shipping":<17} : {shipping:>10.2f}")
    print(f"{"Discount":<17} : {discount:>10.2f}")
    print("="*42)
    total = order+shipping+discount
    print(f"{"Order total":<17} : {total:>10.2f}")
    print("="*42)
else :
    print("Invalid destination code ! Please try again. ")
