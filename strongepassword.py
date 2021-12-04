word=input("Enter the character")
if word>="a" or word<="z" or word>="A" or word<="z":
    print("your password", word)
    number=int(input("Enter the number"))
    if number>=0 or number<=9:
         print("your password",number)
         sp=input("Enter the special character")
         if sp=="@" or sp=="#" or sp=="$" or sp=="&" or sp=="%":
             print("your password",sp)
             sum=word+str(number)+sp
             if sum==sum:
                 print(sum)
                 print("you sucessfuly create strong password")
             else:
                 print("not strong password")
         else:
             print("plese take sp characte")
    else:
        print("plese enter correct number")
else:
    print("plese enter the character")        


            