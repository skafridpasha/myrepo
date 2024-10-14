'''Create a class Vehicle with attributes brand and year. The class should have a method get_info() that returns the brand and year of the vehicle. Then, create two subclasses:

Car, which adds an attribute number_of_doors.
Motorcycle, which adds an attribute has_sidecar.
Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.'''


class vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def get_info(self):
        return self.brand,self.year
class car(vehicle):
    def __init__(self,brand,year,no_of_doors):
        vehicle.__init__(self,brand,year)
        self.no_of_doors=no_of_doors
    def get_info(self):
        return f"brand:{self.brand}, year:{self.year},doors:{self.no_of_doors}"
class motorcycle(vehicle):
    def __init__(self,brand,year,has_sidecar):
        vehicle.__init__(self,brand,year)
        self.has_sidecar=has_sidecar
    def get_info(self):
        return f"brand: {self.brand}, year:{self.year}, sidecar:{self.has_sidecar}"
               
c=car("tata sumo",2024,4)
print(c.get_info())
m=motorcycle("tvs xl",2030,"yes")
print(m.get_info())


'''2.Define an abstract class Animal with an abstract method make_sound(). Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(Animal):
    def make_sound(self):
        return " dog can sound woof"
class cat(Animal):
    def make_sound(self):
        return " cat can sound meow"
class cow(Animal):
    def make_sound(self):
        return " cow can sound moo"
def play_sound(animal):
    if isinstance(animal,Animal):
        return animal.make_sound()
dog=dog()
cat=cat()
cow=cow()
print(play_sound(dog))
print(play_sound(cat))
print(play_sound(cow))

'''Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). Then, create two subclasses:

SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).'''

class BankAccount:
    def __init__(self,damount,wamount,balance):
        self.balance=balance
        self.damount=damount
        self.wamount=wamount
 
    def deposit(self):
        pass
    def withdraw(self):
        pass
    def __get_balance(self):
        pass
class savingAccount(BankAccount):
    def deposit(self):
        self.balance=self.balance+self.damount
        return self.balance
    def withdraw(self):
        if(self.wamount>0):
            if(self.balance>500):
               self.balance=self.balance-self.wamount
               return self.balance
            else:
               return " connot withdraw the amount is insufficient"
        else:
            return " the amount must be positive"
    def __get_balance(self):
            return self.balance
class currentAccount(BankAccount):
    def deposit(self):
        self.balance=(self.balance)+(self.damount)
        return self.balance
    def withdraw(self):
        if(self.wamount>0):
            if(self.balance-self.wamount>=-1000):
               self.balance=self.balance-self.wamount
               return self.balance
            else:
               return "cannot withdrawal, the amount is overdraft"
        else:
            return " the amount must be positive"
           
    def __get_balance(self):
            return self.balance
s=savingAccount(1000,200,500)
print(s.deposit())
print(s.withdraw())
c=currentAccount(6000,4000,3000)
print(c.withdraw())

'''Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.

Add a method increase_salary(percent) in the Employee class that increases the salary by a given percentage.'''
class Employee:
    def  __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_details(self):
        return self.name+" "+str(self.salary)
    def get_salary(self):
        return self.salary
    def increase_salary(self,percentage):
        self.percentage=percentage
        self.salary+=self.salary*(self.percentage)/100
       
 
class manager(Employee):
    def __init__(self,name,salary,depart):
        super().__init__(name,salary)
        self.depart=depart
    def get_details(self):
        return (super().get_details()+"  "+self.depart)
   
   
class developer(Employee):
    def __init__(self,name,salary,planguage):
        super().__init__(name,salary)
        self.planguage=planguage
    def get_details(self):
        return (super().get_details()+"  "+self.planguage)
 
m=manager("gopi",50000,"java")
print(m.get_details())
 
d=developer("raju",23000,"python")
print(d.get_details())
m.increase_salary(3)
d.increase_salary(2)
print("----------after increment--------")
print(m.get_details())
print(d.get_details())


'''Create an abstract class Media with an abstract method play(). Then create the following subclasses:

Audio, which plays a .mp3 file.
Video, which plays a .mp4 file.
LiveStream, which plays a live stream.
Implement a function start_media(media) that takes an object of type Media and calls its play() method. Demonstrate polymorphism by passing different types of media to this function.'''
class Media:
    @abstractmethod
    def play(self):
        pass
class audio(Media):
    def play(self):
        return " play .mp3 file"
class video(Media):
    def play(self):
        return "play .mp4 file"  
class liveStream(Media):
    def play(self):
        return "play a live stream"
def start_media(media):
    if isinstance(media,Media):
        return media.play()
a=audio()
v=video()
l=liveStream()
print(start_media(a))
print(start_media(v))
print(start_media(l))
