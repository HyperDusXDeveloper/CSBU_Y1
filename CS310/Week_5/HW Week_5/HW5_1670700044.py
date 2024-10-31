title1 = '''
==========================================
|           *** Order Summary ***         |
------------------------------------------
'''
title2 = """-------------------------------------------
| Destination:                            |                 
|   (BK) The Bangkok Metropolitan Region  |
|   (TH) For areas in other provinces     |
  ---------------------------------------
|   Weight  |      BK       |     TH      |
  ---------------------------------------
|    1-5    |       80      |     140     |
|    6-10   |      150      |     200     |
|    10+    |      200      |     250     |
------------------------------------------"""
title3 = """==========================================
|      *** Total Order Summary ***       |
------------------------------------------"""

# Variable Total Order Summary
ordersum = 0
shippingsum = 0
discountsum = 0

print(title1)
# Costomer loop
Costomer = int(input("Enter total customer : "))
for info in range (Costomer) :
    order = int(input(f"Order : {info+1}  > Enter order Summary : "))
    print(title2)
    des = input(f"Order : {info+1}  > Enter destination : ").upper()
    # Destinatoin BK/TH/Other
    if des == "BK" or des == "TH" :
        weight = float(input(f"Order : {info+1}  > Enter total weight(KG) : "))
        if des == "BK" :
            # Weight #BK
            if weight <= 5 :
                shipping = 80 
            elif weight <= 10 :
                shipping = 150
            else :
                shipping = 200
        if des == "TH" :
            # Weight #TH
            if weight <= 5 :
                shipping = 140 
            elif weight <= 10 :
                shipping = 200
            else: 
                shipping = 250
                
        #Calculate Discount 
        discount = 0 
        if order > 5000 :
            discount = -120
        elif order >= 3000 :
            discount = -60
            
        #Display total order 
        print(title1)
        print(f"Order : {info+1}  > {"Order summary ":<8} : {order:>10.2f}")
        print(f"Order : {info+1}  > {"Shipping":<14} : {shipping:>10.2f}")
        print(f"Order : {info+1}  > {"Discount":<14} : {discount:>10.2f}")
        print("="*42)
        total = order+shipping+discount
        print(f"Order : {info+1}  > {"Order total":<14} : {total:>10.2f}")
        print("="*42)
        # total Order Summary
        ordersum = ordersum + order
        shippingsum = shippingsum + shipping
        discountsum = discountsum + discount
    else : #else Destinatoin
        # Display  total Order Summary
        print("Invalid destination code ! Please try again. ")
# Test total all sum
# print(f"{ordersum} {shippingsum} discountsum = {discountsum*-1}")
print(title3)
print(f"All {"Order total summary ":<10} : {ordersum:>10.2f}")
print(f"All {"Total Shipping":<20} : {shippingsum:>10.2f}")
print(f"All {"Total Discount":<20} : {discountsum*-1:>10.2f}")
print("="*42)
totalsum = ordersum+shippingsum+discountsum
print(f"All {"Order total":<20} : {totalsum:>10.2f}")
print("="*42)