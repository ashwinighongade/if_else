print("sing up")
print("its free and anyone can join")
Fnam=input("Enter the  first name :")
if Fnam>="a" or Fnam<="z" or Fnam>="A" or Fnam<="Z":
    Lnam=input("Enter last lnam :")
    if Lnam>="a" and Lnam<="z" or Lnam>="A" and Lnam<="Z":
        mail=input("Enter your mail id :")
        if mail=="ghongadeash_1":
            newpass=input("Enter the character :")
            if newpass>="a" and newpass<="z" or newpass>="A" and newpass<="Z":
                newpass=input("enter the special character :")
                if newpass=="@" or newpass=="#" or newpass=="&":
                    newpass=int(input("enter the number :"))
                    if newpass>=0 or newpass<=9:
                        print("yourstrong password",newpass)
                        year=int(input("Enter the birth of year :"))
                        if year>=0 or year<=9:
                            month=int(input("Enter the month :"))
                            if month>=1 or month<=12:
                                date=int(input("enter the date :"))
                                if date>=1 or date<=31:
                                    sex=input("Enter the sex :")
                                    if sex=="male" or sex=="female":
                                        print("sing up")
                                        cap=("enter the capture")
                                        print("Yor are sing up facebook account sucessefuly")
                                    else:
                                        print("wrong option")
                                else:
                                    print("please enter correct date")
                            else: 
                                print("please enter correct month")
                        else:
                            print("please enter the correct year")
                    else:
                        print("please enter number")
                else:
                    print("please enter correct special character")
            else:
                print("please enter correct character")
        else:
            print("involid mail id")
    else:
        print("wrong")
else:
    print("please enter valid name")                                                


                        

                    
                    
                 