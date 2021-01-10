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
    def __init__(self,  year, model, color, seats, exhaust):
        super().__init__(year, model, color)
        self.seats = seats
        self.exhaust = exhaust
    #Override original method to also print seats and exhaust.
    def get_spec(self):
        print(f"{self.year} {self.model} {self.color} {self.seats} {self.exhaust}")
    def get_seats(self):
        print(f"You opted for {self.seats}!")
    def get_exhaust(self):
        print(f"You opted for {self.exhaust}!")
class gWagon(basicCarSpec):
    def __init__(self, year, model, color, trim, top):
        self.trim = trim
        self.top = top
    def get_trim(self):
        print(self.trim)
    def get_top(self):
        print(self.top)
class maybach(basicCarSpec):
    def __init__(self, year, model, color, wheelbase, use):
        self.wheelbase = wheelbase
        self.use = use
    def get_spec(self):
        print(f"{self.year} {self.model} {self.color} {self.wheelbase} {self.use}")
    def get_wheelbase(self):
        print(self.wheelbase)
    def get_use(self):
        print(self.use)
#These 3 previous classes are for other mercedes models that can be instantiated.
#myCar = basicCarSpec(2020, "sedan", "white")
#myCar.get_spec()

myAMG = C63AMG(2020, "coupe", "black", "sport seats", "sport exhaust")
#myAMG.get_spec()
#myAMG.get_seats()
#myAMG.get_exhaust()

myAMG = C63AMG(2012, "sedan", "black", "comfort seats", "standard exhaust")
myAMG.get_spec()
