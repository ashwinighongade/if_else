Basic_salary=int(input("enter the basic salary:"))
if Basic_salary<=10000:
   Gross_salary=Basic_salary+(Basic_salary*20/100)+(Basic_salary*80/100) 
   print("Gross salary is",Gross_salary)
elif Basic_salary>10000 and Basic_salary<=20000:
     Gross_salary=Basic_salary+(Basic_salary*25/100)+(Basic_salary*90/100)
     print("Gross_salary is",Gross_salary)
elif Basic_salary>20000:
     Gross_salary=Basic_salary+(Basic_salary*30/100)+(Basic_salary*95/100)
     print("Gross_salary is",Gross_salary)
else:
    print("Error")




