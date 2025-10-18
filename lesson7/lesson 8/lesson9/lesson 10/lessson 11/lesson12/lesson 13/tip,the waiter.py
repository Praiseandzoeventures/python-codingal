def total(bill_amount,tip_perc):
    total=bill_amount*(1+0.0*tip_perc)
    total=round(total,2)
    print("please pay",total)
    
total(150,20)