physics=int(input("enter the phy marks"))
chemistry=int(input("enter the Che marks"))
biolygy=int(input("enter the bio marks"))
mathematic=int(input("enter the math marks"))
computer=int(input("enter the com marks"))
Pre=physics+chemistry+biolygy+mathematic+computer*100/500
if Pre>=90:
    print("Grade A")
elif Pre>=80 and Pre<=90:
    print("Grade B")
elif Pre>=70 and Pre<=80:
    print("Grade c")
elif Pre>=60 and Pre<=70:
    print("Grade D")
elif Pre>=50 and Pre<=60:
    print("Grade E")
elif Pre>=40 and Pre<=50:
    print("Grade F")
else:
    print("pass")

