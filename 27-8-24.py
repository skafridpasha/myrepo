#string >>> it is single or group of characters between the single'' or double ""


var1="python is very easy to learn "
print(len(var1))

l=len(var1)
for i in range(l):
    if var1[i]=="n":
        print (var1[i])
else: 
 print ("that element is not present")

 #slicing >> it is nothing but a extracting the part of the list.
  
#x=(start:end:step)

x=[1,10,20,'rama','sita','true',]
print(x)
print(x[4])

print(x[:3])

print(x[3:])

print(x[1::2])
print(x[1:4])
print(x[1:5])
print(x[1::3])

#reverse order
x=[1,10,20,'rama','sita','true',]

p=x[-1]
print(p)
p=x[-1::-2]
print(p)
p=x[-3::-2]
print(p)
p=x[-5::-1]
print(p)

#mathematical operator in strings: they are 2types

  # 1)concatenate operator(+): it is used to join two or more strings.
var1= "python is easy to learn"+" it is a open source"
print(var1)
s= "easy to understand"
s1=" it is high level"
print(s+s1)

  #2)repetition operator(*):it is used to repeate the string for num. of 'n' times.

A1=" python "*3
print(A1)
s="python"
print((s+" ")*10)

#find > it is nothing but to find the word in our string
word=" learning of python"
print(word.find('y'))






 

