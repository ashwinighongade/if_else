from typing import AsyncGenerator


birthyear=int(input("enter the birth year :"))
currentyear=int(input("enter the current year :"))

if currentyear-birthyear:
    age=currentyear-birthyear
    print("your age is",age)
    bmonth=int(input("enther the birth month :"))
    cmonth=int(input("enter the current month :"))
    if bmonth>=1 and cmonth<=12 and cmonth>=1 and cmonth<=12:
        month=cmonth-bmonth
        print("your age is",month)
        bdate=int(input("enter the birth date :"))
        cdate=int(input("enter the current date:"))
        if bdate>=1 or bdate<=31 and cdate>=1 and cdate<=31:
            date=cdate-bdate
            print("your age is",date)
            print(age,"year",month,"month",date,"days")
        else:
            print("wrong date")
    else:
        print("wrong")
else:
    print("wrong")   
    

    
    
   