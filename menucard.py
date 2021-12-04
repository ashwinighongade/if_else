print("welcome")
print("sabji, roti, chawal, soup,  noodle, salad")
option=input("plese select option :")
if option=="sabji":
    print("which one")
    print("paneer, normal ")
    var=input("select option :")
    if var=="paneer":
        print("ok")
        print("paneer butter masala, kadai paneer, paneer kolhapuri, paneer hundi, mutter paneer :")
        next=input("please select your like ")
        if next=="kadai paneer" or next=="paneer hundi" or next=="mutter paneer":
            print("ok")
            qut=int(input("please select quantity"))
            if qut==1 or qut==2 or qut==3:
               print("ok")
               print("your order will be ready within 20 mintes")
               print("Thank you")
               print("visit agine")
            else:
                print("ok")
        else: 
            print("ok sir")
    else:
        print("not avaible")
else:
    print("not avaible")           
            
    
        
                                  

