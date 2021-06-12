class Garage:
    def __init__(self, car=None, motorcycle=None):
        self.car = car
        self.motorcycle = motorcycle

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print("Driving {}...".format(self.brand))


class Motorcycle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print("Driving {}...".format(self.brand))

if __name__ == "__main__":
    garage = Garage(motorcycle=Motorcycle("BMW", "M 1000 RR"))
    try:
        garage.car.drive()
    except AttributeError:
        garage.motorcycle.drive()