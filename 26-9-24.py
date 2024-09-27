'''Create a class Person that has instance variables name, age, and gender. Add methods to:
Initialize these variables.
Update the age.
Display the person's information.
 Exercise:
 > Create multiple instances of the Person class.
 > Change the age of one person and display the updated information.'''

class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
f=person("sai","21","male")
f.display()    
        
'''Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
  Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  Exercise:
   >Create multiple employee instances.
   >Print the total number of employees after adding each new employee.
   >Check whether changing the total_employees in one instance affects the others.'''

class company:
    nmb_emp=0
    def __init__(self):
        pass
    def add_employee(self,name,dept):
        self.name=name
        self.dept=dept
        company.nmb_emp+=1
    def display(self):
        print(company.nmb_emp)
e1=company()
e1.add_employee("sai","java")
e1.display()
e2=company()
e1.add_employee("raju","python")
e2.display()


'''Create a class Rectangle that has instance variables length and width. 
  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
  Exercise:
    >Create instances of the Rectangle class with different lengths and widths.
    >Calculate and print the area for each rectangle.'''

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        calculate=self.length*self.width
        print(calculate)
radius=rectangle(15,3)
radius.area()
r1=rectangle(10,3)
r1.area()


