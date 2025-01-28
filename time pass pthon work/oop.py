class Car : # hear it just work like a genralised form which can work with different paremeters with a new varibal
    
    total_car = 0
    def __init__ (self,brand,model): # hear self is used as a telephon line which establish a connection between the class and function 
        self.__brand = brand # defining the atributs of class
        self.__model = model # defining the atributs of class
        # hear __init__ is an costector 
        Car.total_car +=1
        
    def get_brand(self):
        return f"{self.__brand}"
        
    def full_name (self) : # one of the methods 
        return f"Hi i am Driving {self.__brand} {self.__model}"
   
    def full_type (self):
        return "petrol or diesel"
    
    # @ staticmethod are the decoraters in python
    @staticmethod # due to this we only access this varibal with car.gen_def (we does nat able to access function with object)
    def gen_def(): # hear we does not used self or connect the class with class or objects
        return "cars are good means of transport" 
    
    @property # it is used to hide the access of every one or give it to object as read only font
    def model(self):
        return self.__model
    

class Eletriccar(Car) :
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) # hear we just gating the parimaters values (atributes) from the upper class so we does not have defined it again
        self.battery_size = battery_size
        # so in this we inharit the things from car class so we have the access to its atributes too
        
    def full_type (self):
        return "Electric charg"

        

# instance no 1   
my_car = Car("Toyota","Corolla")
# print(my_car.__brand)# we pravitised the __ brand
print(my_car.get_brand())
print(my_car.model)
print(my_car.full_name()) # hear the brackets is given because we are calling the function
print(my_car.full_type())

# instance no 2
my_tesla = Eletriccar("Tasla","S class","85kwh")
# print(my_tesla.__brand)# __brand the direct access to the varibal is stoped if you want to access the varibal so you have to use some methods
print(my_tesla.get_brand())
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.full_type())

print(isinstance(my_tesla,Eletriccar))
print(isinstance(my_tesla,Car))
print(isinstance(my_car,Car))
print(isinstance(my_car,Eletriccar))


print(Car.total_car) # if we used another varibal for this so it will also calculate that varibal as a car so because of that we just simply print it in ths way

class Battery:
    def battery_info(self):
        return "this is battery"
    
class Engine:
    def Engine_info(self):
        return "this is Engine"
    
class ElectriccarTow(Battery,Engine,Car):
    pass
    
my_new_ev = ElectriccarTow("tesla","c class")
print(my_new_ev.battery_info())
print(my_new_ev.Engine_info())# so hear we proved that there is multiple in haritance can be posible in python

# Decorater are use to implement some rules or chang the functionality (enhansment functionality)
# static method :- it just creat a boundation on varibal or function so that it can be access by the class but not by instance
# encapulation means cover the code(pack the code) so if the coder want to tell about the details so then the user is capable to retrived the information
# inharitance means when you get thiongs from your prent class to child class
# polimorphism means method with same name but workin is different in different switch vation

