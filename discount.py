Amt=int(input("enter the amount : "))
if Amt>=1000 and Amt<=5000:
    Dis=Amt*5/100
    print("Total bill pay Rs.",Amt-Dis)
elif Amt>5000 and Amt<=7000:
     Dis=Amt*10/100
     print("Total bill pay Rs.",Amt-Dis)
elif Amt>7000 and Amt<=10000:
     Dis=Amt*15/100
     print("Total bill pay Rs.",Amt-Dis)
elif Amt>10000 and Amt<=40000:
     Dis=Amt*18/100
     print("Total bill pay Rs.",Amt-Dis)
elif Amt>40000 and Amt<=60000:
     Dis=Amt*20/100
     print("Total bill pay Rs.",Amt-Dis)
elif Amt>60000 and Amt<100000:
     Dis=Amt*24/100
     print("Total bill pay Rs.",Amt-Dis)
elif Amt>100000:
     Dis=Amt*28/100
     print("Total bill pay Rs.",Amt-Dis)
else:
    print("Total bill pay Rs.",Amt)


















