# year=int(inut("Enter the year :"))
# if year%4==0:
#     print("This year is leap year")
# else:
#     print("This year isn't leap year")


year=int(input("Enter the year :"))
if year%4==0:
    if year%400:
        if year%100:
            print("This year is leap year")
else:
    print("This year isn't leap year")
        
