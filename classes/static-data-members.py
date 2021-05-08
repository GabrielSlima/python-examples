# CLASS VARIABLES (STATIC VARS/DATA MEMBERS) BECOMES INSTANCE VARIABLES 
# WHEN A NEW OBJECT IS BROUGHT TO EXISTANCE

class Car:
    MAX_WHEELS = 4
    def __init__(self, type, model):
        self.model = model
        self.type = type

print(Car.MAX_WHEELS) #STATIC VARIABLE

lambo = Car("Lamborghini", "Gallardo")
lambo.MAX_WHEELS = 2 #INSTANCE VARIABLE

print(lambo.MAX_WHEELS)
print(Car.type) #AttributeError: type object 'Car' has no attribute 'type'
