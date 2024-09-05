#1)Write a python program to  add a key to a dictionary ?

d={0:10,1:20,2:30}
print(d)
d.update({3:40})
print(d)

#2)Write a python program to check weather the given value is present in the dictionary or not ?

d1={'key1':'value1','key2':'value2'}
if 'key1' in d1:
 print('it is present')
else:
    print('it is absent') 

#3)Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

d=dict()
for x in range (1,16):
   d[x]=x**2
print(d)


#4)Write a python program to create a dictionary from the string ?
str="{'A':10,'B':20,'c':30,'d':40}"
print(type(str))
#eval
d2=eval(str)
print(d2)
print(d2['A'])
print(d2['B'])


#5)Write a python program to combine two dictionaries by adding values of common keys ?
s1={'hyd':10,'srpt':20,'mlg':30,}
s2={'hnr':40,'srpt':30,'nlg':50}
s3=0

for key in s1:
   if key in s2:
      s2[key]=s1[key]+s2[key] 
print(s2)      
      
#6)Write a python program to merge two python dictionaries ?

A1={'A':100,'B':200,'C':300}
B2={'D':400,'E':500}
print(A1|B2)

#7)Write  a python program to sort dictionary by keys or values ?

v1={'c':40,'b':30,'a':20,'d':10}
sort=dict(sorted(v1.items()))
print(sort)

#8)Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.

st=input("Enter a string:")
dic={}
for ch in st:
   if ch in dic:
      dic[ch]+=1
   else:
      dic[ch]=1
print(dic)
         