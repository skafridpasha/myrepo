'''1)Write a Python program to sort a tuple of tuples based on the second element
of each tuple.
Example Tuple: ((1, 2), (3, 1), (5, 0))Expected Output: ((5, 0), (3, 1), (1, 2))'''

t=eval(input("Enter tuple:"))
l1=sorted(t,key=lambda x:x[1])    
print(l1)
print(tuple(l1))


'''2).Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple.
Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)'''

t=eval(input("Enter tuple:"))
l=[]
for i in t:
    if isinstance(i,tuple):
        l.extend(i)
    else:
        l.append(i)
print(tuple(l))           

