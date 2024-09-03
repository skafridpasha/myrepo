# 1)Python Program to count occurrence of a given characters in string.

variable1= input("Enter your string:")
for i in variable1:
    print(i,"=",variable1.count(i),'times')


#2)Python program to replace the string space with a given character.

var= input("enter a string:")
result=" "
char= input("enter the character:")
for i in var:
   if i==" ":
      i=char
result+=i
print("replace string:",result)

#3)Python program to replace the string space with a given character using replace() method.

name="my name is afrid"
print(name)
print(name.replace("afrid","sohail"))

#4)Python program to convert lowercase char to uppercase of string.
name="python is easy to learn"
print(name.upper())


#5)Python program to convert lowercase vowel to uppercase in string.

s=input("enter a string:")
res=""
for i in s:
    if i.islower():
        i = i.upper()
    res+=i
print("after converting:",res)


#6)Python program to remove blank space from string.

word=" learning python is easy "
print(len(word))
s=(word.strip())
print(len(s))


#7)Python program to concatenate two strings using join() method.

list=["rama","sita","ravi","gopi"]
print(len(list))
s="+".join(list)
print(s)
print(len(s))


#8)Python program to concatenate two strings without using join() method.

s1="it is easy to write"
s2="as compare to other"
print(s1+" "+s2)

#9)Python program to check given character is vowel or consonant.


s= "i am learnig python"
vowels="a e i o u"
for i in s:
    if i in vowels:
        print(i, end=" ")


#10)Python program to check given character is digit or not.


num="123456678"
num1=num.isdigit()
print(num1)



#11)Python program to delete vowels in a given string.

s="i am learning a python"
vowels="a e i o u"
for i in s:
    if i not in vowels:
        print(i)

 #12)Python program to check a String is palindrome or not.


value=input("enter a value:")
print(value)
if value == value[-1::-1]:
  print("pallindrome")
else:
   print("not a pallindrome")


#13)Python program to remove repeated character from string.

str=["rama","sita","krishna","gopi","rama","sita"]
new_str=[]
for i in str:
   if i not in new_str:
      new_str.append(i)
print(str)
print(new_str)


string="afridpasha"
new =""
for i in string:
   if i not in new:
     new=new+i
print(new)


#14)Python program to calculate sum of integers in string.

a="abcd123"
count=0
for i in a:
   if i.isdigit():
      count=count+int(i)
print(count)

#15)Python program to copy one string to another string.

string=input("enter a string:")
print( "original string:",string)
new_str=string
print( "copy string:",new_str)


#16)Python program to print all non repeating character in string.

from collections import Counter
str= "python"
char_count=Counter(str)
print(char_count)
for char in str:
   if char_count[char]==1:
       print(char)
       break
   
#17)Python program to count alphabets, digits and special characters.


string=input("enter a string:")
digit=0
alpa=0
spe_char=0
for i in string:
   if i.isdigit():
      digit+=1
   elif i.isalpha():
      alpa+=1
   else:
       spe_char+=1
print( "total nmb:",digit )
print("total letters:",alpa) 
print("total spe:",spe_char)

#18)Python program to count the Occurrence Of Vowels & Consonants in a String.


variable=input("enter any string:")
vowels="a e i o u"
count_consonant=0
count_vowels=0
for i in variable:
   if i in vowels:
      count_vowels+=1
   else: 
      count_consonant+=1
print( "our consonant:",count_consonant)
print("our vowels:",count_vowels)


#19)Python Program to check if two Strings are Anagram.

var1=input("enter a string1:")
var2=input("enter a string2:")
if len(var1)!=len(var2):
   print("not anagram")
else:
    if (var1)==(var2):
     print("it is a anagrams")
    else:
     print("it is not a anagram")


#20)Python program to check given character is digit or not using isdigit() method.

num= (input("enter any character:"))
num1=num.isdigit()
print(num1)


#21)Python program to separate characters in a given string.


word=input("enter a string:")
s=word.split()
print(s)




   