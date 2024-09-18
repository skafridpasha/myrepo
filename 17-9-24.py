#1)Create a dictionary where the keys are tuples representing coordinates (x, y) and the values are city names.
#  Write a Python program to print the city name for a given coordinate. 
# Example Dictionary: #{(40.7128, -74.0060): "New York", 
# (34.0522, -118.2437): "Los Angeles"} # Input: (40.7128, -74.0060) # Expected Output: "New York"


def city(coord):
 city_coordinates={(40.7128,-74.0060):"new york",(34.0522,-118.2437):"Los angels"}
 return city_coordinates.get(coord,"city is not found")
input_coordinate=(34.0522,-118.2437)
print(city(input_coordinate))


#2)Write a Python program to find the minimum and maximum elements in a tuple of integers. 
# python # Example Tuple: (10, 20, 5, 40, 25) 
# # Expected Output: Min: 5, Max: 40
t=(10,20,5,40,25)
print(type(t))
print( "lowest:",min(t))
print("highest:",max(t))

#3)Write a Python program to sort a tuple of tuples based on the second element of each tuple. 
# python # Example Tuple: ((1, 2), (3, 1), (5, 0)) # 
# Expected Output: ((5, 0), (3, 1), (1, 2))

'''t=eval(input("Enter tuple:"))
l1=sorted(t,key=lambda x:x[1])    
print(l1)
print(tuple(l1))


#4)Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple.
#Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)'''

'''t=eval(input("Enter tuple:"))
l=[]
for i in t:
    if isinstance(i,tuple):
        l.extend(i)
    else:
        l.append(i)
print(tuple(l))  '''