class Garage:
    def __init__(self, car=None, motorcycle=None):
        self.car = car
        self.motorcycle = motorcycle
    
    def available_vehicle(self):
        return self.car or self.motorcycle

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print("Driving {}...".format(self.brand))

class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass

if __name__ == "__main__":
    garage = Garage(motorcycle=Motorcycle("BMW", "M 1000 RR"))
    vehicle = garage.available_vehicle()
    vehicle.drive()