Salary=int(input("Enter the salary : "))
yrs=int(input("Enter the Sevice of the Year :"))
if yrs>=5:
    Net_salary=Salary+(Salary*5/100)
    print("Your Net Salary Rs.",Net_salary)
elif yrs>10:
      Net_salary=Salary+(Salary*10/100)
      print("Your Net Salary Rs.",Net_salary)
else:
    print("Your Net Salary Rs.",Salary)