#OOP DESIGN CHALLENGE
class BasicCarSpec:
    def __init__(self, year, model, color):
        self.year = year
        self.model = model
        self.doors = doors
        self.color = color
    #Creating a private function to get the spec of the car object instantiated.
    def get_spec(self):
        return self.year
        return self.model
        return self.color
    #Now I am creating another class for a non standard benz, an AMG benz
    #This inherits from the BasicCarSpec class because everuy car will have those things.
class C63AMG(BasicCarSpec):
    def __init__(self, seats, exhaust):
        self.seats = seats
        self.exhaust = exhaust
class gWagon:
