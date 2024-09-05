#least common factor(LCM)
'''num1= int(input("Enter a nmb:"))
num2= int(input("Enter a nmb:"))
if num1<num2:
    least=num1
else:
    least=num2
div=2
while div<=least:
    if num1%div==0 and num2%div==0:
        print("lcm",div)
        break
    div=div+1
else:
    ('There is no lcm')'''


#GCD
nmb1=int(input("Enter a nmb:"))
nmb2=int(input("Enter a nmb:"))

if nmb1>nmb2:
    least= nmb1
else:
    leasst=nmb2

div= least
while div>=least:
    if nmb1%div==0 and nmb2==0:
        print('GCD',div)
        break
    div=div-1
else:
    print('there is no gcd')


