age=int(input("Enter the age :"))
days=int(input("Enter the working day :"))
gender=input("enter the gender :")
if age>=18 and age<=30:
    if gender=="male":
        male=700
        wages=days*male
        print("your wages is Rs.", wages)
    elif gender=="famale":
        female=750
        wages=days*female
        print("your wages is Rs.",wages)
elif age>=30 and age<=40:
    if gender=="male":
        male=800
        wages=days*male
        print("your wages is Rs.",wages)
    elif gender=="female":
        female=850
        wages=days*850
        print("your wages is Rs.",wages)
else:
    print("not avaiable")



