Bike_price=int(input("Enter the bike price :"))
if Bike_price<=50000:
    Road_tax=Bike_price*5/100
    print("The road tax is Rs.",Road_tax)
elif Bike_price>50000 and Bike_price<=100000:
     Road_tax=Bike_price*10/100
     print("The road tax is Rs.",Road_tax)
else:
     Road_tax=Bike_price*15/100
     print("The road tax is Rs.",Road_tax)


    
