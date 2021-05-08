# PRIVATE CLASS VARIABLES(STATIC) CAN'T BE ACCESSED OUTSIDE OF IT'S CLASS WITHOUT
# A PUBLIC INTERFACE

# THE PUBLIC INTERFACES TO ACCESS THE CLASSES'S STATIC DATA MEMBERS ARE STATIC. THEY DO NOT OPERATE OVER AN OBJECT.
# CLASSES'S PUBLIC INTERFACES ARE NOT ATTACHED TA SPECIFFIC OBJECT, SO THE self/this, WHICH CONTAINS THE OBJECTS's REFERENCE, IS NOT PRESENT

# WE CAN'T ACCESS INSTANCE VARIABLES/FUNCTIONS THROUGHT CLASSES'S/STATIC FUNCTIONS BCZ THE CLASS DOESN'T HAVE
# THE REFERENCE OF ANY OF IT'S INSTANCES/OBJECTS

# TO ACCESS A CLASS'S MEMBER THROUGHT A INSTANCE FUNCTION MEMBER WHE HAVE TO USE THE CLASS'S REFERENCE
# <CLASS_NAME>.<MEMBER_NAME>

class Car:
    __MAX_WHEELS = 4
    def __init__(self, type, model): #BOUND/ATTACHED TO A OBJECT
        self.model = model
        self.type = type
    
    @staticmethod
    def default_amount_of_wheels(): #UNBOUND/NOT ATTACHED TO A OBJECT
        return Car.__MAX_WHEELS

    @staticmethod
    def set_default_amount_of_wheels(amount): #UNBOUND/NOT ATTACHED TO A OBJECT
        Car.__MAX_WHEELS  = amount
        
    def wheels(self): #BOUND/ATTACHED TO A OBJECT
        return self.__MAX_WHEELS
    
    def max_wheels(self, amount): #BOUND/ATTACHED TO A OBJECT
        self.__MAX_WHEELS = amount
    
    def change_class_wheels(self, amount):
        __MAX_WHEELS = amount # __MAX_WHEELS IS A LOCAL VARIABLE
        print(__MAX_WHEELS)
    
    def change_class_wheels_using_name(self, amount):
        Car.__MAX_WHEELS = amount
        

print(Car.default_amount_of_wheels()) #4
lambo = Car("Lamborghini", "Gallardo")
lambo.max_wheels(2)
print(lambo.wheels()) #2
print(Car.default_amount_of_wheels()) #4
lambo.change_class_wheels(56) # DOES NOTHIG TO THE OBJECT OR CLASS
print(Car.default_amount_of_wheels()) #4
print(lambo.wheels()) #2

lambo.change_class_wheels_using_name(56) # CHANGE THE CLASS'S STATE
print(Car.default_amount_of_wheels()) #56
print(lambo.wheels()) #2
print(lambo.default_amount_of_wheels()) #56
print(Car.__MAX_WHEELS) # AttributeError: type object 'Car' has no attribute '__MAX_WHEELS'