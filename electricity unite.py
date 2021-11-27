unit=int(input("enter the eletricity unit :"))
if unit>0 and unit<=50:
    Pay_Amonut=unit*0.50
    Surcharge=unit*20/100
    print("Eletricity bill pay Rs.",Pay_Amonut+Surcharge)
elif unit>50 and unit<=100:
     Pay_Amonut=unit*0.75
     Surcharge=unit*20/100
     print("Electricity bill pay Rs.",Pay_Amonut+Surcharge)
elif unit>100 and unit<=250:
    Pay_Amonut=unit*1.20
    Surcharge=unit*20/100
    print("Eletricity bill pay Rs.",Pay_Amonut+Surcharge)
elif unit>250:
    Pay_Amonut=unit*1.50
    Surcharge=unit*20/100
    print("Eletricity bill pay Rs.",Pay_Amonut+Surcharge)
else:
    Pay_Amonut=0
    print("Electricity bill pay Rs.",Pay_Amount)


