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
    garage = Garage()
    if not garage.car and not garage.car:
        raise Exception("No available vehicles.")
    try:
        garage.car.drive()
    except AttributeError:
        garage.motorcycle.drive()