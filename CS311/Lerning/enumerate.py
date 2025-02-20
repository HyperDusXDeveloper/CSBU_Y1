stocklist = ["NVDA" , "TSM" , "AVGO" , "ARM" , "AAPL"]
price = [120 , 40 ,100 , 300 , 200]
print(f"{stocklist} With Enumerate(list)")
for i,data in enumerate(stocklist):
    print(i+1,data+" Price ")

print(f"\n{stocklist} With range(len(list))")
for i in range(len(stocklist)):
    print(i+1,stocklist[i]+" Price ")