#factorial

'''s=5*4*3*2
print(s)

num=int(input("Enter a nmb:"))
fact=1
while num>=1:#5>=1
    fact=fact*num#1=1*5
    num=num-1#4
print(fact)'''


'''#for loop
for char in "afrid":
  if char=="d":
    break
  print(char,end=" ")'''


#find vowels
'''s="im learning python"
v="aeiou"
for i in s:
    if i not in v:
        print(i,end=" ")'''

#remove duplicate values from given string

'''def dup(s):
    l=[]
    for char in s:
        if char not in l:
            l.append(char)
    print(l)
    st=",".join(l)
    return st
s="aaaaabbbbbccccccc"
print(dup(s))'''

#even nmbs
num=int(input("enter a value:"))
#while num>0:
if num>0 and num%2==0:
   print("even")
  
else:
    print("not")
     



