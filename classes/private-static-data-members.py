import pprint
# PRIVATE CLASS VARIABLES(STATIC) CAN'T BE ACCESSED OUTSIDE OF IT'S CLASS WITHOUT
# A PUBLIC INTERFACE

# THE PUBLIC INTERFACES TO ACCESS THE CLASSES'S STATIC DATA MEMBERS ARE STATIC. THEY DO NOT OPERATE OVER AN OBJECT.
# CLASSES'S PUBLIC INTERFACES ARE NOT ATTACHED TA SPECIFFIC OBJECT, SO THE self/this, WHICH CONTAINS THE OBJECTS's REFERENCE, IS NOT PRESENT

class Car:
    __MAX_WHEELS = 4
    def __init__(self, type, model):
        self.model = model
        self.type = type
    
    @staticmethod
    def default_amount_of_wheels():
        return Car.__MAX_WHEELS

    @staticmethod
    def set_default_amount_of_wheels(amount):
        Car.__MAX_WHEELS  = amount

#print(Car.__MAX_WHEELS) => AttributeError: type object 'Car' has no attribute '__MAX_WHEELS'
Car.__MAX_WHEELS = 2
print(pprint.pprint(Car.__dict__))

print(Car.default_amount_of_wheels()) #4
lambo = Car("Lamborghini", "Gallardo") #{'model': 'Gallardo', 'type': 'Lamborghini'}
print(lambo.default_amount_of_wheels()) #4

Car.set_default_amount_of_wheels(2)

print(Car.default_amount_of_wheels()) #2
print(lambo.default_amount_of_wheels()) #2
lambo = Car("Lamborghini", "Gallardo") #{'model': 'Gallardo', 'type': 'Lamborghini'}
print(lambo.default_amount_of_wheels()) #2

print(pprint.pprint(Car.__dict__)) #mappingproxy({'_Car__MAX_WHEELS': 2, ..)
print(lambo.__dict__) #mappingproxy({'_Car__MAX_WHEELS': 2, ..)

#print(lambo.__MAX_WHEELS) => AttributeError: type object 'Car' has no attribute '__MAX_WHEELS'
lambo.__MAX_WHEELS = 2
lambo.non_existing_attribute_on_template = 2 
print(lambo.__dict__) #{'model': 'Gallardo', 'type': 'Lamborghini', '__MAX_WHEELS': 2, 'non_existing_attribute_on_template': 2}
print(lambo.__MAX_WHEELS) #2