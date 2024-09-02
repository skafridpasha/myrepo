#1)Write a python program to find most frequent element in tuple ?

t1=input("Enter a elements:" )
l=list(t1)
s=max(set(l),key=l.count)
print("Frequent Element is:",s)


#2)Write a python proram to convert tuple into a string ?


s=("a","p","p","l","e")
str="".join(s)
print(str)

#3)write a python program to add an item to the tuple ? 

t=("apple","banana","carrot")
print(type(t))
l=list(t)
print(l)
print(type(l))

l.append("mango")
print(l)
print(tuple(l))

#4)How do you create a empty tuple on python ?

t=("afrid","sohail","chotu")
l=list(t)
l.clear()
t2=tuple(l)
print(t2)


#5)Write a python program to unpack atuple into several variables ?

t=("skywaves", 20145221,50000,"hyderbad")
(company,employeeid,salary,location)=t
print( "company:",company)
print("emp id:",employeeid)
print("amount:",salary)
print("work:",location)



