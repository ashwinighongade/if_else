from typing import MutableMapping


age=input("Enter the age :")
days=int(input("Enter the working days :"))
sex=input("Enter the sex- male or female :")
if age>="18" and age<="30":
    
    if sex=="male":
        print(days*700)

    else:
        print(days*750)


    
