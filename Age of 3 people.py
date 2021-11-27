A=int(input("Enter the age of A :"))
B=int(input("Enter the age of B :"))
C=int(input("Enter the age of C :"))
if A>B and A>C:
    print("A is Older than B and C")
elif B>A and A>C:
    print("B is Older than A and C")
elif C>A and C>B:
    print("C is Older than A and C")
elif A<B and A<C:
    print("A is Yonger than B and C")
elif B<A and A<C:
    print("C is Youngr than B and A")
else:
    print(" B is Younger than A and C")