
global_var = "GLOBAL VAR"

class Car:
    global global_var
    def __init__(self, itype):
        self.type = itype
    
    def show_type(self):
        return self.type
    
