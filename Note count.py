amount=int(input("Enter the amount :"))
note2000=note500=note200=note100=note50=note20=note10=note5=note2=note1=0
if amount>=2000:
    print(amount/2000,note2000)
if amount>=500:
    print(amount/500,note500)
if amount>=200:
    print(amount/200,note200)
if amount>=100:
    print(amount/100,note100)
if amount>=50:
    print(amount/50,note50)
if amount>=20:
    print(amount/20,note20)
if amount>=10:
    print(amount/10,note10)
if amount>=5:
    print(amount/5,note5)
if amount>=2:
    print(amount/2,note2)
if amount>=1:
    print(amount/1,note1)
else:
    print("invalid amount")