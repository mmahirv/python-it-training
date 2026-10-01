__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive
        
class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed
        
ferrari = SportsCar("Ferrari", "488 GTB", 2020, 330)
jeep = OffRoadVehicle("Jeep", "Wrangler", 2021, True)

print(f"Sports Car: {ferrari.make} {ferrari.model}, Year: {ferrari.year}, Max Speed: {ferrari.max_speed} km/h")
print(f"Off-Road Vehicle: {jeep.make} {jeep.model}, Year: {jeep.year}, Four Wheel Drive: {jeep.four_wheel_drive}")