month=input("Enter the month :")
if month=="jan" or month=="mar" or month=="may" or month=="july" or month=="aug" or month=="oct" or month=="dec":
    print("This month days are 31")
elif month=="april" or month=="june" or month=="sep" or month=="nov":
    print("This month days are 30")
else:
    print("This month days are 28 or 29")