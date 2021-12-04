print("Welcome to SBI ATM")
print("insert the card")
card=input("please enter type of card - Debit card or Credit card :")
if card=="Debit":
    print("processing")
    print("plese selected language")
    lan=input("Enter the language : ")
    if lan=="Hindi" or lan=="english":
        pin=int(input("plese enter the pin :"))
        if pin==3456:
            type=input("please enter your account type - saving and current :")
            if type=="saving" or type=="current":
                # print("processing")
                option=input("please enter the tranction - banking or pin generate or balance enquiry :")
                if option=="banking":
                    # print("processing")
                    var=input("plese enter the option - withdrawal or deposite or mini statement :")
                    if var=="withdrawal":
                        # print("processing")
                        print("balance==20000")
                        amt=int(input("please enter the amt :"))
                        if amt<=20000:
                            print("your transaction is being process please wait")
                            print("please collect your cash")
                            print("do you want slip")
                            a=input(" enter do you want slip :")
                            if a=="yes" or a=="no":
                                print("processing")
                                print("thanking you")
                            else:
                                print("thank you")
                        else:
                            print("your balance is Rs.20000")  
                    else:
                        print("wrong option")          
                else:
                    print("please select correct option")
            else:
                print("try againe")
        else:
            print("incorrect pin")
    else:
        print('please select correct option')
else:
    print("incorrect option")                







    


