a=int(input("enter the selling amount"))
b=int(input("enter the purchasing amount"))
if a-b>0:
    print("profit")
elif a-b<0:
    print("Loss")
else:
    print("no profit, no loss")
