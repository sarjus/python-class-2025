class car:
    def __init__(self, registration_number, color, mileage, year):
        self.registration_number = registration_number
        self.color = color
        self.mileage = mileage
        self.year = year

    def print_info(self):
        print("Registration Number: " + self.registration_number)
        print("Color: " + self.color)
        print("Mileage: " + self.mileage)
        print("Year: " + self.year)

new_car = car('KL02BQ5653','Black', 14, 2022)
new_car.print_info()