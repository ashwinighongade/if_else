X=int(input("enter the lenth :"))
Y=int(input("enter the lenth :"))
Z=int(input("enter the lenth :"))
if X==Y==Z:
    print("its equilateral")
elif X==Y or Y==Z or Z==X:
    print("its isosceles")
else:
    print("its scalene")
