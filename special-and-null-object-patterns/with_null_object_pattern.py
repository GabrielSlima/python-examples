class Garage:
    def __init__(self, car=None, motorcycle=None):
        self.car = car
        self.motorcycle = motorcycle
    
    def available_vehicle(self):
        return self.car or self.motorcycle or NullObject()


class Vehicle:
    def __init__(self, brand=None, model=None):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print("Driving {}...".format(self.brand))


class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


class NullObject(Vehicle):
    def drive(self):
        print("No available vehicles.")


if __name__ == "__main__":
    garage = Garage()
    vehicle = garage.available_vehicle()
    vehicle.drive()