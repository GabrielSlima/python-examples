# STATIC DATA MEMBERS: THERE IS ONLY ONE COPY OF THEM FOR EVERY INSTANCE/OBJECT.

# CLASS VARIABLES (STATIC VARS/DATA MEMBERS) BECOMES INSTANCE VARIABLES
# WHEN A NEW OBJECT IS BROUGHT TO EXISTANCE IN PYTHON
# BUT THE CLASS MEMBER CAN BE ACCESS THROUGHT <CLASS_NAME>.<VAR_NAME>
 

class Car:
    MAX_WHEELS = 4
    def __init__(self, type, model):
        self.model = model
        self.type = type
    
    def show_class_member(self):
        return Car.MAX_WHEELS

print(Car.MAX_WHEELS) #STATIC VARIABLE - 4
lambo = Car("Lamborghini", "Gallardo")
lambo.MAX_WHEELS = 2 #INSTANCE VARIABLE
print(lambo.MAX_WHEELS) #2
print(Car.MAX_WHEELS) #4
print(lambo.show_class_member()) #4
print(Car.type) #AttributeError: type object 'Car' has no attribute 'type'
