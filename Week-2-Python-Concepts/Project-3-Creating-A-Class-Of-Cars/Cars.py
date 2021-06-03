class Cars:
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
    
    def print_model(self):
        print(self.model)

    def print_make_and_year(self, make, year):
        print(make)
        print(year)

my_cars = Cars("Ford", "F150", "2020")

my_cars.print_model()

print(my_cars.print_make_and_year("Civic", "1986"))