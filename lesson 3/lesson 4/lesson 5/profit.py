actual_cost=float(input("enter actual price:"))
saleamount=float(input("enter selling amount:"))

if saleamount>actual_cost:
    profit=saleamount-actual_cost
    print("the profit is",profit)
else:
    print("no profit")
