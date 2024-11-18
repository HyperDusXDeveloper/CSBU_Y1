with open("deposit.txt" , "w" ) as file1 :
    with open("withdraw.txt" , "w") as file2 :
        amt = int(input("Enter Transaction amount : "))
        for i in range(amt):
            detail = input("Detail : ")
            kind = input("Type(D/M : )").upper()
            total = int(input("Amount : "))
            if kind == "D" :
                file1.write(f"{detail:<20}{kind:<3}{total:<10.2f}\n")
            elif kind == "M" :
                file2.write(f"{detail:<20}{kind:<3}{total:<10.2f}\n")