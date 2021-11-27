units=int(input("Enter the number of unit"))
if units>100 and units<=200:
    Pay_amount=units*5
    print("Total bill pay of Rs.",Pay_amount)
elif units>200 and units<350:
    Pay_amount=units*10
    print("Total bill pay of Rs.",Pay_amount)
elif units>350:
    print("bill paid of fixed Rs.2000/-")
else:
    print("No Charge")