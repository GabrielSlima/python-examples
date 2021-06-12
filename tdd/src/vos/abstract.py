class AbstractVo:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def exists(self):
        return self.name is not None or self.email is not None
