a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
if a>b and a<c or a>c and a<b:
    print("a is second largest number")
elif b>c and b<a or b>a and b<c:
    print("b is second largest number")
else:
    print("c is second largest number")