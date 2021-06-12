import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)


class Onwer:
    def __init__(self, name, email):
        self.email = email
        self.name = name
    
    def review(self, smart_phone):
        logging.info("Review scheduled for {}".format(smart_phone.name))
    
    def open(self, app_name, smart_phone):
        smart_phone.start(app_name)

    
class SmartPhone:
    def __init__(self, name, owner, apps):
        self.apps = apps
        self.name = name
        self.owner = owner
    
    def notify(self, message):
        logging.info("Message {} sent to {}".format(message, self.owner.name))

    def filter_by(self, name):
        found = None
        for app in list(self.apps):
            if app.name != name:
                continue
            found = app
        
        if not found:
            raise Exception("{} not found".format(name))
        
        return found
    
    def start(self, app_name):
        self.filter_by(app_name).start() # Invoke a behavior from a Object of type App


class App:
    def __init__(self, name):
        self.name = name
    
    def start(self):
        logging.info("{} started!".format(self.name.capitalize()))
    
    def stop(self):
        logging.info("{} stoped!".format(self.name).capitalize())


if __name__ == "__main__":
    defaul_apps = {
        App('calculator'),
        App('calendar'),
        App('dialer'),
        App('sms'),
        App('clock')
    }
    gabriel = Onwer('Gabriel', "gabriel@email.com")
    smart_phone = SmartPhone("SomeCoolSmartPhone", gabriel, defaul_apps)
    
    smart_phone.notify("Upcoming alarm in 10 minutes!")
    
    gabriel.review(smart_phone)
    
    gabriel.open('calculator', smart_phone)