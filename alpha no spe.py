Var=input("Enter the character :")
if Var>="a" and Var<="z" or Var>="A" and Var<="Z":
    print("This is an Alphabet")
elif Var=="@"or Var=="#" or Var=="$" or Var=="%" or Var=="&":
    print("This is a Special Character")
else:
    print("This is a Number")
