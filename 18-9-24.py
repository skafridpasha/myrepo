#1)import random game

import random
fix=random.randint(1,10)
i=1
while i<=3:
    guess=int(input("guess a number:"))
    if fix==guess:
        print("you won the game")
        break
    else:
        print("wrong guess")
    i=i+1
else:
    print("you lost the game")


#2)vegetable market

veg=["tomato","brinjal","cucumber","onion"]
qty=[20,15,30,40]
price=[30,20,25,40]

item=input("what you want?")

if item in veg:
    q=float(input("how much qty you want:"))
    idx=veg.index(item)

    if q<=qty[idx]:
        amount= q*price[idx]
        print("please pay",amount)

else:
    print(item,"is not there")    