#OOP DESIGN CHALLENGE
class basicCarSpec:
    def __init__(self, year, model, color):
        self.year = year
        self.model = model
        self.color = color
    def get_spec(self):
        print(f"{self.year} {self.model} {self.color}")
    #Now I am creating another class for a non standard benz, an AMG benz
    #This inherits from the basicCarSpec class because everuy car will have those things.
class C63AMG(basicCarSpec):
    def __init__(self, seats, exhaust):
        self.seats = seats
        self.exhaust = exhaust
    def get_seats(self):
        return self.seats
    def get_exhaust(self):
        return self.exhaust
class gWagon(basicCarSpec):
    def __init__(self, trim, top):
        self.trim = trim
        self.top = top
    def get_trim(self):
        return self.trim
    def get_top(self):
        return self.top
class maybach(basicCarSpec):
    def __init__(self, wheelbase, use):
        self.wheelbase = wheelbase
        self.use = use
    def get_wheelbase(self):
        return self.wheelbase
    def get_use(self):
        return self.use
#These 3 previous classes are for other mercedes models that can be instantiated.


myCar = basicCarSpec(2020, "sedan", "white")
myCar.get_spec()