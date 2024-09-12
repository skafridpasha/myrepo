#positional arg...
def sum(x,y):
    print(x-y)
sum(x=20,y=10)


def display(m,y):
    print(m+" "+y,"are besties")
display(m="radha",y="krishna")

#keyword argument()
def sum(y,x):
    print(x-y)
sum(40,30)    

#diff b/w the keyword and positional arg....
def display(msg,name):
    print("hi",name,msg)
display(name="radha",msg="gd mrng")    
#        different
def display(msg,name):
    print("hi",name,msg)
display("radha","gd mrng")

#default arg...
def greet(name,msg="java is easy"):
    print("",name,msg)
greet(name="afrid")

#variable length of arg...

def calculator(*n):
    sum=0
    print(type(n))
    for i in n:
     sum=sum+i
    print(sum)
calculator (10,20)

#keyword variable length of arg....

def function(**x):
    print(x.keys())
    print(x.values())
    print(type(x))
    for i,j in x.items():
        print(i,"=",j)
function(f1="ram",f2="sai",f3="sita")        


def emp(**n):
     print(n.keys())
     print(n.values())
     for i,k, in n.items():
        print(i,"==",k,)
emp(name="raju",id="201",salary="30000")