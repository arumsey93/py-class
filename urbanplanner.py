import datetime

class Building:

    def __init__(self, address, stories):
        self.designer= "Alex"
        self.date_constructed= ""
        self.owner= ""
        self.address= address
        self.stories= stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, owner):
        self.owner = owner
        
    def order (self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories")

eight_hundred_eighth = Building("800 8th Street", 12)
eight_hundred_eighth.construct()
eight_hundred_eighth.purchase("Sean")
eight_hundred_eighth.order()