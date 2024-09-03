'''1)Write a program that accepts a sentence and calculate the number of upper case letters 
and lower case letters. Suppose the following input is supplied to the program: Hello 
world! Then, the output should be: UPPER CASE 1 LOWER CASE 9'''


s=input("Enter your message:")

u=0
l=0
for i in s:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1 
print('upper case letter:{}'.format(u))      
  
print('lower case letter:{}'.format(l))


'''2)Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output 
should be: LETTERS 10 DIGITS 3'''


string=input("Enter your sentence:")
def countletteranddigit(string):
  l=0
  d=0
  c=0
  for i in string:
     if i.isdigit():
        d+=1
     elif i.isalpha(): 
        l+=1
  return l,d,
letters,digits=countletteranddigit(string)
print( "Total letter:",letters)
print("Total digits:",digits)


'''''3)Write a program that accepts a comma separated sequence of words as input and prints 
the words ina comma-separated sequence after sorting them alphabetically. Suppose the 
following input is supplied to the program: without, hello, bag, world Then, the output 
should be: bag,hello,without,world'''

s=input("Enter your words:")
v1 =s.split(",")
print(v1)
v1.sort()
print((",").join(v1))

'''4)Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number. Suppose the following input 
is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', 
'33', '12', '98'] ('34', '67', '55', '33', '12', '98')'''

num= input("enter number:")
num1=num.split(",")
print(num1)
num2=tuple(num1)
print(num2)

'''5)With a given integral number n, write a program to generate a dictionary that contains (i, 
i*i) such that is an integral number between 1 and n (both included). and then the program 
should print the dictionary. Suppose the following input is supplied to the program: 8 Then, 
the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64'''


num=int(input("enter a number:"))
num2={}
for i in range(0,num+1):
    num2[i]=i*i
print(num2)

''''6)Write a program which will find all such numbers which are divisible by 7 but are not a 
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be 
printed in a comma-separated sequence on a single line.'''

for i in range(2000,4000):
    if i%7==0 and i%5!=0:
        print(i,end=",")