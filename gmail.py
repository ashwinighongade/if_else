nam=input("Enter the first name :")
if nam>="a" or nam<="z" or nam>="A" or nam>="Z":
    var=input("Enter the last name :")
    if var>="a" or var<="z" or var>="A" or var<="Z":
        sex=input("Enter the gender- male/female :")
        uname=input("Enter the username - character and number :")
        if uname>"a" and uname<="z" and uname>="0" or uname<="9":
            print(uname,"@gmail.com")
            ch=input("Enter the password -character :")
            if ch>="a" or ch<="A" or ch<="Z" or ch<="z":
                sp=input("Enter the special character :")
                if sp=="@" or sp=="#" or sp=="$" or sp=="&" or sp=="&" or sp=="*":
                    no=int(input("Enter the number :"))
                    if no>=0 or no<=9:
                        strop=ch+sp+str(no)
                        print(strop)
                        con=input("Enter the confirm password :")
                        if con==strop:
                            print("you make strong password")
                            mo=int(input("Enter the mobile number"))
                            if mo>=0 or mo<=9:
                                otp=int(input("Enter the opt"))
                                if otp>=0 or otp<=9:
                                    print("verify the otp")
                                    print ("you done process sucessfuly")
                                else:
                                    print("wrong otp")
                            else:
                                print("wrong mobile number")
                        else:
                            print("password not same")
                    else:
                        print("something misket")
                else:
                    print("please enter correct sp")
            else:
                print("please enter correct character")
        else:
            print("please enter correct")
    else:
        print("correct last name")
else:
    print("invalid name")                                                        
 
